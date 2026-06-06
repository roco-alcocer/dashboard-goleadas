# -*- coding: utf-8 -*-
# ligas_under.py (V2) - Under 8.5 por pais+liga
# Usado por el dashboard (app.py) y por el bot (monitor.py).
# Generado desde ranking_under85_con_pais_bot2.xlsx
# Columnas: Pais | Liga/Serie/Division | % ganado Under 8.5 | N juegos
# Clave: "<pais_normalizado>|<liga_normalizada>"


def _normalizar(texto):
    if texto is None:
        return ""
    s = str(texto).strip().lower()
    s = s.replace("-", " ")
    s = " ".join(s.split())
    return s


# pais|liga -> {"pct","pct_num","juegos"}
UNDER_LIGAS = {
    "argentina|reserve league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 4},  # Argentina - Reserve League
    "argentina|torneo federal a": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Argentina - Torneo Federal A
    "australia|a league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Australia - A-League
    "australia|capital territory npl 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Australia - Capital Territory NPL 2
    "australia|new south wales npl 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Australia - New South Wales NPL 2
    "australia|nnsw league 1": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Australia - NNSW League 1
    "australia|queensland npl": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Australia - Queensland NPL
    "australia|south australia npl": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Australia - South Australia NPL
    "australia|south australia state league 1": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Australia - South Australia State League 1
    "australia|victoria npl": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Australia - Victoria NPL
    "australia|victoria npl 2": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Australia - Victoria NPL 2
    "australia|western australia state league 1": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Australia - Western Australia State League 1
    "austria|2. liga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Austria - 2. Liga
    "austria|bundesliga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Austria - Bundesliga
    "austria|frauenliga": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Austria - Frauenliga
    "austria|regionalliga ost": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Austria - Regionalliga - Ost
    "austria|regionalliga west": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Austria - Regionalliga - West
    "belgium|challenger pro league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Belgium - Challenger Pro League
    "belgium|first amateur division": {"pct": "100.0%", "pct_num": 100.0, "juegos": 3},  # Belgium - First Amateur Division
    "bosnia|1st league fbih": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Bosnia - 1st League - FBiH
    "brazil|acreano": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Brazil - Acreano
    "brazil|alagoano 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Brazil - Alagoano - 2
    "brazil|brasileiro u17": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Brazil - Brasileiro U17
    "brazil|kings cup": {"pct": "60.0%", "pct_num": 60.0, "juegos": 15},  # Brazil - Kings Cup
    "brazil|mineiro 1": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Brazil - Mineiro - 1
    "brazil|serie c": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Brazil - Serie C
    "brazil|serie d": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Brazil - Serie D
    "cameroon|elite one": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Cameroon - Elite One
    "canada|canadian premier league": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Canada - Canadian Premier League
    "china|league two": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # China - League Two
    "chinese taipei|taiwan football premier league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Chinese-Taipei - Taiwan Football Premier League
    "croatia|cup": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Croatia - Cup
    "cyprus|1. division": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Cyprus - 1. Division
    "cyprus|2. division": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Cyprus - 2. Division
    "czech republic|1. liga u19": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Czech-Republic - 1. Liga U19
    "czech republic|3. liga cfl a": {"pct": "100.0%", "pct_num": 100.0, "juegos": 3},  # Czech-Republic - 3. liga - CFL A
    "czech republic|3. liga msfl": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Czech-Republic - 3. liga - MSFL
    "czech republic|cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Czech-Republic - Cup
    "denmark|2. division": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Denmark - 2. Division
    "egypt|premier league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Egypt - Premier League
    "england|efl trophy": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # England - EFL Trophy
    "england|fa cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # England - FA Cup
    "england|fa wsl": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # England - FA WSL
    "england|fa youth cup": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # England - FA Youth Cup
    "england|league one": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # England - League One
    "england|league two": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # England - League Two
    "england|national league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # England - National League
    "england|national league north": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # England - National League - North
    "england|national league south": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # England - National League - South
    "england|national league cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # England - National League Cup
    "england|non league premier isthmian": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # England - Non League Premier - Isthmian
    "england|non league premier southern central": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # England - Non League Premier - Southern Central
    "england|non league premier southern south": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # England - Non League Premier - Southern South
    "england|premier league 2 division one": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # England - Premier League 2 Division One
    "england|professional development league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # England - Professional Development League
    "england|u18 premier league north": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # England - U18 Premier League - North
    "england|u18 premier league south": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # England - U18 Premier League - South
    "estonia|cup": {"pct": "33.3%", "pct_num": 33.3, "juegos": 3},  # Estonia - Cup
    "estonia|esiliiga a": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Estonia - Esiliiga A
    "estonia|esiliiga b": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Estonia - Esiliiga B
    "estonia|meistriliiga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Estonia - Meistriliiga
    "finland|kakkonen lohko a": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Finland - Kakkonen - Lohko A
    "finland|kakkonen lohko c": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Finland - Kakkonen - Lohko C
    "finland|kakkonen play offs": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Finland - Kakkonen - Play-offs
    "finland|suomen cup": {"pct": "0.0%", "pct_num": 0.0, "juegos": 3},  # Finland - Suomen Cup
    "finland|ykkösliiga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Finland - Ykkösliiga
    "france|national 1": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # France - National 1
    "france|national 2 group b": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # France - National 2 - Group B
    "gambia|gfa league": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Gambia - GFA League
    "germany|bundesliga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Germany - Bundesliga
    "germany|dfb junioren pokal": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Germany - DFB Junioren Pokal
    "germany|frauen bundesliga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Germany - Frauen Bundesliga
    "germany|oberliga bayern nord": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Germany - Oberliga - Bayern Nord
    "germany|oberliga mittelrhein": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Germany - Oberliga - Mittelrhein
    "germany|regionalliga bayern": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Germany - Regionalliga - Bayern
    "germany|regionalliga nord": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Germany - Regionalliga - Nord
    "germany|regionalliga nordost": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Germany - Regionalliga - Nordost
    "germany|regionalliga west": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Germany - Regionalliga - West
    "germany|u19 bundesliga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Germany - U19 Bundesliga
    "greece|super league 1": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Greece - Super League 1
    "hungary|magyar kupa": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Hungary - Magyar Kupa
    "hungary|nb iii southwest": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Hungary - NB III - Southwest
    "iceland|1. deild": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Iceland - 1. Deild
    "iceland|2. deild": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Iceland - 2. Deild
    "iceland|league cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Iceland - League Cup
    "iceland|úrvalsdeild": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Iceland - Úrvalsdeild
    "italy|campionato primavera 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Italy - Campionato Primavera - 2
    "italy|serie a cup women": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Italy - Serie A Cup Women
    "italy|serie a women": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Italy - Serie A Women
    "italy|serie d girone a": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Italy - Serie D - Girone A
    "italy|serie d girone b": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Italy - Serie D - Girone B
    "italy|serie d girone f": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Italy - Serie D - Girone F
    "italy|serie d girone i": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Italy - Serie D - Girone I
    "japan|j2 league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Japan - J2 League
    "japan|j2/j3 league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Japan - J2/J3 League
    "japan|j3 league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Japan - J3 League
    "kazakhstan|1. division": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Kazakhstan - 1. Division
    "kazakhstan|premier league": {"pct": "0.0%", "pct_num": 0.0, "juegos": 2},  # Kazakhstan - Premier League
    "kuwait|super cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Kuwait - Super Cup
    "kyrgyzstan|premier league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Kyrgyzstan - Premier League
    "latvia|1. liga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Latvia - 1. Liga
    "lebanon|premier league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Lebanon - Premier League
    "lithuania|a lyga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Lithuania - A Lyga
    "lithuania|cup": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Lithuania - Cup
    "macedonia|first league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Macedonia - First League
    "malaysia|mfl cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Malaysia - MFL Cup
    "malaysia|super league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Malaysia - Super League
    "malta|challenge league": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Malta - Challenge League
    "malta|premier league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Malta - Premier League
    "mauritania|premier league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Mauritania - Premier League
    "mexico|liga mx femenil": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Mexico - Liga MX Femenil
    "mexico|liga mx u21": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Mexico - Liga MX U21
    "mexico|liga premier serie a": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Mexico - Liga Premier Serie A
    "mexico|liga premier serie b": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Mexico - Liga Premier Serie B
    "netherlands|knvb beker": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Netherlands - KNVB Beker
    "netherlands|tweede divisie": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Netherlands - Tweede Divisie
    "nicaragua|copa nicaragua": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Nicaragua - Copa Nicaragua
    "nicaragua|primera division": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Nicaragua - Primera Division
    "nigeria|npfl": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Nigeria - NPFL
    "norway|1. division": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Norway - 1. Division
    "norway|3. division girone 1": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Norway - 3. Division - Girone 1
    "norway|3. division girone 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Norway - 3. Division - Girone 2
    "norway|3. division girone 3": {"pct": "100.0%", "pct_num": 100.0, "juegos": 3},  # Norway - 3. Division - Girone 3
    "norway|3. division girone 4": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Norway - 3. Division - Girone 4
    "norway|3. division girone 5": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Norway - 3. Division - Girone 5
    "norway|3. division girone 6": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Norway - 3. Division - Girone 6
    "norway|nasjonal u19 champions league": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Norway - Nasjonal U19 Champions League
    "norway|nm cupen": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Norway - NM Cupen
    "norway|toppserien": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Norway - Toppserien
    "panama|liga panameña de fútbol": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Panama - Liga Panameña de Fútbol
    "paraguay|division intermedia": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Paraguay - Division Intermedia
    "philippines|pfl": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Philippines - PFL
    "poland|central youth league": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Poland - Central Youth League
    "poland|ekstraliga women": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Poland - Ekstraliga Women
    "poland|iii liga group 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Poland - III Liga - Group 2
    "poland|iii liga group 3": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Poland - III Liga - Group 3
    "poland|iii liga group 4": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Poland - III Liga - Group 4
    "portugal|campeonato de portugal prio group a": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Portugal - Campeonato de Portugal Prio - Group A
    "portugal|campeonato de portugal prio group d": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Portugal - Campeonato de Portugal Prio - Group D
    "portugal|júniores u19": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Portugal - Júniores U19
    "portugal|primeira liga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Portugal - Primeira Liga
    "portugal|segunda liga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Portugal - Segunda Liga
    "portugal|taça de portugal": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Portugal - Taça de Portugal
    "qatar|stars league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Qatar - Stars League
    "romania|cupa româniei": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Romania - Cupa României
    "romania|liga 1 feminin": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Romania - Liga 1 Feminin
    "russia|cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Russia - Cup
    "russia|premier league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Russia - Premier League
    "russia|youth championship": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Russia - Youth Championship
    "san marino|campionato": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # San-Marino - Campionato
    "saudi arabia|pro league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Saudi-Arabia - Pro League
    "scotland|championship": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Scotland - Championship
    "scotland|league two": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Scotland - League Two
    "serbia|prva liga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Serbia - Prva Liga
    "singapore|premier league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Singapore - Premier League
    "slovakia|2. liga": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Slovakia - 2. liga
    "slovakia|i liga women": {"pct": "33.3%", "pct_num": 33.3, "juegos": 3},  # Slovakia - I Liga - Women
    "slovakia|super liga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Slovakia - Super Liga
    "slovenia|2. snl": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Slovenia - 2. SNL
    "south africa|premier soccer league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # South-Africa - Premier Soccer League
    "spain|copa federacion": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Spain - Copa Federacion
    "spain|primera división rfef group 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Spain - Primera División RFEF - Group 2
    "spain|segunda división": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Spain - Segunda División
    "spain|segunda división rfef group 5": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Spain - Segunda División RFEF - Group 5
    "spain|tercera división rfef group 14": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Spain - Tercera División RFEF - Group 14
    "spain|tercera división rfef group 16": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Spain - Tercera División RFEF - Group 16
    "spain|tercera división rfef group 18": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Spain - Tercera División RFEF - Group 18
    "spain|tercera división rfef group 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Spain - Tercera División RFEF - Group 2
    "spain|tercera división rfef group 7": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Spain - Tercera División RFEF - Group 7
    "sweden|allsvenskan": {"pct": "33.3%", "pct_num": 33.3, "juegos": 3},  # Sweden - Allsvenskan
    "sweden|division 2 norra götaland": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Sweden - Division 2 - Norra Götaland
    "sweden|division 2 norra svealand": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Sweden - Division 2 - Norra Svealand
    "sweden|division 2 södra götaland": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Sweden - Division 2 - Södra Götaland
    "sweden|division 2 södra svealand": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Sweden - Division 2 - Södra Svealand
    "sweden|division 2 västra götaland": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Sweden - Division 2 - Västra Götaland
    "sweden|elitettan": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Sweden - Elitettan
    "sweden|ettan södra": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Sweden - Ettan - Södra
    "switzerland|1. liga promotion": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Switzerland - 1. Liga Promotion
    "thailand|fa cup": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Thailand - FA Cup
    "thailand|thai league 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Thailand - Thai League 2
    "tunisia|ligue 1": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Tunisia - Ligue 1
    "tunisia|ligue 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Tunisia - Ligue 2
    "turkey|1. lig": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Turkey - 1. Lig
    "turkey|3. lig group 3": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Turkey - 3. Lig - Group 3
    "turkey|3. lig group 4": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Turkey - 3. Lig - Group 4
    "turkey|3. lig play offs": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Turkey - 3. Lig - Play-offs
    "turkey|türkiye kupası": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Turkey - Türkiye Kupası
    "ukraine|druha liga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Ukraine - Druha Liga
    "ukraine|u19 league": {"pct": "0.0%", "pct_num": 0.0, "juegos": 2},  # Ukraine - U19 League
    "uruguay|copa de la liga auf": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Uruguay - Copa De La Liga Auf
    "usa|major league soccer": {"pct": "80.0%", "pct_num": 80.0, "juegos": 5},  # USA - Major League Soccer
    "usa|mls next pro": {"pct": "33.3%", "pct_num": 33.3, "juegos": 3},  # USA - MLS Next Pro
    "usa|usl championship": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # USA - USL Championship
    "usa|usl super league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # USA - USL Super League
    "vietnam|v.league 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Vietnam - V.League 2
    "wales|premier league": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Wales - Premier League
    "world|afc champions league two": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - AFC Champions League Two
    "world|afc u17 asian cup women": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # World - AFC U17 Asian Cup - Women
    "world|afc women's champions league": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # World - AFC Women's Champions League
    "world|asian cup women qualification": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - Asian Cup Women - Qualification
    "world|cosafa u20 championship": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - COSAFA U20 Championship
    "world|cotif tournament": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - COTIF Tournament
    "world|friendlies": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # World - Friendlies
    "world|friendlies clubs": {"pct": "78.3%", "pct_num": 78.3, "juegos": 23},  # World - Friendlies Clubs
    "world|friendlies women": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - Friendlies Women
    "world|kings world cup nations": {"pct": "14.3%", "pct_num": 14.3, "juegos": 14},  # World - Kings World Cup Nations
    "world|uefa champions league women": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - UEFA Champions League Women
    "world|uefa europa league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - UEFA Europa League
    "world|uefa u17 championship qualification": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - UEFA U17 Championship - Qualification
    "world|uefa u21 championship qualification": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # World - UEFA U21 Championship - Qualification
    "world|uefa youth league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 4},  # World - UEFA Youth League
    "world|world cup u17": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # World - World Cup - U17
    "world|world cup u17 women": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - World Cup - U17 - Women
}


def under_liga(pais, liga):
    """Devuelve {"pct","pct_num","juegos"} del Under 8.5 para ese pais+liga, o None."""
    clave = _normalizar(pais) + "|" + _normalizar(liga)
    return UNDER_LIGAS.get(clave)
