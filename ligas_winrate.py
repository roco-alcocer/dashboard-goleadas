# -*- coding: utf-8 -*-
# ligas_winrate.py (V1)
# Generado desde ranking_ligas_pais_completo_365_dias_app.xlsx (365 dias)
# Columnas: Pais | Liga/Serie/Division | % ganado | N juegos
# Clave del diccionario: "<pais_normalizado>|<liga_normalizada>"


def _normalizar(texto):
    if texto is None:
        return ""
    s = str(texto).strip().lower()
    s = s.replace("-", " ")
    s = " ".join(s.split())
    return s


# pais|liga -> {"pct": "85.7%", "pct_num": 85.7, "juegos": 7}
WINRATE_LIGAS = {
    "argentina|liga profesional argentina": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Argentina - Liga Profesional Argentina
    "argentina|primera c": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Argentina - Primera C
    "argentina|reserve league": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Argentina - Reserve League
    "australia|a league women": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Australia - A-League Women
    "australia|australian championship": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Australia - Australian Championship
    "australia|capital territory npl 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Australia - Capital Territory NPL 2
    "australia|nnsw league 1": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Australia - NNSW League 1
    "australia|northern nsw npl": {"pct": "0.0%", "pct_num": 0.0, "juegos": 2},  # Australia - Northern NSW NPL
    "australia|queensland npl": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Australia - Queensland NPL
    "australia|tasmania npl": {"pct": "100.0%", "pct_num": 100.0, "juegos": 3},  # Australia - Tasmania NPL
    "australia|victoria npl": {"pct": "33.3%", "pct_num": 33.3, "juegos": 3},  # Australia - Victoria NPL
    "australia|western australia npl": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Australia - Western Australia NPL
    "austria|cup": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Austria - Cup
    "austria|frauenliga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Austria - Frauenliga
    "austria|regionalliga west": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Austria - Regionalliga - West
    "bahrain|king's cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Bahrain - King's Cup
    "belarus|1. division": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Belarus - 1. Division
    "belarus|premier league": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Belarus - Premier League
    "belgium|first amateur division": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Belgium - First Amateur Division
    "belgium|super league women": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Belgium - Super League Women
    "bhutan|premier league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Bhutan - Premier League
    "bolivia|primera división": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Bolivia - Primera División
    "bosnia|1st league rs": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Bosnia - 1st League - RS
    "bosnia|premijer liga": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Bosnia - Premijer Liga
    "brazil|acreano": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Brazil - Acreano
    "brazil|baiano 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Brazil - Baiano - 2
    "brazil|brasileiro u20 b": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Brazil - Brasileiro U20 B
    "brazil|brasileiro women": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Brazil - Brasileiro Women
    "brazil|capixaba": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Brazil - Capixaba
    "brazil|carioca c": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Brazil - Carioca C
    "brazil|catarinense 2": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Brazil - Catarinense - 2
    "brazil|cearense u20": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Brazil - Cearense U20
    "brazil|copa rio u20": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Brazil - Copa Rio U20
    "brazil|kings cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Brazil - Kings Cup
    "brazil|maranhense": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Brazil - Maranhense
    "brazil|mineiro u20": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Brazil - Mineiro U20
    "brazil|paranaense 1": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Brazil - Paranaense - 1
    "brazil|paulista u20": {"pct": "60.0%", "pct_num": 60.0, "juegos": 5},  # Brazil - Paulista - U20
    "brazil|paulista série b": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Brazil - Paulista Série B
    "brazil|são paulo youth cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Brazil - São Paulo Youth Cup
    "cambodia|c league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Cambodia - C-League
    "colombia|copa colombia": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Colombia - Copa Colombia
    "colombia|liga femenina": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Colombia - Liga Femenina
    "costa rica|liga de ascenso": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Costa-Rica - Liga de Ascenso
    "cyprus|2. division": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Cyprus - 2. Division
    "czech republic|1. liga u19": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Czech-Republic - 1. Liga U19
    "czech republic|3. liga cfl a": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Czech-Republic - 3. liga - CFL A
    "czech republic|3. liga cfl b": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Czech-Republic - 3. liga - CFL B
    "czech republic|3. liga msfl": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Czech-Republic - 3. liga - MSFL
    "czech republic|cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 5},  # Czech-Republic - Cup
    "denmark|2. division": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Denmark - 2. Division
    "denmark|3. division": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Denmark - 3. Division
    "denmark|dbu pokalen": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Denmark - DBU Pokalen
    "denmark|superliga": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Denmark - Superliga
    "egypt|league cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Egypt - League Cup
    "england|championship": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # England - Championship
    "england|fa cup": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # England - FA Cup
    "england|fa wsl": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # England - FA WSL
    "england|national league": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # England - National League
    "england|national league north": {"pct": "50.0%", "pct_num": 50.0, "juegos": 4},  # England - National League - North
    "england|national league south": {"pct": "0.0%", "pct_num": 0.0, "juegos": 2},  # England - National League - South
    "england|non league premier isthmian": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # England - Non League Premier - Isthmian
    "england|non league premier northern": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # England - Non League Premier - Northern
    "england|non league premier southern south": {"pct": "0.0%", "pct_num": 0.0, "juegos": 3},  # England - Non League Premier - Southern South
    "england|premier league 2 division one": {"pct": "0.0%", "pct_num": 0.0, "juegos": 3},  # England - Premier League 2 Division One
    "england|premier league cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # England - Premier League Cup
    "england|professional development league": {"pct": "0.0%", "pct_num": 0.0, "juegos": 2},  # England - Professional Development League
    "england|u18 premier league north": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # England - U18 Premier League - North
    "england|u18 premier league south": {"pct": "33.3%", "pct_num": 33.3, "juegos": 3},  # England - U18 Premier League - South
    "england|women's championship": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # England - Women's Championship
    "england|wsl cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # England - WSL Cup
    "estonia|cup": {"pct": "87.5%", "pct_num": 87.5, "juegos": 8},  # Estonia - Cup
    "estonia|esiliiga a": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Estonia - Esiliiga A
    "estonia|esiliiga b": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Estonia - Esiliiga B
    "faroe islands|meistaradeildin": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Faroe-Islands - Meistaradeildin
    "finland|kakkonen lohko a": {"pct": "25.0%", "pct_num": 25.0, "juegos": 4},  # Finland - Kakkonen - Lohko A
    "finland|kakkonen lohko b": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Finland - Kakkonen - Lohko B
    "finland|kakkonen play offs": {"pct": "50.0%", "pct_num": 50.0, "juegos": 4},  # Finland - Kakkonen - Play-offs
    "finland|kansallinen liiga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Finland - Kansallinen Liiga
    "finland|suomen cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 7},  # Finland - Suomen Cup
    "finland|veikkausliiga": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Finland - Veikkausliiga
    "finland|ykkönen": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Finland - Ykkönen
    "france|coupe de france": {"pct": "100.0%", "pct_num": 100.0, "juegos": 3},  # France - Coupe de France
    "france|ligue 1": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # France - Ligue 1
    "france|national 2 group a": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # France - National 2 - Group A
    "georgia|david kipiani cup": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Georgia - David Kipiani Cup
    "georgia|liga 3": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Georgia - Liga 3
    "germany|2. frauen bundesliga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Germany - 2. Frauen Bundesliga
    "germany|3. liga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Germany - 3. Liga
    "germany|bundesliga": {"pct": "0.0%", "pct_num": 0.0, "juegos": 2},  # Germany - Bundesliga
    "germany|dfb pokal": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Germany - DFB Pokal
    "germany|dfb pokal women": {"pct": "100.0%", "pct_num": 100.0, "juegos": 3},  # Germany - DFB Pokal - Women
    "germany|oberliga bremen": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Germany - Oberliga - Bremen
    "germany|regionalliga nord": {"pct": "75.0%", "pct_num": 75.0, "juegos": 4},  # Germany - Regionalliga - Nord
    "germany|u19 bundesliga": {"pct": "60.0%", "pct_num": 60.0, "juegos": 5},  # Germany - U19 Bundesliga
    "gibraltar|premier division": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Gibraltar - Premier Division
    "greece|cup": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Greece - Cup
    "greece|super league 2": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Greece - Super League 2
    "guatemala|liga nacional": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Guatemala - Liga Nacional
    "hungary|magyar kupa": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Hungary - Magyar Kupa
    "hungary|nb iii northeast": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Hungary - NB III - Northeast
    "hungary|nb iii northwest": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Hungary - NB III - Northwest
    "hungary|nb iii southeast": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Hungary - NB III - Southeast
    "hungary|nb iii southwest": {"pct": "100.0%", "pct_num": 100.0, "juegos": 3},  # Hungary - NB III - Southwest
    "iceland|1. deild": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Iceland - 1. Deild
    "iceland|cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 5},  # Iceland - Cup
    "iceland|league cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Iceland - League Cup
    "india|i league 2nd division": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # India - I-League - 2nd Division
    "indonesia|liga 1": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Indonesia - Liga 1
    "indonesia|liga 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Indonesia - Liga 2
    "israel|ligat ha'al": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Israel - Ligat Ha'al
    "israel|state cup": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Israel - State Cup
    "italy|campionato primavera 2": {"pct": "0.0%", "pct_num": 0.0, "juegos": 3},  # Italy - Campionato Primavera - 2
    "italy|serie d girone b": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Italy - Serie D - Girone B
    "italy|serie d girone c": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Italy - Serie D - Girone C
    "italy|serie d girone d": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Italy - Serie D - Girone D
    "italy|serie d girone h": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Italy - Serie D - Girone H
    "jamaica|premier league": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Jamaica - Premier League
    "japan|j3 league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Japan - J3 League
    "jordan|cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Jordan - Cup
    "jordan|league": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Jordan - League
    "kazakhstan|cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Kazakhstan - Cup
    "kyrgyzstan|premier league": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Kyrgyzstan - Premier League
    "laos|lao league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Laos - Lao League
    "lithuania|1 lyga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Lithuania - 1 Lyga
    "luxembourg|national division": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Luxembourg - National Division
    "macedonia|cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 3},  # Macedonia - Cup
    "malaysia|super league": {"pct": "33.3%", "pct_num": 33.3, "juegos": 3},  # Malaysia - Super League
    "malta|challenge league": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Malta - Challenge League
    "mexico|liga mx femenil": {"pct": "0.0%", "pct_num": 0.0, "juegos": 2},  # Mexico - Liga MX Femenil
    "mexico|liga premier serie a": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Mexico - Liga Premier Serie A
    "moldova|super liga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Moldova - Super Liga
    "mongolia|premier league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 7},  # Mongolia - Premier League
    "montenegro|second league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Montenegro - Second League
    "myanmar|national league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Myanmar - National League
    "netherlands|eredivisie women": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Netherlands - Eredivisie Women
    "netherlands|knvb beker": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Netherlands - KNVB Beker
    "new zealand|national league southern": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # New-Zealand - National League - Southern
    "northern ireland|premiership women": {"pct": "100.0%", "pct_num": 100.0, "juegos": 3},  # Northern-Ireland - Premiership Women
    "norway|1. division": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Norway - 1. Division
    "norway|2. division group 1": {"pct": "0.0%", "pct_num": 0.0, "juegos": 2},  # Norway - 2. Division - Group 1
    "norway|2. division group 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Norway - 2. Division - Group 2
    "norway|3. division girone 1": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Norway - 3. Division - Girone 1
    "norway|3. division girone 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 3},  # Norway - 3. Division - Girone 2
    "norway|3. division girone 3": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Norway - 3. Division - Girone 3
    "norway|3. division girone 4": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Norway - 3. Division - Girone 4
    "norway|3. division girone 5": {"pct": "100.0%", "pct_num": 100.0, "juegos": 3},  # Norway - 3. Division - Girone 5
    "norway|3. division girone 6": {"pct": "83.3%", "pct_num": 83.3, "juegos": 6},  # Norway - 3. Division - Girone 6
    "norway|eliteserien": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Norway - Eliteserien
    "norway|nasjonal u19 champions league": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Norway - Nasjonal U19 Champions League
    "norway|nm cupen": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Norway - NM Cupen
    "norway|toppserien": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Norway - Toppserien
    "panama|liga panameña de fútbol": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Panama - Liga Panameña de Fútbol
    "paraguay|division intermedia": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Paraguay - Division Intermedia
    "peru|primera división": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Peru - Primera División
    "peru|segunda división": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Peru - Segunda División
    "philippines|pfl": {"pct": "85.7%", "pct_num": 85.7, "juegos": 7},  # Philippines - PFL
    "poland|ekstraliga women": {"pct": "0.0%", "pct_num": 0.0, "juegos": 2},  # Poland - Ekstraliga Women
    "poland|i liga": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Poland - I Liga
    "poland|iii liga group 1": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Poland - III Liga - Group 1
    "poland|iii liga group 2": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Poland - III Liga - Group 2
    "poland|iii liga group 3": {"pct": "0.0%", "pct_num": 0.0, "juegos": 2},  # Poland - III Liga - Group 3
    "poland|iii liga group 4": {"pct": "75.0%", "pct_num": 75.0, "juegos": 4},  # Poland - III Liga - Group 4
    "portugal|campeonato de portugal prio group a": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Portugal - Campeonato de Portugal Prio - Group A
    "portugal|campeonato de portugal prio group c": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Portugal - Campeonato de Portugal Prio - Group C
    "portugal|liga 3": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Portugal - Liga 3
    "qatar|emir cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Qatar - Emir Cup
    "qatar|qsl cup": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Qatar - QSL Cup
    "romania|liga 1 feminin": {"pct": "100.0%", "pct_num": 100.0, "juegos": 4},  # Romania - Liga 1 Feminin
    "russia|cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Russia - Cup
    "russia|supreme division women": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Russia - Supreme Division Women
    "russia|youth championship": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Russia - Youth Championship
    "san marino|campionato": {"pct": "0.0%", "pct_num": 0.0, "juegos": 3},  # San-Marino - Campionato
    "scotland|challenge cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Scotland - Challenge Cup
    "scotland|championship": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Scotland - Championship
    "scotland|football league highland league": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Scotland - Football League - Highland League
    "scotland|league cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Scotland - League Cup
    "scotland|premiership": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Scotland - Premiership
    "serbia|prva liga": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Serbia - Prva Liga
    "slovakia|cup": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Slovakia - Cup
    "slovakia|i liga women": {"pct": "100.0%", "pct_num": 100.0, "juegos": 5},  # Slovakia - I Liga - Women
    "slovenia|1. snl": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Slovenia - 1. SNL
    "slovenia|cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Slovenia - Cup
    "south korea|k3 league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # South-Korea - K3 League
    "south korea|wk league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # South-Korea - WK-League
    "spain|la liga": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Spain - La Liga
    "spain|primera división femenina": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Spain - Primera División Femenina
    "spain|segunda división": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Spain - Segunda División
    "spain|segunda división rfef group 1": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Spain - Segunda División RFEF - Group 1
    "spain|segunda división rfef group 3": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Spain - Segunda División RFEF - Group 3
    "spain|tercera división rfef group 1": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Spain - Tercera División RFEF - Group 1
    "spain|tercera división rfef group 10": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Spain - Tercera División RFEF - Group 10
    "spain|tercera división rfef group 11": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Spain - Tercera División RFEF - Group 11
    "spain|tercera división rfef group 15": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Spain - Tercera División RFEF - Group 15
    "spain|tercera división rfef group 16": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Spain - Tercera División RFEF - Group 16
    "spain|tercera división rfef group 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Spain - Tercera División RFEF - Group 2
    "spain|tercera división rfef group 3": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Spain - Tercera División RFEF - Group 3
    "sweden|division 2 norra svealand": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Sweden - Division 2 - Norra Svealand
    "sweden|division 2 norrland": {"pct": "100.0%", "pct_num": 100.0, "juegos": 3},  # Sweden - Division 2 - Norrland
    "sweden|division 2 södra svealand": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Sweden - Division 2 - Södra Svealand
    "sweden|ettan norra": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Sweden - Ettan - Norra
    "sweden|svenska cupen": {"pct": "25.0%", "pct_num": 25.0, "juegos": 4},  # Sweden - Svenska Cupen
    "switzerland|1. liga promotion": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # Switzerland - 1. Liga Promotion
    "switzerland|schweizer cup": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Switzerland - Schweizer Cup
    "switzerland|super league": {"pct": "0.0%", "pct_num": 0.0, "juegos": 2},  # Switzerland - Super League
    "tajikistan|vysshaya liga": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Tajikistan - Vysshaya Liga
    "turkey|1. lig": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Turkey - 1. Lig
    "turkey|2. lig": {"pct": "66.7%", "pct_num": 66.7, "juegos": 6},  # Turkey - 2. Lig
    "turkey|3. lig group 1": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Turkey - 3. Lig - Group 1
    "turkey|3. lig group 2": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # Turkey - 3. Lig - Group 2
    "turkey|3. lig group 4": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Turkey - 3. Lig - Group 4
    "turkey|türkiye kupası": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Turkey - Türkiye Kupası
    "ukraine|druha liga": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Ukraine - Druha Liga
    "ukraine|u19 league": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Ukraine - U19 League
    "uruguay|copa uruguay": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Uruguay - Copa Uruguay
    "uruguay|primera división clausura": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Uruguay - Primera División - Clausura
    "uruguay|segunda división": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Uruguay - Segunda División
    "usa|major league soccer": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # USA - Major League Soccer
    "usa|mls next pro": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # USA - MLS Next Pro
    "uzbekistan|super league": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # Uzbekistan - Super League
    "wales|faw championship": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # Wales - FAW Championship
    "wales|league cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # Wales - League Cup
    "world|afc champions league two": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - AFC Champions League Two
    "world|afc u17 asian cup women": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - AFC U17 Asian Cup - Women
    "world|afc u20 asian cup women": {"pct": "100.0%", "pct_num": 100.0, "juegos": 5},  # World - AFC U20 Asian Cup - Women
    "world|afc u23 asian cup qualification": {"pct": "100.0%", "pct_num": 100.0, "juegos": 4},  # World - AFC U23 Asian Cup - Qualification
    "world|afc women's champions league": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # World - AFC Women's Champions League
    "world|agcff gulf champions league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - AGCFF Gulf Champions League
    "world|asean championship u23": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - ASEAN Championship U23
    "world|asean championship women": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # World - Asean Championship Women
    "world|asian cup women qualification": {"pct": "100.0%", "pct_num": 100.0, "juegos": 6},  # World - Asian Cup Women - Qualification
    "world|concacaf champions league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - CONCACAF Champions League
    "world|concacaf gold cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - CONCACAF Gold Cup
    "world|concacaf u20": {"pct": "100.0%", "pct_num": 100.0, "juegos": 4},  # World - CONCACAF U20
    "world|concacaf u20 qualification": {"pct": "100.0%", "pct_num": 100.0, "juegos": 3},  # World - CONCACAF U20 - Qualification
    "world|concacaf women u20": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - CONCACAF Women U20
    "world|conmebol libertadores femenina": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - CONMEBOL Libertadores Femenina
    "world|eaff e 1 football championship": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - EAFF E-1 Football Championship
    "world|fifa club world cup": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - FIFA Club World Cup
    "world|friendlies": {"pct": "75.0%", "pct_num": 75.0, "juegos": 4},  # World - Friendlies
    "world|friendlies clubs": {"pct": "61.1%", "pct_num": 61.1, "juegos": 36},  # World - Friendlies Clubs
    "world|friendlies women": {"pct": "100.0%", "pct_num": 100.0, "juegos": 5},  # World - Friendlies Women
    "world|kings world cup nations": {"pct": "100.0%", "pct_num": 100.0, "juegos": 8},  # World - Kings World Cup Nations
    "world|ofc pro league": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - OFC Pro League
    "world|uefa champions league": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # World - UEFA Champions League
    "world|uefa champions league women": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # World - UEFA Champions League Women
    "world|uefa europa cup women": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - UEFA Europa Cup - Women
    "world|uefa nations league women": {"pct": "0.0%", "pct_num": 0.0, "juegos": 1},  # World - UEFA Nations League - Women
    "world|uefa u17 championship qualification": {"pct": "100.0%", "pct_num": 100.0, "juegos": 2},  # World - UEFA U17 Championship - Qualification
    "world|uefa u19 championship qualification": {"pct": "75.0%", "pct_num": 75.0, "juegos": 4},  # World - UEFA U19 Championship - Qualification
    "world|uefa youth league": {"pct": "66.7%", "pct_num": 66.7, "juegos": 3},  # World - UEFA Youth League
    "world|world cup qualification europe": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # World - World Cup - Qualification Europe
    "world|world cup u17": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - World Cup - U17
    "world|world cup u20": {"pct": "100.0%", "pct_num": 100.0, "juegos": 1},  # World - World Cup - U20
    "world|world cup women qualification concacaf": {"pct": "100.0%", "pct_num": 100.0, "juegos": 9},  # World - World Cup - Women - Qualification Concacaf
    "world|world cup women qualification europe": {"pct": "50.0%", "pct_num": 50.0, "juegos": 2},  # World - World Cup - Women - Qualification Europe
}


def winrate_liga(pais, liga):
    """Devuelve {"pct","pct_num","juegos"} para ese pais+liga, o None si no existe."""
    clave = _normalizar(pais) + "|" + _normalizar(liga)
    return WINRATE_LIGAS.get(clave)
