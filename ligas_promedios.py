"""
Tabla de promedios historicos de goles por liga
Fuente: datos publicos verificados (Sportradar, Footystats, sources oficiales)
NOTA: Esto es REFERENCIA HISTORICA, NO PREDICCION del partido actual.

Clasificacion basada en promedio de goles por partido:
- ALTA:  promedio >= 2.9 goles/partido
- MEDIA: promedio entre 2.5 y 2.89
- BAJA:  promedio < 2.5
"""

# Diccionario: clave = nombre exacto de la liga en API-Football
# valor = ('clasificacion', 'promedio_aprox')

PROMEDIOS_LIGAS = {
    # === LIGAS TOP CON MUCHOS GOLES (ALTA) ===
    "Bundesliga": ("alta", 3.14),
    "2. Bundesliga": ("alta", 2.95),
    "Premier League": ("alta", 2.93),
    "Major League Soccer": ("alta", 3.12),
    "MLS": ("alta", 3.12),
    "Eredivisie": ("alta", 3.05),
    "Liga Profesional Argentina": ("alta", 2.6),
    "Brasileirao Serie A": ("alta", 2.7),
    "Copa Libertadores": ("alta", 2.9),
    "UEFA Champions League": ("alta", 3.10),
    "UEFA Europa League": ("alta", 2.95),
    "UEFA Conference League": ("alta", 3.0),
    
    # === LIGAS MEXICANAS ===
    "Liga MX": ("alta", 2.95),
    "Liga MX Femenil": ("alta", 3.0),
    "Liga de Expansion MX": ("media", 2.6),
    
    # === LIGAS LATINOAMERICANAS ===
    "Liga Pro Serie A": ("media", 2.4),
    "Liga Pro Serie B": ("media", 2.5),
    "Primera A": ("media", 2.5),
    "Primera B": ("media", 2.4),
    "Liga 1": ("media", 2.4),
    "Primera Division": ("media", 2.5),
    "Categoria Primera A": ("media", 2.4),
    
    # === LIGAS EUROPEAS MEDIAS ===
    "Ligue 1": ("alta", 2.96),
    "Ligue 2": ("media", 2.5),
    "Serie A": ("media", 2.56),
    "Serie B": ("media", 2.4),
    "La Liga": ("media", 2.62),
    "La Liga 2": ("media", 2.4),
    "Segunda Division": ("media", 2.4),
    "Championship": ("media", 2.5),
    "League One": ("media", 2.6),
    "League Two": ("media", 2.6),
    "Primeira Liga": ("media", 2.5),
    "Liga Portugal 2": ("media", 2.4),
    "Eerste Divisie": ("alta", 3.0),
    "Belgian Pro League": ("media", 2.85),
    "Super League": ("media", 2.6),
    "Allsvenskan": ("media", 2.8),
    "Eliteserien": ("media", 2.85),
    "Superliga": ("media", 2.7),
    
    # === LIGAS FEMENINAS (suelen tener mas goles) ===
    "Frauen Bundesliga": ("alta", 3.5),
    "Bundesliga Women": ("alta", 3.5),
    "WSL": ("alta", 3.2),
    "Women's Super League": ("alta", 3.2),
    "NWSL": ("alta", 2.9),
    "Liga F": ("alta", 3.1),
    "Primera Division Femenina": ("alta", 3.1),
    "Serie A Women": ("alta", 3.0),
    "1. Division Women": ("alta", 3.3),
    "Toppserien": ("alta", 3.5),
    "Damallsvenskan": ("alta", 3.2),
    "WE League": ("media", 2.7),
    "Ligat Al Women": ("alta", 3.5),
    "A-League Women": ("alta", 3.0),
    
    # === LIGAS JUVENILES (suelen tener muchos goles) ===
    "U19 League": ("alta", 3.5),
    "U20 League": ("alta", 3.3),
    "U21 League": ("alta", 3.0),
    "U23 League": ("alta", 2.9),
    "Brasileiro U20": ("alta", 3.0),
    "Brasileiro U17": ("alta", 3.5),
    "Premier League U21": ("alta", 3.0),
    "Premier League U18": ("alta", 3.5),
    "U19 Bundesliga": ("alta", 3.5),
    "Junior Liga": ("alta", 3.2),
    
    # === LIGAS ESCANDINAVAS (tienden a tener mas goles) ===
    "Veikkausliiga": ("media", 2.7),
    "Ykkonen": ("media", 2.8),
    "Kakkonen": ("alta", 3.0),
    "Kakkonen - Lohko A": ("alta", 3.0),
    "Kakkonen - Lohko B": ("alta", 3.0),
    "Kakkonen - Lohko C": ("alta", 3.0),
    "Urvalsdeild": ("alta", 3.1),
    "1. Deild": ("alta", 3.0),
    "2. Deild": ("alta", 3.2),
    
    # === LIGAS MENORES ESLAVAS / BALCANES ===
    "1. SNL": ("media", 2.6),
    "2. SNL": ("media", 2.7),
    "3. SNL - East": ("alta", 3.0),
    "3. SNL - West": ("alta", 3.0),
    "Premijer Liga": ("media", 2.5),
    "I Liga": ("media", 2.4),
    "Ekstraklasa": ("media", 2.6),
    
    # === LIGAS BAJAS / DEFENSIVAS (BAJA) ===
    "Botola Pro": ("baja", 2.2),
    "Botola Pro 2": ("baja", 2.0),
    "Egyptian Premier League": ("baja", 2.0),
    "Saudi Pro League": ("media", 2.7),
    "UAE Pro League": ("media", 2.5),
    "Iraqi League": ("baja", 2.2),
    "K League 1": ("media", 2.5),
    "K League 2": ("media", 2.4),
    
    # === LIGAS ASIATICAS ===
    "J1 League": ("media", 2.6),
    "J2 League": ("media", 2.4),
    "Chinese Super League": ("media", 2.5),
    "A-League": ("media", 2.7),
    "Indian Super League": ("media", 2.6),
    
    # === COPAS GRANDES ===
    "FIFA World Cup": ("media", 2.8),
    "Copa America": ("media", 2.3),
    "EURO Championship": ("media", 2.5),
    "FA Cup": ("alta", 2.95),
    "Copa del Rey": ("media", 2.7),
    "DFB Pokal": ("alta", 3.2),
    "Coppa Italia": ("media", 2.6),
    "Copa Sudamericana": ("media", 2.6),
    "DFB Pokal - Women": ("alta", 4.0),
    
    # === LIGAS CON POCOS GOLES (BAJA) ===
    "Campionato": ("baja", 2.4),
    "Campionato Sammarinese": ("baja", 2.4),
    "I Liga - Andorra": ("baja", 2.3),
    "Premier League - Gibraltar": ("baja", 2.4),
    "National League": ("media", 2.7),
    "National League - North": ("media", 2.7),
    "National League - South": ("media", 2.7),
    "Non League Premier - Isthmian": ("media", 2.8),
    "Non League Premier - Southern South": ("media", 2.8),
    "Non League Premier - Southern Central": ("media", 2.8),
}


