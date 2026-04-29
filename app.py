"""
Dashboard Goleadas Tracker
"""

import os
import requests
from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

API_FOOTBALL_KEY = os.getenv("API_FOOTBALL_KEY")
URL_API = "https://v3.football.api-sports.io/fixtures"


def obtener_partidos_en_vivo():
    if not API_FOOTBALL_KEY:
        return []
    headers = {"x-apisports-key": API_FOOTBALL_KEY}
    parametros = {"live": "all"}
    try:
        respuesta = requests.get(URL_API, headers=headers, params=parametros, timeout=15)
        if respuesta.status_code == 200:
            return respuesta.json().get("response", [])
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []


def clasificar_estado(minuto, gol_local, gol_visitante):
    if minuto is None:
        return "fuera"
    diferencia = abs(gol_local - gol_visitante)
    max_goles = max(gol_local, gol_visitante)
    if minuto <= 25:
        if max_goles >= 4 and diferencia >= 4:
            return "alerta_activa"
        if max_goles == 3 and diferencia == 3 and minuto <= 25:
            return "cerca"
    if minuto <= 15:
        if max_goles == 3 and diferencia == 3:
            return "alerta_activa"
        if max_goles == 2 and diferencia == 2:
            return "cerca"
    if minuto <= 25:
        return "vigilando"
    return "fuera"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/partidos")
def api_partidos():
    partidos_raw = obtener_partidos_en_vivo()
    partidos = []
    ligas_set = set()
    alertas_count = 0
    cerca_count = 0
    for p in partidos_raw:
        try:
            minuto = p["fixture"]["status"]["elapsed"]
            gol_local = p["goals"]["home"] or 0
            gol_visitante = p["goals"]["away"] or 0
            estado = clasificar_estado(minuto, gol_local, gol_visitante)
            if estado == "alerta_activa":
                alertas_count += 1
            elif estado == "cerca":
                cerca_count += 1
            ligas_set.add(p["league"]["name"])
            partidos.append({
                "id": p["fixture"]["id"],
                "minuto": minuto if minuto else 0,
                "estado_partido": p["fixture"]["status"]["short"],
                "equipo_local": p["teams"]["home"]["name"],
                "logo_local": p["teams"]["home"]["logo"],
                "equipo_visitante": p["teams"]["away"]["name"],
                "logo_visitante": p["teams"]["away"]["logo"],
                "gol_local": gol_local,
                "gol_visitante": gol_visitante,
                "liga": p["league"]["name"],
                "logo_liga": p["league"]["logo"],
                "pais": p["league"]["country"],
                "bandera": p["league"]["flag"],
                "estado": estado
            })
        except Exception as e:
            continue
    orden = {"alerta_activa": 0, "cerca": 1, "vigilando": 2, "fuera": 3}
    partidos.sort(key=lambda x: (orden.get(x["estado"], 4), -x["minuto"]))
    return jsonify({
        "partidos": partidos,
        "stats": {
            "total": len(partidos),
            "alertas": alertas_count,
            "cerca": cerca_count,
            "ligas": len(ligas_set),
            "actualizado": datetime.now().strftime("%H:%M:%S")
        }
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)