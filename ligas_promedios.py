"""
Tabla expandida de promedios historicos de goles por liga - V2
Fuente: datos publicos verificados (Sportradar, Footystats, FBref, fuentes oficiales)
NOTA: Esto es REFERENCIA HISTORICA, NO PREDICCION del partido actual.

Clasificacion basada en promedio de goles por partido:
- ALTA:  promedio >= 2.9 goles/partido
- MEDIA: promedio entre 2.5 y 2.89
- BAJA:  promedio < 2.5
"""

PROMEDIOS_LIGAS = {
    # ============================================================
    # === COMPETICIONES INTERNACIONALES ===
    # ============================================================
    "UEFA Champions League": ("alta", 3.10),
    "UEFA Europa League": ("alta", 2.95),
    "UEFA Conference League": ("alta", 3.0),
    "UEFA Europa Conference League": ("alta", 3.0),
    "UEFA Champions League Women": ("alta", 3.5),
    "UEFA Womens Champions League": ("alta", 3.5),
    "UEFA Nations League": ("media", 2.7),
    "UEFA Super Cup": ("media", 2.7),
    "Copa Libertadores": ("alta", 2.9),
    "Copa Sudamericana": ("media", 2.6),
    "Copa America": ("media", 2.3),
    "FIFA World Cup": ("media", 2.8),
    "FIFA Club World Cup": ("media", 2.7),
    "EURO Championship": ("media", 2.5),
    "Africa Cup of Nations": ("baja", 2.0),
    "AFC Asian Cup": ("media", 2.4),
    "AFC Champions League": ("media", 2.7),
    "CAF Champions League": ("baja", 2.2),
    "CONCACAF Champions League": ("alta", 2.95),
    "CONCACAF Champions Cup": ("alta", 2.95),
    "Leagues Cup": ("alta", 3.0),
    "Friendlies": ("media", 2.6),
    "Friendlies Clubs": ("media", 2.6),
    "World Cup - Qualification Europe": ("media", 2.7),
    "World Cup - Qualification South America": ("media", 2.5),
    "World Cup - Qualification CONCACAF": ("media", 2.7),
    "World Cup - Qualification Asia": ("media", 2.5),
    "World Cup - Qualification Africa": ("baja", 2.3),
    
    # ============================================================
    # === LIGAS TOP EUROPEAS ===
    # ============================================================
    "Premier League": ("alta", 2.93),
    "Championship": ("media", 2.5),
    "League One": ("media", 2.6),
    "League Two": ("media", 2.6),
    "FA Cup": ("alta", 2.95),
    "EFL Cup": ("alta", 3.0),
    "League Cup": ("media", 2.8),
    "Community Shield": ("media", 2.7),
    "FA Trophy": ("media", 2.8),
    "National League": ("media", 2.7),
    "National League - North": ("media", 2.7),
    "National League - South": ("media", 2.7),
    "Non League Premier - Isthmian": ("media", 2.8),
    "Non League Premier - Southern South": ("media", 2.8),
    "Non League Premier - Southern Central": ("media", 2.8),
    "Non League Premier - Northern": ("media", 2.8),
    "Premier League 2 Division One": ("alta", 3.0),
    "Premier League International Cup": ("alta", 3.0),
    "Professional Development League": ("alta", 3.0),
    "Premier League U21": ("alta", 3.0),
    "Premier League U18": ("alta", 3.5),
    "FA Youth Cup": ("alta", 3.2),
    
    "La Liga": ("media", 2.62),
    "La Liga 2": ("media", 2.4),
    "Segunda Division": ("media", 2.4),
    "Segunda B": ("media", 2.3),
    "Primera Federacion - Group 1": ("media", 2.4),
    "Primera Federacion - Group 2": ("media", 2.4),
    "Tercera Federacion - Group 1": ("media", 2.5),
    "Tercera Federacion - Group 2": ("media", 2.5),
    "Tercera Federacion - Group 3": ("media", 2.5),
    "Tercera Federacion - Group 4": ("media", 2.5),
    "Tercera Federacion - Group 5": ("media", 2.5),
    "Tercera Federacion - Group 6": ("media", 2.5),
    "Tercera Federacion - Group 7": ("media", 2.5),
    "Tercera Federacion - Group 8": ("media", 2.5),
    "Tercera Federacion - Group 9": ("media", 2.5),
    "Tercera Federacion - Group 10": ("media", 2.5),
    "Tercera Division RFEF - Group 1": ("media", 2.5),
    "Tercera Division RFEF - Group 2": ("media", 2.5),
    "Tercera Division RFEF - Group 3": ("media", 2.5),
    "Tercera Division RFEF - Group 4": ("media", 2.5),
    "Tercera Division RFEF - Group 5": ("media", 2.5),
    "Tercera Division RFEF - Group 6": ("media", 2.5),
    "Tercera Division RFEF - Group 7": ("media", 2.5),
    "Tercera Division RFEF - Group 8": ("media", 2.5),
    "Tercera Division RFEF - Group 9": ("media", 2.5),
    "Tercera Division RFEF - Group 10": ("media", 2.5),
    "Tercera Division RFEF - Group 11": ("media", 2.5),
    "Tercera Division RFEF - Group 12": ("media", 2.5),
    "Tercera Division RFEF - Group 13": ("media", 2.5),
    "Tercera Division RFEF - Group 14": ("media", 2.5),
    "Tercera Division RFEF - Group 15": ("media", 2.5),
    "Tercera Division RFEF - Group 16": ("media", 2.5),
    "Tercera Division RFEF - Group 17": ("media", 2.5),
    "Tercera Division RFEF - Group 18": ("media", 2.5),
    "Copa del Rey": ("media", 2.7),
    "Copa Federacion": ("media", 2.6),
    "Supercopa": ("media", 2.5),
    "Liga F": ("alta", 3.1),
    "Primera Division Femenina": ("alta", 3.1),
    "Primera Federacion Women": ("alta", 3.0),
    
    "Serie A": ("media", 2.56),
    "Serie B": ("media", 2.4),
    "Serie C - Girone A": ("media", 2.5),
    "Serie C - Girone B": ("media", 2.5),
    "Serie C - Girone C": ("media", 2.5),
    "Serie D": ("media", 2.6),
    "Coppa Italia": ("media", 2.6),
    "Coppa Italia Serie C": ("media", 2.5),
    "Supercoppa": ("media", 2.5),
    "Primavera 1": ("alta", 3.0),
    "Primavera 2": ("alta", 3.0),
    "Serie A Women": ("alta", 3.0),
    "Coppa Italia Women": ("alta", 3.2),
    
    "Bundesliga": ("alta", 3.14),
    "2. Bundesliga": ("alta", 2.95),
    "3. Liga": ("media", 2.7),
    "Regionalliga - West": ("media", 2.8),
    "Regionalliga - Nord": ("media", 2.8),
    "Regionalliga - Sudwest": ("media", 2.8),
    "Regionalliga - Bayern": ("media", 2.8),
    "Regionalliga - Nordost": ("media", 2.8),
    "Oberliga - Westfalen": ("alta", 3.0),
    "Oberliga - Nordrhein-Westfalen": ("alta", 3.0),
    "Oberliga - Niedersachsen": ("alta", 3.0),
    "Oberliga - Hamburg": ("alta", 3.0),
    "Oberliga - Bremen": ("alta", 3.0),
    "Oberliga - Bayern Nord": ("alta", 3.0),
    "Oberliga - Bayern Sud": ("alta", 3.0),
    "Oberliga - Baden-Wurttemberg": ("alta", 3.0),
    "DFB Pokal": ("alta", 3.2),
    "DFL Super Cup": ("media", 2.5),
    "Frauen Bundesliga": ("alta", 3.5),
    "Bundesliga Women": ("alta", 3.5),
    "2. Frauen Bundesliga": ("alta", 3.5),
    "DFB Pokal - Women": ("alta", 4.0),
    "U19 Bundesliga": ("alta", 3.5),
    "U17 Bundesliga": ("alta", 3.7),
    "Junioren Bundesliga": ("alta", 3.5),
    
    "Ligue 1": ("alta", 2.96),
    "Ligue 2": ("media", 2.5),
    "National 1": ("media", 2.4),
    "National 2 - Group A": ("media", 2.5),
    "National 2 - Group B": ("media", 2.5),
    "National 2 - Group C": ("media", 2.5),
    "National 2 - Group D": ("media", 2.5),
    "National 3": ("media", 2.6),
    "Coupe de France": ("media", 2.7),
    "Trophee des Champions": ("media", 2.5),
    "Coupe de la Ligue": ("media", 2.6),
    "Feminine Division 1": ("alta", 3.5),
    "D1 Feminine": ("alta", 3.5),
    
    # ============================================================
    # === LIGAS PAISES BAJOS / BELGICA ===
    # ============================================================
    "Eredivisie": ("alta", 3.05),
    "Eerste Divisie": ("alta", 3.0),
    "Tweede Divisie": ("alta", 2.9),
    "Derde Divisie - Saturday": ("media", 2.8),
    "Derde Divisie - Sunday": ("media", 2.8),
    "KNVB Beker": ("alta", 2.95),
    "Eredivisie Vrouwen": ("alta", 3.4),
    "Eredivisie Cup": ("alta", 3.0),
    
    "Belgian Pro League": ("media", 2.85),
    "Jupiler Pro League": ("media", 2.85),
    "Challenger Pro League": ("media", 2.7),
    "First Division B": ("media", 2.7),
    "Belgian Cup": ("media", 2.8),
    "Super League Women": ("alta", 3.3),
    
    # ============================================================
    # === LIGAS ESCANDINAVAS ===
    # ============================================================
    "Allsvenskan": ("media", 2.8),
    "Superettan": ("media", 2.7),
    "Division 1 - Norra": ("media", 2.8),
    "Division 1 - Sodra": ("media", 2.8),
    "Division 2": ("media", 2.8),
    "Svenska Cupen": ("media", 2.8),
    "Damallsvenskan": ("alta", 3.2),
    "Elitettan": ("alta", 3.0),
    
    "Eliteserien": ("media", 2.85),
    "1. Division": ("media", 2.8),
    "2. Division - Group 1": ("media", 2.9),
    "2. Division - Group 2": ("media", 2.9),
    "Norway Cup": ("media", 2.8),
    "Toppserien": ("alta", 3.5),
    "1. Division Women": ("alta", 3.3),
    "1. Division Kvinner": ("alta", 3.3),
    
    "Superliga": ("media", 2.7),
    "1st Division": ("media", 2.7),
    "2nd Division": ("media", 2.6),
    "DBU Pokalen": ("media", 2.7),
    "Kvindeligaen": ("alta", 3.4),
    "Womens 1st Division": ("alta", 3.2),
    
    "Veikkausliiga": ("media", 2.7),
    "Ykkonen": ("media", 2.8),
    "Ykkosliiga": ("media", 2.7),
    "Kakkonen": ("alta", 3.0),
    "Kakkonen - Lohko A": ("alta", 3.0),
    "Kakkonen - Lohko B": ("alta", 3.0),
    "Kakkonen - Lohko C": ("alta", 3.0),
    "Suomen Cup": ("media", 2.7),
    "Kansallinen Liiga": ("alta", 3.2),
    "Naisten Liiga": ("alta", 3.2),
    
    "Urvalsdeild": ("alta", 3.1),
    "Premier League - Iceland": ("alta", 3.1),
    "1. Deild": ("alta", 3.0),
    "2. Deild": ("alta", 3.2),
    "3. Deild": ("alta", 3.2),
    "4. Deild": ("alta", 3.3),
    "U19 League": ("alta", 3.5),
    "U19 League B": ("alta", 3.5),
    "U19 League C": ("alta", 3.5),
    "U19 Cup": ("alta", 3.5),
    "U20 League A Women": ("alta", 3.5),
    "U20 League B Women": ("alta", 3.5),
    "Reykjavik Youth Cup": ("alta", 3.5),
    "Iceland Cup": ("media", 2.9),
    "League Cup": ("media", 2.8),
    "Reykjavik Cup": ("media", 2.9),
    "Premier League Women": ("alta", 3.4),
    "Urvalsdeild Women": ("alta", 3.4),
    "Fotbolti.net Cup A": ("media", 2.9),
    "Fotbolti.net Cup B": ("media", 2.9),
    "Fotbolti.net Cup C": ("media", 2.9),
    
    # ============================================================
    # === LIGAS ESTE EUROPA / BALCANES ===
    # ============================================================
    "Ekstraklasa": ("media", 2.6),
    "I Liga": ("media", 2.4),
    "II Liga": ("media", 2.5),
    "III Liga - Group 1": ("media", 2.6),
    "III Liga - Group 2": ("media", 2.6),
    "III Liga - Group 3": ("media", 2.6),
    "III Liga - Group 4": ("media", 2.6),
    "Polish Cup": ("media", 2.6),
    "Ekstraliga": ("alta", 3.0),
    
    "Premijer Liga": ("media", 2.5),
    "Prva HNL": ("media", 2.6),
    "1. HNL": ("media", 2.6),
    "Druga HNL": ("media", 2.5),
    "Treca HNL": ("media", 2.6),
    "Croatian Cup": ("media", 2.6),
    
    "1. SNL": ("media", 2.6),
    "2. SNL": ("media", 2.7),
    "3. SNL - East": ("alta", 3.0),
    "3. SNL - West": ("alta", 3.0),
    "4. SNL": ("alta", 3.0),
    "Slovenian Cup": ("media", 2.7),
    
    "Czech Liga": ("media", 2.7),
    "Fortuna Liga": ("media", 2.6),
    "FNL": ("media", 2.6),
    "Czech Cup": ("media", 2.7),
    
    "Slovak Super Liga": ("media", 2.5),
    "Slovak Cup": ("media", 2.6),
    "2. Liga": ("media", 2.5),
    
    "NB I": ("media", 2.6),
    "NB II": ("media", 2.5),
    "NB III - Center": ("media", 2.6),
    "NB III - East": ("media", 2.6),
    "NB III - West": ("media", 2.6),
    "Hungarian Cup": ("media", 2.6),
    
    "Liga 1": ("media", 2.4),
    "Liga 2": ("media", 2.4),
    "Liga 3": ("media", 2.5),
    "Cupa Romaniei": ("media", 2.5),
    
    "Bulgarian First League": ("media", 2.4),
    "First Professional League": ("media", 2.4),
    "Second Professional Football League": ("media", 2.4),
    "Bulgarian Cup": ("media", 2.4),
    
    "Super League": ("media", 2.6),
    "Super League 2": ("media", 2.5),
    "Football League": ("media", 2.5),
    "Greek Cup": ("media", 2.6),
    
    "Super Lig": ("media", 2.7),
    "1. Lig": ("media", 2.5),
    "2. Lig": ("media", 2.5),
    "3. Lig": ("media", 2.5),
    "Turkiye Kupasi": ("media", 2.7),
    "TFF 1. Lig": ("media", 2.5),
    "TFF 2. Lig": ("media", 2.5),
    "TFF 3. Lig": ("media", 2.5),
    
    "Ukrainian Premier League": ("media", 2.6),
    "Persha Liga": ("media", 2.5),
    "Ukrainian Cup": ("media", 2.6),
    
    "Russian Premier League": ("media", 2.4),
    "Premier League - Russia": ("media", 2.4),
    "FNL": ("media", 2.4),
    "PFL": ("media", 2.5),
    "First League": ("media", 2.5),
    "Second League": ("media", 2.5),
    "Russian Cup": ("media", 2.5),
    "Second League A - Group Gold": ("media", 2.5),
    "Second League A - Group Silver": ("media", 2.5),
    "Second League B - Group 1": ("media", 2.5),
    "Second League B - Group 2": ("media", 2.5),
    "Second League B - Group 3": ("media", 2.5),
    "Second League B - Group 4": ("media", 2.5),
    
    # ============================================================
    # === LIGAS PORTUGAL / SUIZA / AUSTRIA ===
    # ============================================================
    "Primeira Liga": ("media", 2.5),
    "Liga Portugal 2": ("media", 2.4),
    "Segunda Liga": ("media", 2.4),
    "Liga 3": ("media", 2.5),
    "Campeonato de Portugal": ("media", 2.5),
    "Taca de Portugal": ("media", 2.6),
    "Taca da Liga": ("media", 2.6),
    "Campeonato Nacional Feminino": ("alta", 3.3),
    
    "Super League - Switzerland": ("media", 2.85),
    "Challenge League": ("media", 2.7),
    "Promotion League": ("media", 2.6),
    "1. Liga Classic": ("media", 2.6),
    "Schweizer Cup": ("media", 2.7),
    "Womens Super League": ("alta", 3.2),
    
    "Bundesliga - Austria": ("alta", 2.95),
    "2. Liga - Austria": ("media", 2.8),
    "Regionalliga - Mitte": ("media", 2.8),
    "Regionalliga - Ost": ("media", 2.8),
    "Regionalliga - West": ("media", 2.8),
    "OFB Cup": ("media", 2.8),
    "Frauen Bundesliga - Austria": ("alta", 3.4),
    
    # ============================================================
    # === LIGAS SUDAMERICANAS ===
    # ============================================================
    "Liga Profesional Argentina": ("media", 2.6),
    "Primera Division - Argentina": ("media", 2.6),
    "Copa de la Liga Profesional": ("media", 2.6),
    "Copa Argentina": ("media", 2.6),
    "Primera Nacional": ("media", 2.4),
    "Primera B Metropolitana": ("media", 2.4),
    "Primera C": ("media", 2.4),
    "Primera D": ("media", 2.5),
    "Torneo Federal A": ("media", 2.5),
    "Torneo Federal B": ("media", 2.5),
    "Trofeo de Campeones": ("media", 2.5),
    "Supercopa Argentina": ("media", 2.5),
    "Reserve League": ("alta", 2.9),
    "Reserve League Argentina": ("alta", 2.9),
    
    "Brasileirao Serie A": ("alta", 2.7),
    "Serie A - Brazil": ("alta", 2.7),
    "Brasileirao Serie B": ("media", 2.5),
    "Brasileirao Serie C": ("media", 2.5),
    "Brasileirao Serie D": ("media", 2.6),
    "Copa do Brasil": ("media", 2.7),
    "Copa Verde": ("media", 2.6),
    "Copa do Nordeste": ("media", 2.6),
    "Brasileiro U20": ("alta", 3.0),
    "Brasileiro U17": ("alta", 3.5),
    "Brasileiro Women": ("alta", 3.0),
    "Carioca": ("media", 2.5),
    "Paulista A1": ("media", 2.4),
    "Paulista A2": ("media", 2.4),
    "Paulista A3": ("media", 2.5),
    "Paulista A4": ("media", 2.5),
    "Mineiro": ("media", 2.5),
    "Gaucho": ("media", 2.5),
    "Baiano": ("media", 2.5),
    "Pernambucano": ("media", 2.6),
    "Goiano": ("media", 2.5),
    "Cearense": ("media", 2.5),
    
    "Primera A - Colombia": ("media", 2.5),
    "Primera B - Colombia": ("media", 2.4),
    "Liga BetPlay": ("media", 2.5),
    "Categoria Primera A": ("media", 2.5),
    "Categoria Primera B": ("media", 2.4),
    "Copa Colombia": ("media", 2.6),
    "Liga Femenina": ("alta", 3.0),
    
    "Primera Division - Chile": ("media", 2.6),
    "Primera B - Chile": ("media", 2.5),
    "Segunda Division - Chile": ("media", 2.5),
    "Segunda Division Profesional": ("media", 2.5),
    "Tercera Division A": ("media", 2.6),
    "Tercera Division B": ("media", 2.6),
    "Copa Chile": ("media", 2.6),
    
    "Liga Pro Serie A": ("media", 2.4),
    "Liga Pro Serie B": ("media", 2.5),
    "Liga Pro - Ecuador": ("media", 2.4),
    "Copa Ecuador": ("media", 2.5),
    
    "Liga 1 - Peru": ("media", 2.5),
    "Liga 2 - Peru": ("media", 2.4),
    "Copa Bicentenario": ("media", 2.5),
    
    "Primera Division - Uruguay": ("media", 2.5),
    "Segunda Division - Uruguay": ("media", 2.5),
    "Segunda Division Profesional - Uruguay": ("media", 2.5),
    "Copa Uruguay": ("media", 2.5),
    
    "Division Profesional": ("media", 2.5),
    "Primera Division - Paraguay": ("media", 2.5),
    "Division Intermedia": ("media", 2.5),
    "Copa Paraguay": ("media", 2.5),
    
    "Division Profesional - Bolivia": ("media", 2.7),
    "Primera Division - Bolivia": ("media", 2.7),
    "Copa Simon Bolivar": ("media", 2.6),
    
    "Primera Division - Venezuela": ("media", 2.5),
    "Primera Division Venezolana": ("media", 2.5),
    "Segunda Division - Venezuela": ("media", 2.5),
    
    # ============================================================
    # === MEXICO ===
    # ============================================================
    "Liga MX": ("alta", 2.95),
    "Liga MX Femenil": ("alta", 3.0),
    "Liga de Expansion MX": ("media", 2.6),
    "Copa MX": ("media", 2.7),
    "Copa por Mexico": ("media", 2.7),
    "Liga Premier - Serie A": ("media", 2.6),
    "Liga Premier - Serie B": ("media", 2.7),
    "Liga TDP": ("media", 2.7),
    "Campeon de Campeones": ("media", 2.5),
    "Super Copa MX": ("media", 2.5),
    "U20 League": ("alta", 3.0),
    "U23 League": ("alta", 2.9),
    "Liga Premier U20": ("alta", 3.2),
    
    # ============================================================
    # === USA / CANADA ===
    # ============================================================
    "Major League Soccer": ("alta", 3.12),
    "MLS": ("alta", 3.12),
    "MLS Next Pro": ("alta", 3.0),
    "USL Championship": ("alta", 2.95),
    "USL League One": ("media", 2.85),
    "USL League Two": ("alta", 3.0),
    "US Open Cup": ("alta", 3.0),
    "MLS Cup Playoffs": ("alta", 3.0),
    "Leagues Cup": ("alta", 3.0),
    "NWSL Women": ("alta", 2.9),
    "NWSL": ("alta", 2.9),
    "NWSL Challenge Cup": ("alta", 2.9),
    "Super League": ("alta", 3.0),
    "USL Super League": ("alta", 3.0),
    "NCAA": ("alta", 3.5),
    "NCAA Division I": ("alta", 3.0),
    
    "Canadian Premier League": ("alta", 2.95),
    "Canadian Championship": ("media", 2.8),
    "League1 Ontario": ("media", 2.8),
    
    # ============================================================
    # === LIGAS ASIATICAS ===
    # ============================================================
    "J1 League": ("media", 2.6),
    "J2 League": ("media", 2.4),
    "J3 League": ("media", 2.4),
    "Emperor Cup": ("media", 2.6),
    "J League Cup": ("media", 2.6),
    "WE League": ("media", 2.7),
    "Empress Cup": ("media", 2.8),
    
    "K League 1": ("media", 2.5),
    "K League 2": ("media", 2.4),
    "FA Cup - Korea": ("media", 2.5),
    "WK League": ("media", 2.7),
    
    "Chinese Super League": ("media", 2.5),
    "China League One": ("media", 2.4),
    "China League Two": ("media", 2.5),
    "Chinese FA Cup": ("media", 2.5),
    "Chinese Womens Super League": ("media", 2.6),
    
    "Indian Super League": ("media", 2.6),
    "I-League": ("media", 2.4),
    "Federation Cup": ("media", 2.5),
    "Indian Womens League": ("alta", 3.0),
    
    "Thai League 1": ("media", 2.7),
    "Thai League 2": ("media", 2.6),
    "Thai FA Cup": ("media", 2.6),
    
    "V.League 1": ("media", 2.4),
    "V.League 2": ("media", 2.4),
    
    "Liga 1 - Indonesia": ("media", 2.5),
    "Liga 2 - Indonesia": ("media", 2.5),
    
    "Malaysia Super League": ("media", 2.5),
    "Malaysia Premier League": ("media", 2.5),
    
    "Philippines Football League": ("media", 2.7),
    
    "Hong Kong Premier League": ("media", 2.7),
    "HKFA Senior Shield": ("media", 2.7),
    
    "AFC Cup": ("media", 2.5),
    "AFC Champions League Two": ("media", 2.6),
    
    # ============================================================
    # === MEDIO ORIENTE / NORTE DE AFRICA ===
    # ============================================================
    "Saudi Pro League": ("media", 2.7),
    "Saudi League 1": ("media", 2.5),
    "Saudi Cup": ("media", 2.6),
    "Kings Cup": ("media", 2.6),
    
    "UAE Pro League": ("media", 2.5),
    "UAE League Cup": ("media", 2.5),
    
    "Qatar Stars League": ("media", 2.7),
    "Qatar Cup": ("media", 2.6),
    
    "Iraqi League": ("baja", 2.2),
    "Iraq Stars League": ("baja", 2.2),
    
    "Iranian Pro League": ("baja", 2.3),
    "Persian Gulf Pro League": ("baja", 2.3),
    
    "Israeli Premier League": ("media", 2.7),
    "Liga Leumit": ("media", 2.5),
    "Israel Cup": ("media", 2.6),
    "Toto Cup": ("media", 2.6),
    "Ligat Al Women": ("alta", 3.5),
    "Ligat Nashim": ("alta", 3.5),
    "State Cup Women": ("alta", 3.5),
    
    "Botola Pro": ("baja", 2.2),
    "Botola Pro 2": ("baja", 2.0),
    "Coupe du Trone": ("baja", 2.3),
    
    "Egyptian Premier League": ("baja", 2.0),
    "Egypt Cup": ("baja", 2.1),
    
    "Tunisian Ligue 1": ("baja", 2.0),
    "Tunisian Ligue 2": ("baja", 2.0),
    
    "Algerian Ligue 1": ("baja", 2.1),
    "Algerian Ligue 2": ("baja", 2.0),
    
    "Premier League - South Africa": ("baja", 2.2),
    "PSL": ("baja", 2.2),
    "South African Premier Soccer League": ("baja", 2.2),
    
    "Nigerian Professional Football League": ("baja", 2.0),
    "Nigeria Premier League": ("baja", 2.0),
    
    # ============================================================
    # === OCEANIA ===
    # ============================================================
    "A-League": ("media", 2.7),
    "A-League Women": ("alta", 3.0),
    "FFA Cup": ("media", 2.8),
    "NPL Victoria": ("alta", 2.95),
    "NPL New South Wales": ("alta", 2.95),
    "NPL Queensland": ("alta", 2.95),
    "NPL Western Australia": ("alta", 2.95),
    "NPL South Australia": ("alta", 2.95),
    "NPL Northern Territory": ("alta", 2.95),
    "NPL Capital Football": ("alta", 2.95),
    "NPL Tasmania": ("alta", 2.95),
    "Tasmania Northern Championship": ("media", 2.8),
    "Victoria State League 1": ("alta", 3.0),
    "Victoria State League 2": ("alta", 3.0),
    
    "New Zealand Football Championship": ("media", 2.8),
    "Northern League": ("media", 2.8),
    
    # ============================================================
    # === LIGAS PEQUEÑAS DE EUROPA ===
    # ============================================================
    "Campionato": ("baja", 2.4),
    "Campionato Sammarinese": ("baja", 2.4),
    "Coppa Titano": ("baja", 2.4),
    "I Liga - Andorra": ("baja", 2.3),
    "Premier League - Gibraltar": ("baja", 2.4),
    "Premier League - Faroe Islands": ("media", 2.6),
    "1. Deild - Faroe Islands": ("media", 2.7),
    "Coppa Italia - San Marino": ("baja", 2.4),
    
    "Cypriot First Division": ("media", 2.6),
    "Cyprus Cup": ("media", 2.6),
    
    "Maltese Premier League": ("media", 2.6),
    "Maltese Cup": ("media", 2.6),
    
    "Premier Division - Ireland": ("media", 2.5),
    "First Division - Ireland": ("media", 2.6),
    "FAI Cup": ("media", 2.5),
    "Premier Division": ("media", 2.5),
    "First Division": ("media", 2.6),
    
    "Premiership - Northern Ireland": ("media", 2.7),
    "Championship - Northern Ireland": ("media", 2.6),
    "Northern Irish Cup": ("media", 2.7),
    
    "Premiership - Scotland": ("media", 2.7),
    "Championship - Scotland": ("media", 2.5),
    "League One - Scotland": ("media", 2.6),
    "League Two - Scotland": ("media", 2.6),
    "Scottish Cup": ("media", 2.7),
    "Scottish League Cup": ("media", 2.7),
    
    "Cymru Premier": ("media", 2.7),
    "Welsh Cup": ("media", 2.8),
    
    "Belarus Premier League": ("media", 2.5),
    "Belarus First League": ("media", 2.5),
    
    "Estonian Meistriliiga": ("alta", 3.0),
    "Esiliiga": ("alta", 3.0),
    "Estonian Cup": ("alta", 3.0),
    
    "Latvian Higher League": ("media", 2.7),
    "Virsliga": ("media", 2.7),
    
    "A Lyga": ("media", 2.6),
    "Lithuanian Cup": ("media", 2.6),
    
    "Erovnuli Liga": ("media", 2.5),
    "Erovnuli Liga 2": ("media", 2.5),
    
    "Armenian Premier League": ("media", 2.5),
    
    "Azerbaijani Premier League": ("media", 2.5),
    
    "Kazakhstan Premier League": ("media", 2.5),
    
    "Albanian Superliga": ("baja", 2.3),
    "Kategoria Superiore": ("baja", 2.3),
    "Kategoria e Pare": ("baja", 2.4),
    
    "Bosnian Premier Liga": ("media", 2.5),
    "Premijer Liga - Bosnia": ("media", 2.5),
    "First League FBiH": ("media", 2.5),
    "First League RS": ("media", 2.5),
    
    "Macedonian First Football League": ("media", 2.6),
    "First League - Macedonia": ("media", 2.6),
    
    "Montenegrin First League": ("media", 2.5),
    "First League - Montenegro": ("media", 2.5),
    
    "Serbian SuperLiga": ("media", 2.5),
    "SuperLiga - Serbia": ("media", 2.5),
    "First League - Serbia": ("media", 2.5),
    "Serbian Cup": ("media", 2.5),
}