def obtener_indicador_liga(nombre_liga):
    """
    Devuelve el indicador de probabilidad histórica de Over 5.5 para una liga.
    Returns: dict con 'nivel' (alta/media/baja/nd) y 'promedio'
    """
    if not nombre_liga:
        return {"nivel": "nd", "promedio": None, "label": "N/D"}
    
    # Buscar coincidencia exacta primero
    if nombre_liga in PROMEDIOS_LIGAS:
        nivel, promedio = PROMEDIOS_LIGAS[nombre_liga]
        return {"nivel": nivel, "promedio": promedio, "label": _label(nivel)}
    
    # Buscar coincidencia parcial (case insensitive)
    nombre_lower = nombre_liga.lower()
    for liga_key, valor in PROMEDIOS_LIGAS.items():
        if liga_key.lower() in nombre_lower or nombre_lower in liga_key.lower():
            nivel, promedio = valor
            return {"nivel": nivel, "promedio": promedio, "label": _label(nivel)}
    
    # Si no hay match, intentar inferir por palabras clave
    if any(x in nombre_lower for x in ["women", "femenil", "femenin", "frauen", "damen"]):
        return {"nivel": "alta", "promedio": 3.0, "label": "ALTA HIST."}
    if any(x in nombre_lower for x in ["u17", "u18", "u19", "u20", "u21", "u23", "youth", "junior", "sub-"]):
        return {"nivel": "alta", "promedio": 3.2, "label": "ALTA HIST."}
    
    return {"nivel": "nd", "promedio": None, "label": "N/D"}


def _label(nivel):
    labels = {"alta": "ALTA HIST.", "media": "MEDIA HIST.", "baja": "BAJA HIST.", "nd": "N/D"}
    return labels.get(nivel, "N/D")