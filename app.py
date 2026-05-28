"""
Dashboard Goleadas Tracker - V4
- Indicador historico por liga
- Detecta condicion 2-2 al min 25
- Alerta 4-0 / 0-4 hasta el minuto 34
- Letrero APUESTA PREMIUM para paises seleccionados
"""

import os
import requests
from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta, timezone
from ligas_promedios import obtener_indicador_liga

app = Flask(__name__)

API_FOOTBALL_KEY = os.getenv("API_FOOTBALL_KEY")
URL_API_LIVE = "https://v3.football.api-sports.io/fixtures"

# Paises con etiqueta APUESTA PREMIUM (API-Football los devuelve en ingles)
PAISES_PREMIUM = {"australia", "austria", "poland", "finland"}

def es_premium(pais):
    if not pais:
        return False
    return pais.strip().lower() in PAISES_PREMIUM


def consulta_api(parametros):
    if not API_FOOTBALL_KEY:
        return []
    headers = {"x-apisports-key": API_FOOTBALL_KEY}
    try:
        respuesta = requests.get(URL_API_LIVE, headers=headers, params=parametros, timeout=15)
        if respuesta.status_code == 200:
            return respuesta.json().get("response", [])
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


def obtener_partidos_en_vivo():
    return consulta_api({"live": "all"})


def obtener_proximos_partidos():
    hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    todos = consulta_api({"date": hoy, "status": "NS"})
    
    ahora = datetime.now(timezone.utc)
    en_dos_horas = ahora + timedelta(hours=2)
    proximos = []
    
    for p in todos:
        try:
            fecha_str = p["fixture"]["date"]
            fecha = datetime.fromisoformat(fecha_str.replace("Z", "+00:00"))
            if ahora <= fecha <= en_dos_horas:
                proximos.append(p)
        except Exception:
            continue
    
    return proximos


def clasificar_estado(minuto, gol_local, gol_visitante):
    if minuto is None:
        return "fuera"
    diferencia = abs(gol_local - gol_visitante)
    max_goles = max(gol_local, gol_visitante)
    
    # Alerta 4-0 al min 34
    if minuto <= 34:
        if max_goles >= 4 and diferencia >= 4:
            return "alerta_activa"
    
    # Alerta 2-2 al min 25
    if minuto <= 25:
        if gol_local == 2 and gol_visitante == 2:
            return "alerta_activa"
    
    # Cerca de 4-0 (3-0 entre min 16-25)
    if minuto <= 25:
        if max_goles == 3 and diferencia == 3 and minuto > 15:
            return "cerca"
    
    # Alerta 3-0 al min 15
    if minuto <= 15:
        if max_goles == 3 and diferencia == 3:
            return "alerta_activa"
        if max_goles == 2 and diferencia == 2:
            return "cerca"
    
    if minuto <= 34:
        return "vigilando"
    return "fuera"


def parsear_partido_vivo(p):
    minuto = p["fixture"]["status"]["elapsed"]
    gol_local = p["goals"]["home"] or 0
    gol_visitante = p["goals"]["away"] or 0
    estado = clasificar_estado(minuto, gol_local, gol_visitante)
    liga_nombre = p["league"]["name"]
    indicador = obtener_indicador_liga(liga_nombre)
    
    return {
        "id": p["fixture"]["id"],
        "tipo": "vivo",
        "minuto": minuto if minuto else 0,
        "estado_partido": p["fixture"]["status"]["short"],
        "equipo_local": p["teams"]["home"]["name"],
        "logo_local": p["teams"]["home"]["logo"],
        "equipo_visitante": p["teams"]["away"]["name"],
        "logo_visitante": p["teams"]["away"]["logo"],
        "gol_local": gol_local,
        "gol_visitante": gol_visitante,
        "liga": liga_nombre,
        "logo_liga": p["league"]["logo"],
        "pais": p["league"]["country"],
        "bandera": p["league"]["flag"],
        "estado": estado,
        "indicador_nivel": indicador["nivel"],
        "indicador_label": indicador["label"],
        "indicador_promedio": indicador["promedio"],
        "premium": es_premium(p["league"]["country"])
    }


def parsear_partido_proximo(p):
    fecha_str = p["fixture"]["date"]
    fecha_utc = datetime.fromisoformat(fecha_str.replace("Z", "+00:00"))
    fecha_mx = fecha_utc - timedelta(hours=6)
    hora_inicio = fecha_mx.strftime("%H:%M")
    
    ahora = datetime.now(timezone.utc)
    minutos_falta = int((fecha_utc - ahora).total_seconds() / 60)
    
    liga_nombre = p["league"]["name"]
    indicador = obtener_indicador_liga(liga_nombre)
    
    return {
        "id": p["fixture"]["id"],
        "tipo": "proximo",
        "hora_inicio": hora_inicio,
        "minutos_falta": minutos_falta,
        "equipo_local": p["teams"]["home"]["name"],
        "logo_local": p["teams"]["home"]["logo"],
        "equipo_visitante": p["teams"]["away"]["name"],
        "logo_visitante": p["teams"]["away"]["logo"],
        "liga": liga_nombre,
        "logo_liga": p["league"]["logo"],
        "pais": p["league"]["country"],
        "bandera": p["league"]["flag"],
        "estado": "proximo",
        "indicador_nivel": indicador["nivel"],
        "indicador_label": indicador["label"],
        "indicador_promedio": indicador["promedio"],
        "premium": es_premium(p["league"]["country"])
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/partidos")
def api_partidos():
    vivos_raw = obtener_partidos_en_vivo()
    partidos_vivos = []
    ligas_set = set()
    alertas_count = 0
    cerca_count = 0
    
    for p in vivos_raw:
        try:
            partido = parsear_partido_vivo(p)
            if partido["estado"] == "alerta_activa":
                alertas_count += 1
            elif partido["estado"] == "cerca":
                cerca_count += 1
            ligas_set.add(partido["liga"])
            partidos_vivos.append(partido)
        except Exception:
            continue
    
    proximos_raw = obtener_proximos_partidos()
    partidos_proximos = []
    
    for p in proximos_raw:
        try:
            partido = parsear_partido_proximo(p)
            ligas_set.add(partido["liga"])
            partidos_proximos.append(partido)
        except Exception:
            continue
    
    orden = {"alerta_activa": 0, "cerca": 1, "vigilando": 2, "fuera": 3}
    partidos_vivos.sort(key=lambda x: (orden.get(x["estado"], 4), -x["minuto"]))
    partidos_proximos.sort(key=lambda x: x["minutos_falta"])
    
    return jsonify({
        "partidos_vivos": partidos_vivos,
        "partidos_proximos": partidos_proximos,
        "stats": {
            "total_vivo": len(partidos_vivos),
            "total_proximos": len(partidos_proximos),
            "alertas": alertas_count,
            "cerca": cerca_count,
            "ligas": len(ligas_set),
            "actualizado": datetime.now().strftime("%H:%M:%S")
        }
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)