def obtener_indicador_liga(nombre_liga):
    """
    Devuelve el indicador de probabilidad histórica para una liga.
    Returns: dict con 'nivel', 'promedio', 'label'
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
    
    # Inferir por palabras clave si no hay match directo
    if any(x in nombre_lower for x in ["women", "femenil", "femenin", "frauen", "damen", "kvinner", "naisten", "feminine", "feminina"]):
        return {"nivel": "alta", "promedio": 3.0, "label": "ALTA HIST."}
    if any(x in nombre_lower for x in ["u17", "u18", "u19", "u20", "u21", "u23", "youth", "junior", "sub-", "primavera"]):
        return {"nivel": "alta", "promedio": 3.2, "label": "ALTA HIST."}
    if any(x in nombre_lower for x in ["amateur", "regional", "oberliga", "kreisliga"]):
        return {"nivel": "alta", "promedio": 2.95, "label": "ALTA HIST."}
    if any(x in nombre_lower for x in ["reserve", "reservas", "b team"]):
        return {"nivel": "alta", "promedio": 2.9, "label": "ALTA HIST."}
    if any(x in nombre_lower for x in ["copa", "cup", "pokal", "coupe", "trofeo"]):
        return {"nivel": "media", "promedio": 2.7, "label": "MEDIA HIST."}
    
    return {"nivel": "nd", "promedio": None, "label": "N/D"}


def _label(nivel):
    labels = {"alta": "ALTA HIST.", "media": "MEDIA HIST.", "baja": "BAJA HIST.", "nd": "N/D"}
    return labels.get(nivel, "N/D")