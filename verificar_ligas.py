"""
Verificador de ligas en API-Football
Comprueba si las ligas que apuestas están disponibles
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_FOOTBALL_KEY")

if not API_KEY:
    print("ERROR: No se encontro API_FOOTBALL_KEY en el archivo .env")
    exit()

URL_LEAGUES = "https://v3.football.api-sports.io/leagues"
headers = {"x-apisports-key": API_KEY}

# Lista de búsquedas basadas en tus apuestas reales
busquedas = [
    {"pais": "Iceland", "tipo": "U-19 / Juveniles"},
    {"pais": "Finland", "tipo": "Ligas menores"},
    {"pais": "Germany", "tipo": "Femenino", "filtro": "women"},
    {"pais": "Slovenia", "tipo": "Segunda/Tercera"},
    {"pais": "Mexico", "tipo": "Liga MX"},
    {"pais": "Norway", "tipo": "Femenino", "filtro": "women"},
    {"pais": "Israel", "tipo": "Femenino", "filtro": "women"},
]

print("=" * 70)
print("VERIFICACION DE COBERTURA - API-FOOTBALL")
print("=" * 70)

total_ligas_relevantes = 0

for b in busquedas:
    print(f"\n[{b['pais']}] - {b['tipo']}")
    print("-" * 70)
    params = {"country": b["pais"]}
    try:
        r = requests.get(URL_LEAGUES, headers=headers, params=params, timeout=10)
        if r.status_code != 200:
            print(f"  ERROR: {r.status_code}")
            continue
        ligas = r.json().get("response", [])
        
        # Filtrar por palabra clave si aplica
        if "filtro" in b:
            ligas_filtradas = [l for l in ligas if b["filtro"].lower() in l["league"]["name"].lower()]
        else:
            ligas_filtradas = ligas
        
        if not ligas_filtradas:
            print(f"  Sin coincidencias para '{b.get('filtro', 'todas')}' en {b['pais']}")
            continue
        
        for liga in ligas_filtradas[:10]:  # Mostrar máximo 10
            nombre = liga["league"]["name"]
            tipo = liga["league"]["type"]
            anio_actual = "Activa" if liga["seasons"][-1].get("current") else "Inactiva"
            print(f"  - {nombre} ({tipo}) - {anio_actual}")
            total_ligas_relevantes += 1
    except Exception as e:
        print(f"  ERROR: {e}")

print("\n" + "=" * 70)
print(f"TOTAL ligas relevantes encontradas: {total_ligas_relevantes}")
print("=" * 70)
print("\nSi ves todas las ligas que apuestas, NO necesitas cambiar de API.")
print("Si faltan algunas, anotalas y avisame para investigar alternativas.")