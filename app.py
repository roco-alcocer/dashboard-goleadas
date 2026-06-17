"""
Dashboard Goleadas Tracker - V6
- Indicador unico por liga: Nivel + Promedio de goles (desde Excel)
- Las alertas SOLO suenan en ligas de nivel "Muy alta"
- Alerta 4-0 / 0-4 hasta el minuto 34
- Alerta 3-1 / 1-3 hasta el minuto 28
- Alerta de MEDIO TIEMPO: 4-0/0-4 o 3-1/1-3 al terminar el primer tiempo
- Letrero APUESTA PREMIUM para paises seleccionados
"""

import os
import requests
from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta, timezone
from ligas_nivel import nivel_liga

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


def clasificar_estado(minuto, gol_local, gol_visitante, estado_corto=None, nivel_clase=None):
    # Solo alertamos en ligas de nivel "Muy alta"
    if nivel_clase != "muy_alta":
        if minuto is None:
            return "fuera"
        return "vigilando" if minuto <= 34 else "fuera"
    
    diferencia = abs(gol_local - gol_visitante)
    max_goles = max(gol_local, gol_visitante)
    min_goles = min(gol_local, gol_visitante)
    
    # Alerta MEDIO TIEMPO: 4-0/0-4 o 3-1/1-3 al terminar el primer tiempo (igual que el bot)
    if estado_corto == "HT" and ((max_goles >= 4 and diferencia >= 4) or (max_goles == 3 and min_goles == 1)):
        return "alerta_activa"
    
    if minuto is None:
        return "fuera"
    
    # Alerta: 4-0 o 0-4 antes del minuto 34 (igual que el bot)
    if minuto <= 34 and max_goles >= 4 and diferencia >= 4:
        return "alerta_activa"
    
    # Alerta: 3-1 o 1-3 antes del minuto 28 (igual que el bot)
    if minuto <= 28 and max_goles == 3 and min_goles == 1:
        return "alerta_activa"
    
    # Cerca: 3-0 o 0-3 (a un gol del 4-0) antes del minuto 34
    if minuto <= 34 and max_goles == 3 and diferencia == 3:
        return "cerca"
    
    if minuto <= 34:
        return "vigilando"
    return "fuera"


def parsear_partido_vivo(p):
    minuto = p["fixture"]["status"]["elapsed"]
    gol_local = p["goals"]["home"] or 0
    gol_visitante = p["goals"]["away"] or 0
    estado_corto = p["fixture"]["status"]["short"]
    liga_nombre = p["league"]["name"]
    niv = nivel_liga(p["league"]["country"], liga_nombre)
    nivel_clase = niv["clase"] if niv else None
    estado = clasificar_estado(minuto, gol_local, gol_visitante, estado_corto, nivel_clase)
    
    return {
        "id": p["fixture"]["id"],
        "tipo": "vivo",
        "minuto": minuto if minuto else 0,
        "estado_partido": estado_corto,
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
        "premium": es_premium(p["league"]["country"]),
        "nivel": niv["nivel"] if niv else None,
        "nivel_clase": niv["clase"] if niv else None,
        "nivel_promedio": niv["promedio"] if niv else None,
        "nivel_n": niv["n"] if niv else None
    }


def parsear_partido_proximo(p):
    fecha_str = p["fixture"]["date"]
    fecha_utc = datetime.fromisoformat(fecha_str.replace("Z", "+00:00"))
    fecha_mx = fecha_utc - timedelta(hours=6)
    hora_inicio = fecha_mx.strftime("%H:%M")
    
    ahora = datetime.now(timezone.utc)
    minutos_falta = int((fecha_utc - ahora).total_seconds() / 60)
    
    liga_nombre = p["league"]["name"]
    niv = nivel_liga(p["league"]["country"], liga_nombre)
    
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
        "premium": es_premium(p["league"]["country"]),
        "nivel": niv["nivel"] if niv else None,
        "nivel_clase": niv["clase"] if niv else None,
        "nivel_promedio": niv["promedio"] if niv else None,
        "nivel_n": niv["n"] if niv else None
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