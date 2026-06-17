# -*- coding: utf-8 -*-
# ligas_nivel.py (V1) - Nivel + Promedio de goles por pais+liga
# Generado desde ligas_nivel_y_promedio_TODAS.xlsx (882 ligas)
# Columnas usadas: Nivel de la liga | Promedio de goles - N partidos
# La normalizacion quita acentos y guiones para evitar fallos de coincidencia.

import unicodedata


def _normalizar(texto):
    if texto is None:
        return ""
    s = str(texto).strip().lower()
    s = "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))
    s = s.replace("-", " ")
    return " ".join(s.split())


# pais|liga -> {"nivel","clase","promedio","n"}
NIVEL_LIGAS = {
    "albania|1st division": {"nivel": "Baja", "clase": "baja", "promedio": 2.42, "n": 201},  # Albania - 1st Division
    "albania|cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.59, "n": 44},  # Albania - Cup
    "albania|superliga": {"nivel": "Baja", "clase": "baja", "promedio": 2.22, "n": 190},  # Albania - Superliga
    "algeria|coupe nationale": {"nivel": "Baja", "clase": "baja", "promedio": 2.55, "n": 64},  # Algeria - Coupe Nationale
    "algeria|ligue 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.24, "n": 254},  # Algeria - Ligue 1
    "algeria|ligue 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.20, "n": 480},  # Algeria - Ligue 2
    "andorra|1a divisio": {"nivel": "Baja", "clase": "baja", "promedio": 2.67, "n": 112},  # Andorra - 1a Divisió
    "angola|girabola": {"nivel": "Baja", "clase": "baja", "promedio": 2.14, "n": 238},  # Angola - Girabola
    "antigua and barbuda|premier division": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.05, "n": 131},  # Antigua-And-Barbuda - Premier Division
    "argentina|copa argentina": {"nivel": "Baja", "clase": "baja", "promedio": 2.47, "n": 68},  # Argentina - Copa Argentina
    "argentina|liga profesional argentina": {"nivel": "Baja", "clase": "baja", "promedio": 1.99, "n": 510},  # Argentina - Liga Profesional Argentina
    "argentina|primera b metropolitana": {"nivel": "Baja", "clase": "baja", "promedio": 2.05, "n": 454},  # Argentina - Primera B Metropolitana
    "argentina|primera c": {"nivel": "Baja", "clase": "baja", "promedio": 1.97, "n": 448},  # Argentina - Primera C
    "argentina|primera nacional": {"nivel": "Baja", "clase": "baja", "promedio": 1.83, "n": 613},  # Argentina - Primera Nacional
    "argentina|reserve league": {"nivel": "Baja", "clase": "baja", "promedio": 2.47, "n": 584},  # Argentina - Reserve League
    "argentina|torneo federal a": {"nivel": "Baja", "clase": "baja", "promedio": 1.98, "n": 519},  # Argentina - Torneo Federal A
    "argentina|torneo promocional amateur": {"nivel": "Baja", "clase": "baja", "promedio": 2.11, "n": 89},  # Argentina - Torneo Promocional Amateur
    "armenia|cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.79, "n": 24},  # Armenia - Cup
    "armenia|first league": {"nivel": "Alta", "clase": "alta", "promedio": 3.27, "n": 239},  # Armenia - First League
    "armenia|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.58, "n": 135},  # Armenia - Premier League
    "aruba|division di honor": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.27, "n": 143},  # Aruba - Division di Honor
    "australia|a league": {"nivel": "Media", "clase": "media", "promedio": 2.82, "n": 163},  # Australia - A-League
    "australia|a league women": {"nivel": "Baja", "clase": "baja", "promedio": 2.75, "n": 117},  # Australia - A-League Women
    "australia|australia cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.55, "n": 31},  # Australia - Australia Cup
    "australia|australian championship": {"nivel": "Alta", "clase": "alta", "promedio": 3.22, "n": 55},  # Australia - Australian Championship
    "australia|brisbane premier league": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.35, "n": 82},  # Australia - Brisbane Premier League
    "australia|capital territory npl": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.32, "n": 111},  # Australia - Capital Territory NPL
    "australia|capital territory npl 2": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.10, "n": 50},  # Australia - Capital Territory NPL 2
    "australia|new south wales npl": {"nivel": "Baja", "clase": "baja", "promedio": 2.75, "n": 246},  # Australia - New South Wales NPL
    "australia|new south wales npl 2": {"nivel": "Alta", "clase": "alta", "promedio": 3.24, "n": 242},  # Australia - New South Wales NPL 2
    "australia|nnsw league 1": {"nivel": "Alta", "clase": "alta", "promedio": 3.69, "n": 91},  # Australia - NNSW League 1
    "australia|northern nsw npl": {"nivel": "Alta", "clase": "alta", "promedio": 3.40, "n": 156},  # Australia - Northern NSW NPL
    "australia|northern territory premier league": {"nivel": "Alta", "clase": "alta", "promedio": 3.24, "n": 45},  # Australia - Northern Territory Premier League
    "australia|npl nsw u20": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.82, "n": 151},  # Australia - Npl Nsw U20
    "australia|queensland npl": {"nivel": "Alta", "clase": "alta", "promedio": 3.59, "n": 147},  # Australia - Queensland NPL
    "australia|queensland premier league": {"nivel": "Alta", "clase": "alta", "promedio": 3.51, "n": 144},  # Australia - Queensland Premier League
    "australia|south australia npl": {"nivel": "Alta", "clase": "alta", "promedio": 3.60, "n": 140},  # Australia - South Australia NPL
    "australia|south australia state league 1": {"nivel": "Alta", "clase": "alta", "promedio": 3.43, "n": 137},  # Australia - South Australia State League 1
    "australia|tasmania northern championship": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 5.53, "n": 81},  # Australia - Tasmania Northern Championship
    "australia|tasmania npl": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.51, "n": 98},  # Australia - Tasmania NPL
    "australia|tasmania southern championship": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 5.76, "n": 90},  # Australia - Tasmania Southern Championship
    "australia|victoria npl": {"nivel": "Media", "clase": "media", "promedio": 3.09, "n": 173},  # Australia - Victoria NPL
    "australia|victoria npl 2": {"nivel": "Alta", "clase": "alta", "promedio": 3.41, "n": 179},  # Australia - Victoria NPL 2
    "australia|victoria premier league 2": {"nivel": "Media", "clase": "media", "promedio": 3.05, "n": 116},  # Australia - Victoria Premier League 2
    "australia|western australia npl": {"nivel": "Alta", "clase": "alta", "promedio": 3.54, "n": 152},  # Australia - Western Australia NPL
    "australia|western australia state league 1": {"nivel": "Alta", "clase": "alta", "promedio": 3.40, "n": 134},  # Australia - Western Australia State League 1
    "austria|2. liga": {"nivel": "Baja", "clase": "baja", "promedio": 2.68, "n": 222},  # Austria - 2. Liga
    "austria|bundesliga": {"nivel": "Baja", "clase": "baja", "promedio": 2.70, "n": 195},  # Austria - Bundesliga
    "austria|cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.59, "n": 63},  # Austria - Cup
    "austria|frauenliga": {"nivel": "Alta", "clase": "alta", "promedio": 3.35, "n": 112},  # Austria - Frauenliga
    "austria|landesliga burgenland": {"nivel": "Media", "clase": "media", "promedio": 3.02, "n": 238},  # Austria - Landesliga - Burgenland
    "austria|landesliga karnten": {"nivel": "Alta", "clase": "alta", "promedio": 3.28, "n": 226},  # Austria - Landesliga - Karnten
    "austria|landesliga niederosterreich": {"nivel": "Media", "clase": "media", "promedio": 3.16, "n": 224},  # Austria - Landesliga - Niederosterreich
    "austria|landesliga oberosterreich": {"nivel": "Media", "clase": "media", "promedio": 3.18, "n": 224},  # Austria - Landesliga - Oberosterreich
    "austria|landesliga salzburg": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.91, "n": 224},  # Austria - Landesliga - Salzburg
    "austria|landesliga steiermark": {"nivel": "Alta", "clase": "alta", "promedio": 3.60, "n": 238},  # Austria - Landesliga - Steiermark
    "austria|landesliga tirol": {"nivel": "Alta", "clase": "alta", "promedio": 3.69, "n": 168},  # Austria - Landesliga - Tirol
    "austria|landesliga vorarlbergliga": {"nivel": "Alta", "clase": "alta", "promedio": 3.44, "n": 174},  # Austria - Landesliga - Vorarlbergliga
    "austria|landesliga wien": {"nivel": "Media", "clase": "media", "promedio": 3.11, "n": 205},  # Austria - Landesliga - Wien
    "austria|regionalliga mitte": {"nivel": "Alta", "clase": "alta", "promedio": 3.53, "n": 240},  # Austria - Regionalliga - Mitte
    "austria|regionalliga ost": {"nivel": "Media", "clase": "media", "promedio": 3.14, "n": 272},  # Austria - Regionalliga - Ost
    "austria|regionalliga west": {"nivel": "Alta", "clase": "alta", "promedio": 3.39, "n": 271},  # Austria - Regionalliga - West
    "azerbaijan|birinci dasta": {"nivel": "Media", "clase": "media", "promedio": 2.82, "n": 136},  # Azerbaijan - Birinci Dasta
    "azerbaijan|cup": {"nivel": "Media", "clase": "media", "promedio": 3.05, "n": 39},  # Azerbaijan - Cup
    "azerbaijan|premyer liqa": {"nivel": "Baja", "clase": "baja", "promedio": 2.59, "n": 198},  # Azerbaijan - Premyer Liqa
    "bahrain|king's cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.37, "n": 19},  # Bahrain - King's Cup
    "bahrain|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.41, "n": 138},  # Bahrain - Premier League
    "bangladesh|federation cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.67, "n": 24},  # Bangladesh - Federation Cup
    "bangladesh|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.61, "n": 90},  # Bangladesh - Premier League
    "barbados|premier league": {"nivel": "Alta", "clase": "alta", "promedio": 3.49, "n": 87},  # Barbados - Premier League
    "belarus|1. division": {"nivel": "Media", "clase": "media", "promedio": 3.18, "n": 296},  # Belarus - 1. Division
    "belarus|coppa": {"nivel": "Alta", "clase": "alta", "promedio": 3.22, "n": 54},  # Belarus - Coppa
    "belarus|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.49, "n": 235},  # Belarus - Premier League
    "belgium|challenger pro league": {"nivel": "Media", "clase": "media", "promedio": 2.82, "n": 271},  # Belgium - Challenger Pro League
    "belgium|cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.56, "n": 218},  # Belgium - Cup
    "belgium|first amateur division": {"nivel": "Alta", "clase": "alta", "promedio": 3.28, "n": 433},  # Belgium - First Amateur Division
    "belgium|jupiler pro league": {"nivel": "Baja", "clase": "baja", "promedio": 2.68, "n": 321},  # Belgium - Jupiler Pro League
    "belgium|reserve pro league": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.04, "n": 156},  # Belgium - Reserve Pro League
    "belgium|second amateur division acff": {"nivel": "Media", "clase": "media", "promedio": 2.90, "n": 305},  # Belgium - Second Amateur Division - ACFF
    "belgium|second amateur division vfv a": {"nivel": "Alta", "clase": "alta", "promedio": 3.24, "n": 239},  # Belgium - Second Amateur Division - VFV A
    "belgium|second amateur division vfv b": {"nivel": "Alta", "clase": "alta", "promedio": 3.40, "n": 240},  # Belgium - Second Amateur Division - VFV B
    "belgium|super league women": {"nivel": "Media", "clase": "media", "promedio": 3.00, "n": 108},  # Belgium - Super League Women
    "belize|premier league": {"nivel": "Alta", "clase": "alta", "promedio": 3.65, "n": 48},  # Belize - Premier League
    "benin|championnat national": {"nivel": "Baja", "clase": "baja", "promedio": 1.86, "n": 298},  # Benin - Championnat National
    "bhutan|premier league": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.31, "n": 96},  # Bhutan - Premier League
    "bolivia|copa de la division profesional": {"nivel": "Alta", "clase": "alta", "promedio": 3.46, "n": 119},  # Bolivia - Copa de la División Profesional
    "bolivia|nacional b": {"nivel": "Alta", "clase": "alta", "promedio": 3.43, "n": 100},  # Bolivia - Nacional B
    "bolivia|primera division": {"nivel": "Alta", "clase": "alta", "promedio": 3.54, "n": 224},  # Bolivia - Primera División
    "bolivia|torneo amistoso de verano": {"nivel": "Alta", "clase": "alta", "promedio": 3.57, "n": 30},  # Bolivia - Torneo Amistoso de Verano
    "bosnia|1st league fbih": {"nivel": "Baja", "clase": "baja", "promedio": 2.57, "n": 182},  # Bosnia - 1st League - FBiH
    "bosnia|1st league rs": {"nivel": "Baja", "clase": "baja", "promedio": 2.52, "n": 196},  # Bosnia - 1st League - RS
    "bosnia|cup": {"nivel": "Media", "clase": "media", "promedio": 2.87, "n": 38},  # Bosnia - Cup
    "bosnia|premijer liga": {"nivel": "Baja", "clase": "baja", "promedio": 2.16, "n": 180},  # Bosnia - Premijer Liga
    "botswana|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.18, "n": 239},  # Botswana - Premier League
    "brazil|acreano": {"nivel": "Media", "clase": "media", "promedio": 2.91, "n": 34},  # Brazil - Acreano
    "brazil|alagoano": {"nivel": "Baja", "clase": "baja", "promedio": 2.06, "n": 34},  # Brazil - Alagoano
    "brazil|alagoano 2": {"nivel": "Media", "clase": "media", "promedio": 2.95, "n": 55},  # Brazil - Alagoano - 2
    "brazil|alagoano u20": {"nivel": "Alta", "clase": "alta", "promedio": 3.22, "n": 41},  # Brazil - Alagoano U20
    "brazil|amapaense": {"nivel": "Media", "clase": "media", "promedio": 3.06, "n": 33},  # Brazil - Amapaense
    "brazil|amazonense": {"nivel": "Baja", "clase": "baja", "promedio": 2.05, "n": 39},  # Brazil - Amazonense
    "brazil|baiano 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.56, "n": 48},  # Brazil - Baiano - 1
    "brazil|baiano 2": {"nivel": "Media", "clase": "media", "promedio": 3.16, "n": 45},  # Brazil - Baiano - 2
    "brazil|baiano u20": {"nivel": "Media", "clase": "media", "promedio": 3.04, "n": 224},  # Brazil - Baiano U20
    "brazil|brasileiro u17": {"nivel": "Alta", "clase": "alta", "promedio": 3.39, "n": 182},  # Brazil - Brasileiro U17
    "brazil|brasileiro u20 a": {"nivel": "Media", "clase": "media", "promedio": 3.12, "n": 220},  # Brazil - Brasileiro U20 A
    "brazil|brasileiro u20 b": {"nivel": "Media", "clase": "media", "promedio": 3.04, "n": 57},  # Brazil - Brasileiro U20 B
    "brazil|brasileiro women": {"nivel": "Baja", "clase": "baja", "promedio": 2.72, "n": 130},  # Brazil - Brasileiro Women
    "brazil|brasiliense": {"nivel": "Baja", "clase": "baja", "promedio": 2.56, "n": 50},  # Brazil - Brasiliense
    "brazil|brasiliense b": {"nivel": "Alta", "clase": "alta", "promedio": 3.68, "n": 28},  # Brazil - Brasiliense B
    "brazil|brasiliense u20": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.26, "n": 81},  # Brazil - Brasiliense U20
    "brazil|capixaba": {"nivel": "Baja", "clase": "baja", "promedio": 2.14, "n": 59},  # Brazil - Capixaba
    "brazil|capixaba b": {"nivel": "Media", "clase": "media", "promedio": 3.18, "n": 33},  # Brazil - Capixaba B
    "brazil|carioca 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.56, "n": 62},  # Brazil - Carioca - 1
    "brazil|carioca 2": {"nivel": "Baja", "clase": "baja", "promedio": 1.90, "n": 72},  # Brazil - Carioca - 2
    "brazil|carioca a2": {"nivel": "Baja", "clase": "baja", "promedio": 2.05, "n": 78},  # Brazil - Carioca A2
    "brazil|carioca b2": {"nivel": "Baja", "clase": "baja", "promedio": 2.58, "n": 38},  # Brazil - Carioca B2
    "brazil|carioca c": {"nivel": "Media", "clase": "media", "promedio": 3.19, "n": 100},  # Brazil - Carioca C
    "brazil|carioca u20": {"nivel": "Baja", "clase": "baja", "promedio": 2.55, "n": 87},  # Brazil - Carioca U20
    "brazil|catarinense 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.40, "n": 70},  # Brazil - Catarinense - 1
    "brazil|catarinense 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.40, "n": 82},  # Brazil - Catarinense - 2
    "brazil|catarinense u20": {"nivel": "Media", "clase": "media", "promedio": 3.00, "n": 95},  # Brazil - Catarinense U20
    "brazil|cearense 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.19, "n": 43},  # Brazil - Cearense - 1
    "brazil|cearense 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.20, "n": 50},  # Brazil - Cearense - 2
    "brazil|cearense u20": {"nivel": "Media", "clase": "media", "promedio": 2.86, "n": 84},  # Brazil - Cearense U20
    "brazil|copa alagoas": {"nivel": "Media", "clase": "media", "promedio": 3.00, "n": 28},  # Brazil - Copa Alagoas
    "brazil|copa centro oeste": {"nivel": "Baja", "clase": "baja", "promedio": 2.44, "n": 34},  # Brazil - Copa Centro-Oeste
    "brazil|copa do brasil": {"nivel": "Baja", "clase": "baja", "promedio": 2.10, "n": 156},  # Brazil - Copa Do Brasil
    "brazil|copa do brasil u17": {"nivel": "Alta", "clase": "alta", "promedio": 3.53, "n": 45},  # Brazil - Copa do Brasil U17
    "brazil|copa do brasil u20": {"nivel": "Baja", "clase": "baja", "promedio": 2.58, "n": 45},  # Brazil - Copa do Brasil U20
    "brazil|copa do nordeste": {"nivel": "Baja", "clase": "baja", "promedio": 2.76, "n": 68},  # Brazil - Copa do Nordeste
    "brazil|copa espirito santo": {"nivel": "Baja", "clase": "baja", "promedio": 2.60, "n": 55},  # Brazil - Copa Espírito Santo
    "brazil|copa fares lopes": {"nivel": "Baja", "clase": "baja", "promedio": 2.20, "n": 25},  # Brazil - Copa Fares Lopes
    "brazil|copa gaucha": {"nivel": "Baja", "clase": "baja", "promedio": 2.40, "n": 57},  # Brazil - Copa Gaúcha
    "brazil|copa norte": {"nivel": "Alta", "clase": "alta", "promedio": 3.56, "n": 34},  # Brazil - Copa Norte
    "brazil|copa paulista": {"nivel": "Baja", "clase": "baja", "promedio": 2.11, "n": 130},  # Brazil - Copa Paulista
    "brazil|copa rio": {"nivel": "Baja", "clase": "baja", "promedio": 1.63, "n": 46},  # Brazil - Copa Rio
    "brazil|copa rio u20": {"nivel": "Media", "clase": "media", "promedio": 2.97, "n": 61},  # Brazil - Copa Rio U20
    "brazil|copa santa catarina": {"nivel": "Baja", "clase": "baja", "promedio": 2.75, "n": 63},  # Brazil - Copa Santa Catarina
    "brazil|copa sul sudeste": {"nivel": "Baja", "clase": "baja", "promedio": 2.69, "n": 42},  # Brazil - Copa Sul-Sudeste
    "brazil|estadual junior u20": {"nivel": "Baja", "clase": "baja", "promedio": 2.61, "n": 64},  # Brazil - Estadual Junior U20
    "brazil|gaucho 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.28, "n": 64},  # Brazil - Gaúcho - 1
    "brazil|gaucho 2": {"nivel": "Baja", "clase": "baja", "promedio": 1.77, "n": 70},  # Brazil - Gaúcho - 2
    "brazil|gaucho 3": {"nivel": "Baja", "clase": "baja", "promedio": 2.74, "n": 35},  # Brazil - Gaúcho - 3
    "brazil|goiano 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.51, "n": 70},  # Brazil - Goiano - 1
    "brazil|goiano 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.33, "n": 36},  # Brazil - Goiano - 2
    "brazil|goiano 3": {"nivel": "Media", "clase": "media", "promedio": 3.18, "n": 67},  # Brazil - Goiano - 3
    "brazil|goiano u20": {"nivel": "Baja", "clase": "baja", "promedio": 2.74, "n": 80},  # Brazil - Goiano U20
    "brazil|kings cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 8.65, "n": 31},  # Brazil - Kings Cup
    "brazil|maranhense": {"nivel": "Baja", "clase": "baja", "promedio": 1.97, "n": 36},  # Brazil - Maranhense
    "brazil|maranhense 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.62, "n": 47},  # Brazil - Maranhense - 2
    "brazil|matogrossense": {"nivel": "Baja", "clase": "baja", "promedio": 1.89, "n": 53},  # Brazil - Matogrossense
    "brazil|matogrossense 2": {"nivel": "Media", "clase": "media", "promedio": 3.00, "n": 50},  # Brazil - Matogrossense 2
    "brazil|mineiro 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.32, "n": 59},  # Brazil - Mineiro - 1
    "brazil|mineiro 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.14, "n": 37},  # Brazil - Mineiro - 2
    "brazil|mineiro 3": {"nivel": "Baja", "clase": "baja", "promedio": 2.59, "n": 51},  # Brazil - Mineiro - 3
    "brazil|mineiro u20": {"nivel": "Media", "clase": "media", "promedio": 2.91, "n": 140},  # Brazil - Mineiro U20
    "brazil|paraense": {"nivel": "Baja", "clase": "baja", "promedio": 2.14, "n": 44},  # Brazil - Paraense
    "brazil|paraense a3": {"nivel": "Media", "clase": "media", "promedio": 3.05, "n": 37},  # Brazil - Paraense A3
    "brazil|paraense u20": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.88, "n": 88},  # Brazil - Paraense U20
    "brazil|paraibano": {"nivel": "Baja", "clase": "baja", "promedio": 2.35, "n": 51},  # Brazil - Paraibano
    "brazil|paraibano 2": {"nivel": "Alta", "clase": "alta", "promedio": 3.21, "n": 52},  # Brazil - Paraibano 2
    "brazil|paraibano u20": {"nivel": "Media", "clase": "media", "promedio": 3.12, "n": 66},  # Brazil - Paraibano U20
    "brazil|paranaense 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.44, "n": 54},  # Brazil - Paranaense - 1
    "brazil|paranaense 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.55, "n": 69},  # Brazil - Paranaense - 2
    "brazil|paranaense 3": {"nivel": "Baja", "clase": "baja", "promedio": 2.52, "n": 58},  # Brazil - Paranaense - 3
    "brazil|paranaense u20": {"nivel": "Media", "clase": "media", "promedio": 3.03, "n": 92},  # Brazil - Paranaense U20
    "brazil|paulista a1": {"nivel": "Baja", "clase": "baja", "promedio": 2.33, "n": 72},  # Brazil - Paulista - A1
    "brazil|paulista a2": {"nivel": "Baja", "clase": "baja", "promedio": 2.35, "n": 150},  # Brazil - Paulista - A2
    "brazil|paulista a3": {"nivel": "Baja", "clase": "baja", "promedio": 2.22, "n": 134},  # Brazil - Paulista - A3
    "brazil|paulista a4": {"nivel": "Baja", "clase": "baja", "promedio": 1.93, "n": 133},  # Brazil - Paulista - A4
    "brazil|paulista u20": {"nivel": "Media", "clase": "media", "promedio": 2.89, "n": 309},  # Brazil - Paulista - U20
    "brazil|paulista serie b": {"nivel": "Baja", "clase": "baja", "promedio": 2.77, "n": 144},  # Brazil - Paulista Série B
    "brazil|pernambucano 1": {"nivel": "Media", "clase": "media", "promedio": 2.92, "n": 38},  # Brazil - Pernambucano - 1
    "brazil|pernambucano 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.42, "n": 43},  # Brazil - Pernambucano - 2
    "brazil|pernambucano u20": {"nivel": "Media", "clase": "media", "promedio": 2.92, "n": 50},  # Brazil - Pernambucano - U20
    "brazil|piauiense": {"nivel": "Baja", "clase": "baja", "promedio": 2.21, "n": 34},  # Brazil - Piauiense
    "brazil|piauiense 2": {"nivel": "Baja", "clase": "baja", "promedio": 1.65, "n": 20},  # Brazil - Piauiense - 2
    "brazil|potiguar": {"nivel": "Media", "clase": "media", "promedio": 2.95, "n": 38},  # Brazil - Potiguar
    "brazil|potiguar 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.74, "n": 27},  # Brazil - Potiguar - 2
    "brazil|potiguar u20": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.92, "n": 37},  # Brazil - Potiguar - U20
    "brazil|rondoniense": {"nivel": "Baja", "clase": "baja", "promedio": 2.38, "n": 48},  # Brazil - Rondoniense
    "brazil|roraimense": {"nivel": "Alta", "clase": "alta", "promedio": 3.38, "n": 39},  # Brazil - Roraimense
    "brazil|sergipano": {"nivel": "Baja", "clase": "baja", "promedio": 2.22, "n": 55},  # Brazil - Sergipano
    "brazil|sergipano 2": {"nivel": "Media", "clase": "media", "promedio": 3.07, "n": 43},  # Brazil - Sergipano - 2
    "brazil|serie a": {"nivel": "Baja", "clase": "baja", "promedio": 2.65, "n": 441},  # Brazil - Serie A
    "brazil|serie b": {"nivel": "Baja", "clase": "baja", "promedio": 2.30, "n": 391},  # Brazil - Serie B
    "brazil|serie c": {"nivel": "Baja", "clase": "baja", "promedio": 2.14, "n": 226},  # Brazil - Serie C
    "brazil|serie d": {"nivel": "Baja", "clase": "baja", "promedio": 2.28, "n": 705},  # Brazil - Serie D
    "brazil|sul matogrossense": {"nivel": "Baja", "clase": "baja", "promedio": 2.65, "n": 55},  # Brazil - Sul-Matogrossense
    "brazil|sao paulo youth cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.77, "n": 255},  # Brazil - São Paulo Youth Cup
    "brazil|tocantinense": {"nivel": "Baja", "clase": "baja", "promedio": 2.35, "n": 34},  # Brazil - Tocantinense
    "bulgaria|cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.40, "n": 48},  # Bulgaria - Cup
    "bulgaria|first league": {"nivel": "Baja", "clase": "baja", "promedio": 2.29, "n": 293},  # Bulgaria - First League
    "bulgaria|second league": {"nivel": "Baja", "clase": "baja", "promedio": 2.51, "n": 272},  # Bulgaria - Second League
    "bulgaria|third league northeast": {"nivel": "Alta", "clase": "alta", "promedio": 3.54, "n": 269},  # Bulgaria - Third League - Northeast
    "bulgaria|third league northwest": {"nivel": "Media", "clase": "media", "promedio": 3.12, "n": 129},  # Bulgaria - Third League - Northwest
    "bulgaria|third league southeast": {"nivel": "Media", "clase": "media", "promedio": 3.11, "n": 342},  # Bulgaria - Third League - Southeast
    "bulgaria|third league southwest": {"nivel": "Baja", "clase": "baja", "promedio": 2.79, "n": 299},  # Bulgaria - Third League - Southwest
    "burkina faso|ligue 1": {"nivel": "Baja", "clase": "baja", "promedio": 1.74, "n": 240},  # Burkina-Faso - Ligue 1
    "burundi|ligue a": {"nivel": "Baja", "clase": "baja", "promedio": 2.61, "n": 240},  # Burundi - Ligue A
    "cambodia|c league": {"nivel": "Media", "clase": "media", "promedio": 3.19, "n": 160},  # Cambodia - C-League
    "cameroon|elite one": {"nivel": "Baja", "clase": "baja", "promedio": 2.56, "n": 186},  # Cameroon - Elite One
    "cameroon|elite two": {"nivel": "Baja", "clase": "baja", "promedio": 2.44, "n": 177},  # Cameroon - Elite Two
    "canada|canadian championship": {"nivel": "Alta", "clase": "alta", "promedio": 3.69, "n": 16},  # Canada - Canadian Championship
    "canada|canadian premier league": {"nivel": "Media", "clase": "media", "promedio": 2.94, "n": 114},  # Canada - Canadian Premier League
    "canada|canadian soccer league": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 5.86, "n": 21},  # Canada - Canadian Soccer League
    "canada|league 1 ontario": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.75, "n": 60},  # Canada - League 1 Ontario
    "canada|northern super league": {"nivel": "Media", "clase": "media", "promedio": 2.82, "n": 74},  # Canada - Northern Super League
    "canada|pacific coast soccer league": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.57, "n": 21},  # Canada - Pacific Coast Soccer League
    "chile|copa chile": {"nivel": "Media", "clase": "media", "promedio": 3.00, "n": 37},  # Chile - Copa Chile
    "chile|copa de la liga": {"nivel": "Media", "clase": "media", "promedio": 2.83, "n": 48},  # Chile - Copa De La Liga
    "chile|primera b": {"nivel": "Baja", "clase": "baja", "promedio": 2.55, "n": 266},  # Chile - Primera B
    "chile|primera division": {"nivel": "Baja", "clase": "baja", "promedio": 2.74, "n": 251},  # Chile - Primera División
    "chile|segunda division": {"nivel": "Baja", "clase": "baja", "promedio": 2.70, "n": 145},  # Chile - Segunda División
    "china|fa cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.68, "n": 47},  # China - FA Cup
    "china|league one": {"nivel": "Baja", "clase": "baja", "promedio": 2.52, "n": 231},  # China - League One
    "china|league two": {"nivel": "Baja", "clase": "baja", "promedio": 2.23, "n": 331},  # China - League Two
    "china|super league": {"nivel": "Media", "clase": "media", "promedio": 3.15, "n": 251},  # China - Super League
    "chinese taipei|taiwan football premier league": {"nivel": "Media", "clase": "media", "promedio": 2.86, "n": 84},  # Chinese-Taipei - Taiwan Football Premier League
    "colombia|copa colombia": {"nivel": "Baja", "clase": "baja", "promedio": 2.56, "n": 86},  # Colombia - Copa Colombia
    "colombia|liga femenina": {"nivel": "Baja", "clase": "baja", "promedio": 2.33, "n": 143},  # Colombia - Liga Femenina
    "colombia|primera a": {"nivel": "Baja", "clase": "baja", "promedio": 2.47, "n": 435},  # Colombia - Primera A
    "colombia|primera b": {"nivel": "Baja", "clase": "baja", "promedio": 2.25, "n": 302},  # Colombia - Primera B
    "congo dr|ligue 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.00, "n": 472},  # Congo-DR - Ligue 1
    "costa rica|copa costa rica": {"nivel": "Media", "clase": "media", "promedio": 3.03, "n": 37},  # Costa-Rica - Copa Costa Rica
    "costa rica|liga de ascenso": {"nivel": "Baja", "clase": "baja", "promedio": 2.74, "n": 250},  # Costa-Rica - Liga de Ascenso
    "costa rica|primera division": {"nivel": "Baja", "clase": "baja", "promedio": 2.47, "n": 192},  # Costa-Rica - Primera División
    "croatia|cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.02, "n": 47},  # Croatia - Cup
    "croatia|first nl": {"nivel": "Baja", "clase": "baja", "promedio": 2.34, "n": 198},  # Croatia - First NL
    "croatia|hnl": {"nivel": "Baja", "clase": "baja", "promedio": 2.66, "n": 180},  # Croatia - HNL
    "croatia|second nl": {"nivel": "Baja", "clase": "baja", "promedio": 2.77, "n": 239},  # Croatia - Second NL
    "croatia|third nl istok": {"nivel": "Baja", "clase": "baja", "promedio": 2.56, "n": 113},  # Croatia - Third NL - Istok
    "croatia|third nl jug": {"nivel": "Media", "clase": "media", "promedio": 2.88, "n": 240},  # Croatia - Third NL - Jug
    "croatia|third nl sjever": {"nivel": "Alta", "clase": "alta", "promedio": 3.49, "n": 120},  # Croatia - Third NL - Sjever
    "croatia|third nl sredite": {"nivel": "Media", "clase": "media", "promedio": 3.12, "n": 120},  # Croatia - Third NL - Sredite
    "croatia|third nl zapad": {"nivel": "Media", "clase": "media", "promedio": 2.99, "n": 120},  # Croatia - Third NL - Zapad
    "cyprus|1. division": {"nivel": "Baja", "clase": "baja", "promedio": 2.64, "n": 240},  # Cyprus - 1. Division
    "cyprus|2. division": {"nivel": "Baja", "clase": "baja", "promedio": 2.71, "n": 232},  # Cyprus - 2. Division
    "cyprus|3. division": {"nivel": "Baja", "clase": "baja", "promedio": 2.76, "n": 230},  # Cyprus - 3. Division
    "cyprus|cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.41, "n": 29},  # Cyprus - Cup
    "czech republic|1. liga u19": {"nivel": "Alta", "clase": "alta", "promedio": 3.59, "n": 240},  # Czech-Republic - 1. Liga U19
    "czech republic|1. liga women": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.10, "n": 80},  # Czech-Republic - 1. Liga Women
    "czech republic|3. liga cfl a": {"nivel": "Media", "clase": "media", "promedio": 3.19, "n": 272},  # Czech-Republic - 3. liga - CFL A
    "czech republic|3. liga cfl b": {"nivel": "Alta", "clase": "alta", "promedio": 3.35, "n": 272},  # Czech-Republic - 3. liga - CFL B
    "czech republic|3. liga msfl": {"nivel": "Media", "clase": "media", "promedio": 3.13, "n": 304},  # Czech-Republic - 3. liga - MSFL
    "czech republic|4. liga divizie a": {"nivel": "Alta", "clase": "alta", "promedio": 3.44, "n": 240},  # Czech-Republic - 4. liga - Divizie A
    "czech republic|4. liga divizie b": {"nivel": "Alta", "clase": "alta", "promedio": 3.57, "n": 240},  # Czech-Republic - 4. liga - Divizie B
    "czech republic|4. liga divizie c": {"nivel": "Alta", "clase": "alta", "promedio": 3.53, "n": 239},  # Czech-Republic - 4. liga - Divizie C
    "czech republic|4. liga divizie d": {"nivel": "Media", "clase": "media", "promedio": 3.17, "n": 240},  # Czech-Republic - 4. liga - Divizie D
    "czech republic|4. liga divizie e": {"nivel": "Media", "clase": "media", "promedio": 3.14, "n": 210},  # Czech-Republic - 4. liga - Divizie E
    "czech republic|4. liga divizie f": {"nivel": "Alta", "clase": "alta", "promedio": 3.38, "n": 240},  # Czech-Republic - 4. liga - Divizie F
    "czech republic|cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.66, "n": 152},  # Czech-Republic - Cup
    "czech republic|czech liga": {"nivel": "Baja", "clase": "baja", "promedio": 2.64, "n": 279},  # Czech-Republic - Czech Liga
    "czech republic|fnl": {"nivel": "Baja", "clase": "baja", "promedio": 2.68, "n": 240},  # Czech-Republic - FNL
    "czech republic|tipsport liga": {"nivel": "Alta", "clase": "alta", "promedio": 3.54, "n": 24},  # Czech-Republic - Tipsport Liga
    "denmark|1. division": {"nivel": "Media", "clase": "media", "promedio": 2.80, "n": 192},  # Denmark - 1. Division
    "denmark|2. division": {"nivel": "Baja", "clase": "baja", "promedio": 2.78, "n": 192},  # Denmark - 2. Division
    "denmark|3. division": {"nivel": "Media", "clase": "media", "promedio": 3.05, "n": 192},  # Denmark - 3. Division
    "denmark|dbu pokalen": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.10, "n": 110},  # Denmark - DBU Pokalen
    "denmark|denmark series group 1": {"nivel": "Alta", "clase": "alta", "promedio": 3.24, "n": 89},  # Denmark - Denmark Series - Group 1
    "denmark|denmark series group 2": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.71, "n": 85},  # Denmark - Denmark Series - Group 2
    "denmark|denmark series group 3": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.97, "n": 89},  # Denmark - Denmark Series - Group 3
    "denmark|denmark series group 4": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.73, "n": 83},  # Denmark - Denmark Series - Group 4
    "denmark|kvindeliga": {"nivel": "Media", "clase": "media", "promedio": 2.94, "n": 116},  # Denmark - Kvindeliga
    "denmark|superliga": {"nivel": "Media", "clase": "media", "promedio": 3.10, "n": 193},  # Denmark - Superliga
    "dominican republic|liga mayor": {"nivel": "Baja", "clase": "baja", "promedio": 2.66, "n": 135},  # Dominican-Republic - Liga Mayor
    "ecuador|copa ecuador": {"nivel": "Baja", "clase": "baja", "promedio": 2.44, "n": 63},  # Ecuador - Copa Ecuador
    "ecuador|liga pro": {"nivel": "Baja", "clase": "baja", "promedio": 2.39, "n": 312},  # Ecuador - Liga Pro
    "ecuador|liga pro serie b": {"nivel": "Baja", "clase": "baja", "promedio": 2.19, "n": 198},  # Ecuador - Liga Pro Serie B
    "egypt|cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.35, "n": 31},  # Egypt - Cup
    "egypt|league cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.26, "n": 77},  # Egypt - League Cup
    "egypt|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.02, "n": 322},  # Egypt - Premier League
    "egypt|second league": {"nivel": "Baja", "clase": "baja", "promedio": 1.96, "n": 307},  # Egypt - Second League
    "el salvador|copa presidente": {"nivel": "Baja", "clase": "baja", "promedio": 2.71, "n": 49},  # El-Salvador - Copa Presidente
    "el salvador|primera division": {"nivel": "Baja", "clase": "baja", "promedio": 2.66, "n": 290},  # El-Salvador - Primera Division
    "england|championship": {"nivel": "Baja", "clase": "baja", "promedio": 2.59, "n": 557},  # England - Championship
    "england|efl trophy": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.74, "n": 127},  # England - EFL Trophy
    "england|fa cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.30, "n": 869},  # England - FA Cup
    "england|fa trophy": {"nivel": "Media", "clase": "media", "promedio": 3.03, "n": 335},  # England - FA Trophy
    "england|fa women's cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.11, "n": 136},  # England - FA Women's Cup
    "england|fa wsl": {"nivel": "Media", "clase": "media", "promedio": 2.95, "n": 133},  # England - FA WSL
    "england|fa youth cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.06, "n": 31},  # England - FA Youth Cup
    "england|league cup": {"nivel": "Media", "clase": "media", "promedio": 2.80, "n": 93},  # England - League Cup
    "england|league one": {"nivel": "Baja", "clase": "baja", "promedio": 2.62, "n": 557},  # England - League One
    "england|league two": {"nivel": "Baja", "clase": "baja", "promedio": 2.57, "n": 557},  # England - League Two
    "england|national league": {"nivel": "Media", "clase": "media", "promedio": 2.92, "n": 556},  # England - National League
    "england|national league north": {"nivel": "Media", "clase": "media", "promedio": 3.06, "n": 557},  # England - National League - North
    "england|national league south": {"nivel": "Media", "clase": "media", "promedio": 2.86, "n": 557},  # England - National League - South
    "england|national league cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.28, "n": 71},  # England - National League Cup
    "england|non league div one isthmian north": {"nivel": "Media", "clase": "media", "promedio": 2.96, "n": 458},  # England - Non League Div One - Isthmian North
    "england|non league div one isthmian south central": {"nivel": "Alta", "clase": "alta", "promedio": 3.35, "n": 432},  # England - Non League Div One - Isthmian South Central
    "england|non league div one isthmian south east": {"nivel": "Alta", "clase": "alta", "promedio": 3.49, "n": 439},  # England - Non League Div One - Isthmian South East
    "england|non league div one northern east": {"nivel": "Media", "clase": "media", "promedio": 2.82, "n": 436},  # England - Non League Div One - Northern East
    "england|non league div one northern midlands": {"nivel": "Baja", "clase": "baja", "promedio": 2.78, "n": 449},  # England - Non League Div One - Northern Midlands
    "england|non league div one northern west": {"nivel": "Media", "clase": "media", "promedio": 3.05, "n": 460},  # England - Non League Div One - Northern West
    "england|non league div one southern central": {"nivel": "Alta", "clase": "alta", "promedio": 3.59, "n": 464},  # England - Non League Div One - Southern Central
    "england|non league div one southern south": {"nivel": "Media", "clase": "media", "promedio": 3.18, "n": 428},  # England - Non League Div One - Southern South
    "england|non league premier isthmian": {"nivel": "Alta", "clase": "alta", "promedio": 3.21, "n": 465},  # England - Non League Premier - Isthmian
    "england|non league premier northern": {"nivel": "Baja", "clase": "baja", "promedio": 2.58, "n": 423},  # England - Non League Premier - Northern
    "england|non league premier southern central": {"nivel": "Media", "clase": "media", "promedio": 2.98, "n": 465},  # England - Non League Premier - Southern Central
    "england|non league premier southern south": {"nivel": "Media", "clase": "media", "promedio": 3.17, "n": 465},  # England - Non League Premier - Southern South
    "england|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.75, "n": 380},  # England - Premier League
    "england|premier league 2 division one": {"nivel": "Alta", "clase": "alta", "promedio": 3.58, "n": 305},  # England - Premier League 2 Division One
    "england|premier league cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.70, "n": 111},  # England - Premier League Cup
    "england|professional development league": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.84, "n": 295},  # England - Professional Development League
    "england|u18 premier league north": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.18, "n": 176},  # England - U18 Premier League - North
    "england|u18 premier league south": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.12, "n": 211},  # England - U18 Premier League - South
    "england|women's championship": {"nivel": "Media", "clase": "media", "promedio": 3.00, "n": 132},  # England - Women's Championship
    "england|wsl cup": {"nivel": "Media", "clase": "media", "promedio": 3.17, "n": 40},  # England - WSL Cup
    "estonia|cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 6.15, "n": 67},  # Estonia - Cup
    "estonia|esiliiga a": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.82, "n": 179},  # Estonia - Esiliiga A
    "estonia|esiliiga b": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.46, "n": 182},  # Estonia - Esiliiga B
    "estonia|meistriliiga": {"nivel": "Media", "clase": "media", "promedio": 3.16, "n": 178},  # Estonia - Meistriliiga
    "eswatini|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.17, "n": 246},  # Eswatini - Premier League
    "ethiopia|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 1.79, "n": 357},  # Ethiopia - Premier League
    "faroe islands|1. deild": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.91, "n": 134},  # Faroe-Islands - 1. Deild
    "faroe islands|løgmanssteypid": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.12, "n": 17},  # Faroe-Islands - Løgmanssteypid
    "faroe islands|meistaradeildin": {"nivel": "Alta", "clase": "alta", "promedio": 3.30, "n": 135},  # Faroe-Islands - Meistaradeildin
    "fiji|national football league": {"nivel": "Alta", "clase": "alta", "promedio": 3.23, "n": 40},  # Fiji - National Football League
    "finland|kakkonen lohko a": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.91, "n": 90},  # Finland - Kakkonen - Lohko A
    "finland|kakkonen lohko b": {"nivel": "Alta", "clase": "alta", "promedio": 3.68, "n": 90},  # Finland - Kakkonen - Lohko B
    "finland|kakkonen lohko c": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.41, "n": 81},  # Finland - Kakkonen - Lohko C
    "finland|kakkonen play offs": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.72, "n": 87},  # Finland - Kakkonen - Play-offs
    "finland|kansallinen liiga": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.99, "n": 130},  # Finland - Kansallinen Liiga
    "finland|league cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.48, "n": 33},  # Finland - League Cup
    "finland|suomen cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.48, "n": 119},  # Finland - Suomen Cup
    "finland|veikkausliiga": {"nivel": "Media", "clase": "media", "promedio": 3.11, "n": 179},  # Finland - Veikkausliiga
    "finland|ykkonen": {"nivel": "Alta", "clase": "alta", "promedio": 3.47, "n": 168},  # Finland - Ykkönen
    "finland|ykkoscup": {"nivel": "Baja", "clase": "baja", "promedio": 2.57, "n": 23},  # Finland - Ykköscup
    "finland|ykkosliiga": {"nivel": "Media", "clase": "media", "promedio": 2.92, "n": 143},  # Finland - Ykkösliiga
    "france|coupe de france": {"nivel": "Media", "clase": "media", "promedio": 3.15, "n": 201},  # France - Coupe de France
    "france|feminine division 1": {"nivel": "Media", "clase": "media", "promedio": 3.04, "n": 131},  # France - Feminine Division 1
    "france|ligue 1": {"nivel": "Media", "clase": "media", "promedio": 2.83, "n": 309},  # France - Ligue 1
    "france|ligue 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.53, "n": 307},  # France - Ligue 2
    "france|national 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.42, "n": 271},  # France - National 1
    "france|national 2 group a": {"nivel": "Baja", "clase": "baja", "promedio": 2.60, "n": 240},  # France - National 2 - Group A
    "france|national 2 group b": {"nivel": "Baja", "clase": "baja", "promedio": 2.49, "n": 240},  # France - National 2 - Group B
    "france|national 2 group c": {"nivel": "Baja", "clase": "baja", "promedio": 2.62, "n": 240},  # France - National 2 - Group C
    "france|national 3 group a": {"nivel": "Baja", "clase": "baja", "promedio": 2.67, "n": 182},  # France - National 3 - Group A
    "france|national 3 group b": {"nivel": "Baja", "clase": "baja", "promedio": 2.70, "n": 178},  # France - National 3 - Group B
    "france|national 3 group c": {"nivel": "Baja", "clase": "baja", "promedio": 2.50, "n": 178},  # France - National 3 - Group C
    "france|national 3 group d": {"nivel": "Baja", "clase": "baja", "promedio": 2.72, "n": 178},  # France - National 3 - Group D
    "france|national 3 group e": {"nivel": "Baja", "clase": "baja", "promedio": 2.60, "n": 178},  # France - National 3 - Group E
    "france|national 3 group f": {"nivel": "Baja", "clase": "baja", "promedio": 2.77, "n": 182},  # France - National 3 - Group F
    "france|national 3 group g": {"nivel": "Media", "clase": "media", "promedio": 2.84, "n": 180},  # France - National 3 - Group G
    "france|national 3 group h": {"nivel": "Media", "clase": "media", "promedio": 2.97, "n": 179},  # France - National 3 - Group H
    "gabon|championnat d1": {"nivel": "Baja", "clase": "baja", "promedio": 2.51, "n": 149},  # Gabon - Championnat D1
    "gambia|gfa league": {"nivel": "Baja", "clase": "baja", "promedio": 1.87, "n": 253},  # Gambia - GFA League
    "georgia|david kipiani cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.29, "n": 35},  # Georgia - David Kipiani Cup
    "georgia|erovnuli liga": {"nivel": "Baja", "clase": "baja", "promedio": 2.77, "n": 180},  # Georgia - Erovnuli Liga
    "georgia|erovnuli liga 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.56, "n": 192},  # Georgia - Erovnuli Liga 2
    "georgia|liga 3": {"nivel": "Media", "clase": "media", "promedio": 2.99, "n": 249},  # Georgia - Liga 3
    "germany|2. bundesliga": {"nivel": "Media", "clase": "media", "promedio": 2.92, "n": 308},  # Germany - 2. Bundesliga
    "germany|2. frauen bundesliga": {"nivel": "Alta", "clase": "alta", "promedio": 3.54, "n": 183},  # Germany - 2. Frauen Bundesliga
    "germany|3. liga": {"nivel": "Alta", "clase": "alta", "promedio": 3.21, "n": 380},  # Germany - 3. Liga
    "germany|bundesliga": {"nivel": "Alta", "clase": "alta", "promedio": 3.22, "n": 308},  # Germany - Bundesliga
    "germany|dfb junioren pokal": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.19, "n": 63},  # Germany - DFB Junioren Pokal
    "germany|dfb pokal": {"nivel": "Media", "clase": "media", "promedio": 3.17, "n": 63},  # Germany - DFB Pokal
    "germany|dfb pokal women": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.21, "n": 47},  # Germany - DFB Pokal - Women
    "germany|frauen bundesliga": {"nivel": "Alta", "clase": "alta", "promedio": 3.45, "n": 182},  # Germany - Frauen Bundesliga
    "germany|oberliga baden wurttemberg": {"nivel": "Alta", "clase": "alta", "promedio": 3.46, "n": 306},  # Germany - Oberliga - Baden-Württemberg
    "germany|oberliga bayern nord": {"nivel": "Alta", "clase": "alta", "promedio": 3.29, "n": 272},  # Germany - Oberliga - Bayern Nord
    "germany|oberliga bayern sud": {"nivel": "Media", "clase": "media", "promedio": 3.09, "n": 271},  # Germany - Oberliga - Bayern Süd
    "germany|oberliga bremen": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.45, "n": 240},  # Germany - Oberliga - Bremen
    "germany|oberliga hamburg": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.44, "n": 304},  # Germany - Oberliga - Hamburg
    "germany|oberliga hessen": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.74, "n": 309},  # Germany - Oberliga - Hessen
    "germany|oberliga mittelrhein": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.06, "n": 232},  # Germany - Oberliga - Mittelrhein
    "germany|oberliga niederrhein": {"nivel": "Alta", "clase": "alta", "promedio": 3.46, "n": 306},  # Germany - Oberliga - Niederrhein
    "germany|oberliga niedersachsen": {"nivel": "Alta", "clase": "alta", "promedio": 3.55, "n": 240},  # Germany - Oberliga - Niedersachsen
    "germany|oberliga nordost nord": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.77, "n": 240},  # Germany - Oberliga - Nordost-Nord
    "germany|oberliga nordost sud": {"nivel": "Media", "clase": "media", "promedio": 3.19, "n": 240},  # Germany - Oberliga - Nordost-Süd
    "germany|oberliga rheinland pfalz / saar": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.80, "n": 306},  # Germany - Oberliga - Rheinland-Pfalz / Saar
    "germany|oberliga schleswig holstein": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.81, "n": 239},  # Germany - Oberliga - Schleswig-Holstein
    "germany|oberliga westfalen": {"nivel": "Alta", "clase": "alta", "promedio": 3.30, "n": 340},  # Germany - Oberliga - Westfalen
    "germany|regionalliga bayern": {"nivel": "Media", "clase": "media", "promedio": 2.98, "n": 310},  # Germany - Regionalliga - Bayern
    "germany|regionalliga nord": {"nivel": "Alta", "clase": "alta", "promedio": 3.59, "n": 307},  # Germany - Regionalliga - Nord
    "germany|regionalliga nordost": {"nivel": "Media", "clase": "media", "promedio": 2.99, "n": 306},  # Germany - Regionalliga - Nordost
    "germany|regionalliga sudwest": {"nivel": "Alta", "clase": "alta", "promedio": 3.39, "n": 306},  # Germany - Regionalliga - SudWest
    "germany|regionalliga west": {"nivel": "Media", "clase": "media", "promedio": 3.08, "n": 306},  # Germany - Regionalliga - West
    "germany|u19 bundesliga": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.04, "n": 879},  # Germany - U19 Bundesliga
    "ghana|cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.47, "n": 15},  # Ghana - Cup
    "ghana|division one league": {"nivel": "Baja", "clase": "baja", "promedio": 2.39, "n": 705},  # Ghana - Division One League
    "ghana|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.02, "n": 299},  # Ghana - Premier League
    "gibraltar|premier division": {"nivel": "Alta", "clase": "alta", "promedio": 3.53, "n": 147},  # Gibraltar - Premier Division
    "greece|cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.69, "n": 64},  # Greece - Cup
    "greece|gamma ethniki group 1": {"nivel": "Media", "clase": "media", "promedio": 2.89, "n": 162},  # Greece - Gamma Ethniki - Group 1
    "greece|gamma ethniki group 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.62, "n": 162},  # Greece - Gamma Ethniki - Group 2
    "greece|gamma ethniki group 3": {"nivel": "Baja", "clase": "baja", "promedio": 2.37, "n": 179},  # Greece - Gamma Ethniki - Group 3
    "greece|gamma ethniki group 4": {"nivel": "Baja", "clase": "baja", "promedio": 2.69, "n": 162},  # Greece - Gamma Ethniki - Group 4
    "greece|gamma ethniki group 5": {"nivel": "Baja", "clase": "baja", "promedio": 2.22, "n": 144},  # Greece - Gamma Ethniki - Group 5
    "greece|gamma ethniki group 6": {"nivel": "Baja", "clase": "baja", "promedio": 2.33, "n": 162},  # Greece - Gamma Ethniki - Group 6
    "greece|gamma ethniki promotion group": {"nivel": "Baja", "clase": "baja", "promedio": 2.43, "n": 23},  # Greece - Gamma Ethniki - Promotion Group
    "greece|super league 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.57, "n": 236},  # Greece - Super League 1
    "greece|super league 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.29, "n": 265},  # Greece - Super League 2
    "grenada|premier division": {"nivel": "Alta", "clase": "alta", "promedio": 3.46, "n": 76},  # Grenada - Premier Division
    "guatemala|liga nacional": {"nivel": "Baja", "clase": "baja", "promedio": 2.42, "n": 291},  # Guatemala - Liga Nacional
    "guinea|ligue 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.24, "n": 209},  # Guinea - Ligue 1
    "honduras|liga nacional": {"nivel": "Media", "clase": "media", "promedio": 2.88, "n": 247},  # Honduras - Liga Nacional
    "hong kong|hkfa 1st division": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.87, "n": 90},  # Hong-Kong - HKFA 1st Division
    "hong kong|premier league": {"nivel": "Alta", "clase": "alta", "promedio": 3.29, "n": 110},  # Hong-Kong - Premier League
    "hungary|magyar kupa": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.11, "n": 171},  # Hungary - Magyar Kupa
    "hungary|nb i": {"nivel": "Media", "clase": "media", "promedio": 3.00, "n": 198},  # Hungary - NB I
    "hungary|nb ii": {"nivel": "Baja", "clase": "baja", "promedio": 2.51, "n": 240},  # Hungary - NB II
    "hungary|nb iii northeast": {"nivel": "Alta", "clase": "alta", "promedio": 3.32, "n": 240},  # Hungary - NB III - Northeast
    "hungary|nb iii northwest": {"nivel": "Alta", "clase": "alta", "promedio": 3.33, "n": 240},  # Hungary - NB III - Northwest
    "hungary|nb iii southeast": {"nivel": "Alta", "clase": "alta", "promedio": 3.31, "n": 239},  # Hungary - NB III - Southeast
    "hungary|nb iii southwest": {"nivel": "Alta", "clase": "alta", "promedio": 3.32, "n": 240},  # Hungary - NB III - Southwest
    "iceland|1. deild": {"nivel": "Alta", "clase": "alta", "promedio": 3.56, "n": 142},  # Iceland - 1. Deild
    "iceland|2. deild": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.93, "n": 132},  # Iceland - 2. Deild
    "iceland|cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.55, "n": 76},  # Iceland - Cup
    "iceland|fotbolti.net cup a": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.60, "n": 15},  # Iceland - Fotbolti.net Cup A
    "iceland|league cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.04, "n": 57},  # Iceland - League Cup
    "iceland|reykjavik cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.24, "n": 17},  # Iceland - Reykjavik Cup
    "iceland|urvalsdeild": {"nivel": "Alta", "clase": "alta", "promedio": 3.68, "n": 158},  # Iceland - Úrvalsdeild
    "iceland|urvalsdeild women": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.08, "n": 65},  # Iceland - Úrvalsdeild Women
    "india|aiff super cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.48, "n": 27},  # India - AIFF Super Cup
    "india|calcutta premier division": {"nivel": "Baja", "clase": "baja", "promedio": 2.68, "n": 152},  # India - Calcutta Premier Division
    "india|i league": {"nivel": "Media", "clase": "media", "promedio": 3.05, "n": 66},  # India - I-League
    "india|i league 2nd division": {"nivel": "Baja", "clase": "baja", "promedio": 2.64, "n": 36},  # India - I-League - 2nd Division
    "india|indian super league": {"nivel": "Baja", "clase": "baja", "promedio": 2.43, "n": 91},  # India - Indian Super League
    "india|santosh trophy": {"nivel": "Media", "clase": "media", "promedio": 2.84, "n": 88},  # India - Santosh Trophy
    "indonesia|liga 1": {"nivel": "Media", "clase": "media", "promedio": 2.80, "n": 306},  # Indonesia - Liga 1
    "indonesia|liga 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.79, "n": 273},  # Indonesia - Liga 2
    "iran|azadegan league": {"nivel": "Baja", "clase": "baja", "promedio": 1.50, "n": 258},  # Iran - Azadegan League
    "iran|hazfi cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.04, "n": 23},  # Iran - Hazfi Cup
    "iran|persian gulf pro league": {"nivel": "Baja", "clase": "baja", "promedio": 1.80, "n": 176},  # Iran - Persian Gulf Pro League
    "iraq|iraqi league": {"nivel": "Baja", "clase": "baja", "promedio": 2.49, "n": 406},  # Iraq - Iraqi League
    "ireland|fai cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.72, "n": 43},  # Ireland - FAI Cup
    "ireland|first division": {"nivel": "Baja", "clase": "baja", "promedio": 2.74, "n": 190},  # Ireland - First Division
    "ireland|premier division": {"nivel": "Baja", "clase": "baja", "promedio": 2.57, "n": 183},  # Ireland - Premier Division
    "israel|liga alef": {"nivel": "Media", "clase": "media", "promedio": 2.80, "n": 348},  # Israel - Liga Alef
    "israel|liga leumit": {"nivel": "Baja", "clase": "baja", "promedio": 2.72, "n": 296},  # Israel - Liga Leumit
    "israel|ligat ha'al": {"nivel": "Media", "clase": "media", "promedio": 2.97, "n": 239},  # Israel - Ligat Ha'al
    "israel|state cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.31, "n": 61},  # Israel - State Cup
    "israel|toto cup ligat al": {"nivel": "Media", "clase": "media", "promedio": 2.86, "n": 29},  # Israel - Toto Cup Ligat Al
    "italy|campionato primavera 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.75, "n": 386},  # Italy - Campionato Primavera - 1
    "italy|campionato primavera 2": {"nivel": "Media", "clase": "media", "promedio": 3.05, "n": 490},  # Italy - Campionato Primavera - 2
    "italy|coppa italia": {"nivel": "Baja", "clase": "baja", "promedio": 2.47, "n": 45},  # Italy - Coppa Italia
    "italy|coppa italia primavera": {"nivel": "Alta", "clase": "alta", "promedio": 3.25, "n": 51},  # Italy - Coppa Italia Primavera
    "italy|coppa italia serie c": {"nivel": "Baja", "clase": "baja", "promedio": 2.40, "n": 62},  # Italy - Coppa Italia Serie C
    "italy|coppa italia serie d": {"nivel": "Baja", "clase": "baja", "promedio": 2.36, "n": 166},  # Italy - Coppa Italia Serie D
    "italy|coppa italia women": {"nivel": "Media", "clase": "media", "promedio": 3.16, "n": 31},  # Italy - Coppa Italia Women
    "italy|serie a": {"nivel": "Baja", "clase": "baja", "promedio": 2.43, "n": 380},  # Italy - Serie A
    "italy|serie a cup women": {"nivel": "Media", "clase": "media", "promedio": 2.90, "n": 21},  # Italy - Serie A Cup Women
    "italy|serie a women": {"nivel": "Baja", "clase": "baja", "promedio": 2.61, "n": 132},  # Italy - Serie A Women
    "italy|serie b": {"nivel": "Baja", "clase": "baja", "promedio": 2.55, "n": 390},  # Italy - Serie B
    "italy|serie c girone a": {"nivel": "Baja", "clase": "baja", "promedio": 2.34, "n": 380},  # Italy - Serie C - Girone A
    "italy|serie c girone b": {"nivel": "Baja", "clase": "baja", "promedio": 2.25, "n": 357},  # Italy - Serie C - Girone B
    "italy|serie c girone c": {"nivel": "Baja", "clase": "baja", "promedio": 2.49, "n": 380},  # Italy - Serie C - Girone C
    "italy|serie c promotion play offs": {"nivel": "Baja", "clase": "baja", "promedio": 2.46, "n": 39},  # Italy - Serie C - Promotion - Play-offs
    "italy|serie d girone a": {"nivel": "Baja", "clase": "baja", "promedio": 2.47, "n": 310},  # Italy - Serie D - Girone A
    "italy|serie d girone b": {"nivel": "Baja", "clase": "baja", "promedio": 2.51, "n": 310},  # Italy - Serie D - Girone B
    "italy|serie d girone c": {"nivel": "Baja", "clase": "baja", "promedio": 2.32, "n": 312},  # Italy - Serie D - Girone C
    "italy|serie d girone d": {"nivel": "Baja", "clase": "baja", "promedio": 2.35, "n": 311},  # Italy - Serie D - Girone D
    "italy|serie d girone e": {"nivel": "Baja", "clase": "baja", "promedio": 2.28, "n": 311},  # Italy - Serie D - Girone E
    "italy|serie d girone f": {"nivel": "Baja", "clase": "baja", "promedio": 2.53, "n": 310},  # Italy - Serie D - Girone F
    "italy|serie d girone g": {"nivel": "Baja", "clase": "baja", "promedio": 2.68, "n": 311},  # Italy - Serie D - Girone G
    "italy|serie d girone h": {"nivel": "Baja", "clase": "baja", "promedio": 2.27, "n": 311},  # Italy - Serie D - Girone H
    "italy|serie d girone i": {"nivel": "Baja", "clase": "baja", "promedio": 2.35, "n": 311},  # Italy - Serie D - Girone I
    "ivory coast|ligue 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.00, "n": 240},  # Ivory-Coast - Ligue 1
    "jamaica|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.63, "n": 283},  # Jamaica - Premier League
    "japan|emperor cup": {"nivel": "Media", "clase": "media", "promedio": 3.09, "n": 34},  # Japan - Emperor Cup
    "japan|j1 league": {"nivel": "Baja", "clase": "baja", "promedio": 2.60, "n": 382},  # Japan - J1 League
    "japan|j2 league": {"nivel": "Baja", "clase": "baja", "promedio": 2.49, "n": 193},  # Japan - J2 League
    "japan|j2/j3 league": {"nivel": "Baja", "clase": "baja", "promedio": 2.56, "n": 400},  # Japan - J2/J3 League
    "japan|j3 league": {"nivel": "Baja", "clase": "baja", "promedio": 2.73, "n": 225},  # Japan - J3 League
    "japan|japan football league": {"nivel": "Baja", "clase": "baja", "promedio": 2.62, "n": 144},  # Japan - Japan Football League
    "japan|we league": {"nivel": "Baja", "clase": "baja", "promedio": 2.57, "n": 132},  # Japan - WE League
    "jordan|cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.48, "n": 31},  # Jordan - Cup
    "jordan|league": {"nivel": "Baja", "clase": "baja", "promedio": 2.76, "n": 135},  # Jordan - League
    "jordan|shield cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.09, "n": 45},  # Jordan - Shield Cup
    "kazakhstan|1. division": {"nivel": "Alta", "clase": "alta", "promedio": 3.64, "n": 179},  # Kazakhstan - 1. Division
    "kazakhstan|cup": {"nivel": "Media", "clase": "media", "promedio": 3.09, "n": 32},  # Kazakhstan - Cup
    "kazakhstan|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.55, "n": 202},  # Kazakhstan - Premier League
    "kenya|fkf premier league": {"nivel": "Baja", "clase": "baja", "promedio": 1.99, "n": 316},  # Kenya - FKF Premier League
    "kenya|shield cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.11, "n": 18},  # Kenya - Shield Cup
    "kenya|super league": {"nivel": "Baja", "clase": "baja", "promedio": 2.10, "n": 383},  # Kenya - Super League
    "kosovo|cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.76, "n": 33},  # Kosovo - Cup
    "kosovo|liga e pare": {"nivel": "Media", "clase": "media", "promedio": 2.81, "n": 305},  # Kosovo - Liga E Pare
    "kosovo|superliga": {"nivel": "Baja", "clase": "baja", "promedio": 2.66, "n": 181},  # Kosovo - Superliga
    "kuwait|crown prince cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.60, "n": 15},  # Kuwait - Crown Prince Cup
    "kuwait|division 1": {"nivel": "Media", "clase": "media", "promedio": 3.06, "n": 52},  # Kuwait - Division 1
    "kuwait|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.55, "n": 93},  # Kuwait - Premier League
    "kyrgyzstan|premier league": {"nivel": "Media", "clase": "media", "promedio": 2.89, "n": 192},  # Kyrgyzstan - Premier League
    "laos|lao league": {"nivel": "Alta", "clase": "alta", "promedio": 3.59, "n": 90},  # Laos - Lao League
    "latvia|1. liga": {"nivel": "Alta", "clase": "alta", "promedio": 3.39, "n": 181},  # Latvia - 1. Liga
    "latvia|cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.79, "n": 33},  # Latvia - Cup
    "latvia|virsliga": {"nivel": "Media", "clase": "media", "promedio": 2.99, "n": 184},  # Latvia - Virsliga
    "lebanon|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.56, "n": 138},  # Lebanon - Premier League
    "lesotho|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.28, "n": 240},  # Lesotho - Premier League
    "liberia|lfa first division": {"nivel": "Baja", "clase": "baja", "promedio": 2.79, "n": 201},  # Liberia - LFA First Division
    "libya|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.36, "n": 359},  # Libya - Premier League
    "liechtenstein|cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 5.89, "n": 18},  # Liechtenstein - Cup
    "lithuania|1 lyga": {"nivel": "Media", "clase": "media", "promedio": 3.00, "n": 245},  # Lithuania - 1 Lyga
    "lithuania|a lyga": {"nivel": "Baja", "clase": "baja", "promedio": 2.67, "n": 193},  # Lithuania - A Lyga
    "lithuania|cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.27, "n": 55},  # Lithuania - Cup
    "luxembourg|cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.24, "n": 63},  # Luxembourg - Cup
    "luxembourg|national division": {"nivel": "Media", "clase": "media", "promedio": 2.84, "n": 242},  # Luxembourg - National Division
    "macao|primeira divisao": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.95, "n": 88},  # Macao - Primeira Divisão
    "macedonia|cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.00, "n": 31},  # Macedonia - Cup
    "macedonia|first league": {"nivel": "Media", "clase": "media", "promedio": 3.08, "n": 199},  # Macedonia - First League
    "macedonia|second league": {"nivel": "Alta", "clase": "alta", "promedio": 3.29, "n": 243},  # Macedonia - Second League
    "malawi|super league": {"nivel": "Baja", "clase": "baja", "promedio": 2.15, "n": 225},  # Malawi - Super League
    "malaysia|fa cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.03, "n": 29},  # Malaysia - FA Cup
    "malaysia|malaysia cup": {"nivel": "Media", "clase": "media", "promedio": 3.03, "n": 29},  # Malaysia - Malaysia Cup
    "malaysia|super league": {"nivel": "Alta", "clase": "alta", "promedio": 3.29, "n": 156},  # Malaysia - Super League
    "mali|premiere division": {"nivel": "Baja", "clase": "baja", "promedio": 1.95, "n": 182},  # Mali - Première Division
    "malta|challenge league": {"nivel": "Alta", "clase": "alta", "promedio": 3.31, "n": 176},  # Malta - Challenge League
    "malta|fa trophy": {"nivel": "Media", "clase": "media", "promedio": 3.05, "n": 39},  # Malta - FA Trophy
    "malta|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.51, "n": 199},  # Malta - Premier League
    "mauritania|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.46, "n": 182},  # Mauritania - Premier League
    "mexico|liga de expansion mx": {"nivel": "Media", "clase": "media", "promedio": 2.84, "n": 240},  # Mexico - Liga de Expansión MX
    "mexico|liga mx": {"nivel": "Media", "clase": "media", "promedio": 2.91, "n": 337},  # Mexico - Liga MX
    "mexico|liga mx femenil": {"nivel": "Alta", "clase": "alta", "promedio": 3.37, "n": 334},  # Mexico - Liga MX Femenil
    "mexico|liga mx u21": {"nivel": "Baja", "clase": "baja", "promedio": 2.63, "n": 334},  # Mexico - Liga MX U21
    "mexico|liga premier serie a": {"nivel": "Media", "clase": "media", "promedio": 2.83, "n": 550},  # Mexico - Liga Premier Serie A
    "mexico|liga premier serie b": {"nivel": "Baja", "clase": "baja", "promedio": 2.75, "n": 102},  # Mexico - Liga Premier Serie B
    "moldova|cupa": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.07, "n": 29},  # Moldova - Cupa
    "moldova|liga 1": {"nivel": "Alta", "clase": "alta", "promedio": 3.69, "n": 118},  # Moldova - Liga 1
    "moldova|super liga": {"nivel": "Media", "clase": "media", "promedio": 2.97, "n": 153},  # Moldova - Super Liga
    "mongolia|premier league": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 5.21, "n": 112},  # Mongolia - Premier League
    "montenegro|cup": {"nivel": "Media", "clase": "media", "promedio": 2.88, "n": 17},  # Montenegro - Cup
    "montenegro|first league": {"nivel": "Baja", "clase": "baja", "promedio": 2.38, "n": 184},  # Montenegro - First League
    "montenegro|second league": {"nivel": "Baja", "clase": "baja", "promedio": 2.55, "n": 184},  # Montenegro - Second League
    "morocco|botola 2": {"nivel": "Baja", "clase": "baja", "promedio": 1.91, "n": 216},  # Morocco - Botola 2
    "morocco|botola pro": {"nivel": "Baja", "clase": "baja", "promedio": 2.12, "n": 192},  # Morocco - Botola Pro
    "morocco|cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.61, "n": 18},  # Morocco - Cup
    "myanmar|national league": {"nivel": "Alta", "clase": "alta", "promedio": 3.55, "n": 132},  # Myanmar - National League
    "netherlands|derde divisie relegation round": {"nivel": "Media", "clase": "media", "promedio": 2.92, "n": 24},  # Netherlands - Derde Divisie - Relegation Round
    "netherlands|derde divisie saturday": {"nivel": "Alta", "clase": "alta", "promedio": 3.32, "n": 306},  # Netherlands - Derde Divisie - Saturday
    "netherlands|derde divisie sunday": {"nivel": "Alta", "clase": "alta", "promedio": 3.31, "n": 306},  # Netherlands - Derde Divisie - Sunday
    "netherlands|eerste divisie": {"nivel": "Media", "clase": "media", "promedio": 3.18, "n": 392},  # Netherlands - Eerste Divisie
    "netherlands|eredivisie": {"nivel": "Media", "clase": "media", "promedio": 3.17, "n": 309},  # Netherlands - Eredivisie
    "netherlands|eredivisie women": {"nivel": "Alta", "clase": "alta", "promedio": 3.36, "n": 132},  # Netherlands - Eredivisie Women
    "netherlands|knvb beker": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.92, "n": 109},  # Netherlands - KNVB Beker
    "netherlands|tweede divisie": {"nivel": "Alta", "clase": "alta", "promedio": 3.31, "n": 322},  # Netherlands - Tweede Divisie
    "netherlands|u19 divisie 1": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.24, "n": 112},  # Netherlands - U19 Divisie 1
    "netherlands|u21 divisie 1": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.76, "n": 113},  # Netherlands - U21 Divisie 1
    "new zealand|chatham cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.25, "n": 16},  # New-Zealand - Chatham Cup
    "new zealand|national league central": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.47, "n": 40},  # New-Zealand - National League - Central
    "new zealand|national league national": {"nivel": "Alta", "clase": "alta", "promedio": 3.44, "n": 55},  # New-Zealand - National League - National
    "new zealand|national league northern": {"nivel": "Media", "clase": "media", "promedio": 3.13, "n": 54},  # New-Zealand - National League - Northern
    "new zealand|national league southern": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.18, "n": 45},  # New-Zealand - National League - Southern
    "nicaragua|primera division": {"nivel": "Media", "clase": "media", "promedio": 2.94, "n": 198},  # Nicaragua - Primera Division
    "nigeria|federation cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.48, "n": 27},  # Nigeria - Federation Cup
    "nigeria|npfl": {"nivel": "Baja", "clase": "baja", "promedio": 2.03, "n": 379},  # Nigeria - NPFL
    "northern ireland|championship": {"nivel": "Media", "clase": "media", "promedio": 2.92, "n": 228},  # Northern-Ireland - Championship
    "northern ireland|irish cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.77, "n": 39},  # Northern-Ireland - Irish Cup
    "northern ireland|league cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.78, "n": 37},  # Northern-Ireland - League Cup
    "northern ireland|premier intermediate league": {"nivel": "Alta", "clase": "alta", "promedio": 3.56, "n": 172},  # Northern-Ireland - Premier Intermediate League
    "northern ireland|premiership": {"nivel": "Media", "clase": "media", "promedio": 2.94, "n": 233},  # Northern-Ireland - Premiership
    "northern ireland|premiership women": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.22, "n": 67},  # Northern-Ireland - Premiership Women
    "norway|1. division": {"nivel": "Alta", "clase": "alta", "promedio": 3.42, "n": 256},  # Norway - 1. Division
    "norway|1. division women": {"nivel": "Alta", "clase": "alta", "promedio": 3.45, "n": 128},  # Norway - 1. Division Women
    "norway|2. division group 1": {"nivel": "Media", "clase": "media", "promedio": 3.12, "n": 182},  # Norway - 2. Division - Group 1
    "norway|2. division group 2": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.77, "n": 181},  # Norway - 2. Division - Group 2
    "norway|3. division girone 1": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.57, "n": 182},  # Norway - 3. Division - Girone 1
    "norway|3. division girone 2": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.09, "n": 184},  # Norway - 3. Division - Girone 2
    "norway|3. division girone 3": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.19, "n": 181},  # Norway - 3. Division - Girone 3
    "norway|3. division girone 4": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.30, "n": 182},  # Norway - 3. Division - Girone 4
    "norway|3. division girone 5": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.30, "n": 182},  # Norway - 3. Division - Girone 5
    "norway|3. division girone 6": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.12, "n": 182},  # Norway - 3. Division - Girone 6
    "norway|eliteserien": {"nivel": "Media", "clase": "media", "promedio": 3.13, "n": 252},  # Norway - Eliteserien
    "norway|nasjonal u19 champions league": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.95, "n": 112},  # Norway - Nasjonal U19 Champions League
    "norway|nm cupen": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.00, "n": 86},  # Norway - NM Cupen
    "norway|obos supercup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.24, "n": 25},  # Norway - Obos Supercup
    "norway|toppserien": {"nivel": "Alta", "clase": "alta", "promedio": 3.36, "n": 135},  # Norway - Toppserien
    "oman|fa cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.78, "n": 45},  # Oman - FA Cup
    "oman|professional league": {"nivel": "Baja", "clase": "baja", "promedio": 2.50, "n": 182},  # Oman - Professional League
    "oman|sultan cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.37, "n": 27},  # Oman - Sultan Cup
    "panama|liga panamena de futbol": {"nivel": "Baja", "clase": "baja", "promedio": 2.59, "n": 205},  # Panama - Liga Panameña de Fútbol
    "paraguay|copa paraguay": {"nivel": "Media", "clase": "media", "promedio": 2.88, "n": 59},  # Paraguay - Copa Paraguay
    "paraguay|division intermedia": {"nivel": "Baja", "clase": "baja", "promedio": 2.54, "n": 224},  # Paraguay - Division Intermedia
    "paraguay|division profesional apertura": {"nivel": "Baja", "clase": "baja", "promedio": 2.44, "n": 131},  # Paraguay - Division Profesional - Apertura
    "paraguay|division profesional clausura": {"nivel": "Baja", "clase": "baja", "promedio": 2.58, "n": 132},  # Paraguay - Division Profesional - Clausura
    "peru|copa peru": {"nivel": "Media", "clase": "media", "promedio": 2.97, "n": 122},  # Peru - Copa Perú
    "peru|liga women": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.76, "n": 55},  # Peru - Liga Women
    "peru|primera division": {"nivel": "Baja", "clase": "baja", "promedio": 2.54, "n": 353},  # Peru - Primera División
    "peru|segunda division": {"nivel": "Baja", "clase": "baja", "promedio": 2.32, "n": 161},  # Peru - Segunda División
    "philippines|pfl": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.80, "n": 135},  # Philippines - PFL
    "poland|central youth league": {"nivel": "Alta", "clase": "alta", "promedio": 3.56, "n": 240},  # Poland - Central Youth League
    "poland|cup": {"nivel": "Media", "clase": "media", "promedio": 2.91, "n": 67},  # Poland - Cup
    "poland|ekstraklasa": {"nivel": "Baja", "clase": "baja", "promedio": 2.74, "n": 306},  # Poland - Ekstraklasa
    "poland|ekstraliga women": {"nivel": "Alta", "clase": "alta", "promedio": 3.39, "n": 132},  # Poland - Ekstraliga Women
    "poland|i liga": {"nivel": "Media", "clase": "media", "promedio": 2.98, "n": 308},  # Poland - I Liga
    "poland|ii liga east": {"nivel": "Media", "clase": "media", "promedio": 2.95, "n": 308},  # Poland - II Liga - East
    "poland|iii liga group 1": {"nivel": "Alta", "clase": "alta", "promedio": 3.33, "n": 306},  # Poland - III Liga - Group 1
    "poland|iii liga group 2": {"nivel": "Media", "clase": "media", "promedio": 3.03, "n": 306},  # Poland - III Liga - Group 2
    "poland|iii liga group 3": {"nivel": "Alta", "clase": "alta", "promedio": 3.22, "n": 290},  # Poland - III Liga - Group 3
    "poland|iii liga group 4": {"nivel": "Media", "clase": "media", "promedio": 3.13, "n": 305},  # Poland - III Liga - Group 4
    "portugal|1a divisao women": {"nivel": "Baja", "clase": "baja", "promedio": 2.68, "n": 94},  # Portugal - 1a Divisão - Women
    "portugal|campeonato de portugal prio group a": {"nivel": "Baja", "clase": "baja", "promedio": 2.37, "n": 182},  # Portugal - Campeonato de Portugal Prio - Group A
    "portugal|campeonato de portugal prio group b": {"nivel": "Baja", "clase": "baja", "promedio": 2.28, "n": 182},  # Portugal - Campeonato de Portugal Prio - Group B
    "portugal|campeonato de portugal prio group c": {"nivel": "Baja", "clase": "baja", "promedio": 2.46, "n": 182},  # Portugal - Campeonato de Portugal Prio - Group C
    "portugal|campeonato de portugal prio group d": {"nivel": "Baja", "clase": "baja", "promedio": 2.40, "n": 182},  # Portugal - Campeonato de Portugal Prio - Group D
    "portugal|campeonato de portugal prio promotion round": {"nivel": "Baja", "clase": "baja", "promedio": 2.36, "n": 25},  # Portugal - Campeonato de Portugal Prio - Promotion Round
    "portugal|juniores u19": {"nivel": "Media", "clase": "media", "promedio": 2.91, "n": 296},  # Portugal - Júniores U19
    "portugal|liga 3": {"nivel": "Baja", "clase": "baja", "promedio": 2.23, "n": 296},  # Portugal - Liga 3
    "portugal|liga revelacao u23": {"nivel": "Media", "clase": "media", "promedio": 2.85, "n": 256},  # Portugal - Liga Revelação U23
    "portugal|primeira liga": {"nivel": "Baja", "clase": "baja", "promedio": 2.67, "n": 308},  # Portugal - Primeira Liga
    "portugal|segunda liga": {"nivel": "Baja", "clase": "baja", "promedio": 2.43, "n": 308},  # Portugal - Segunda Liga
    "portugal|taca de portugal": {"nivel": "Media", "clase": "media", "promedio": 3.10, "n": 150},  # Portugal - Taça de Portugal
    "qatar|emir cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.26, "n": 19},  # Qatar - Emir Cup
    "qatar|qsl cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.55, "n": 113},  # Qatar - QSL Cup
    "qatar|second division": {"nivel": "Media", "clase": "media", "promedio": 3.02, "n": 56},  # Qatar - Second Division
    "qatar|stars league": {"nivel": "Alta", "clase": "alta", "promedio": 3.32, "n": 133},  # Qatar - Stars League
    "romania|cupa romaniei": {"nivel": "Alta", "clase": "alta", "promedio": 3.58, "n": 151},  # Romania - Cupa României
    "romania|liga 1 feminin": {"nivel": "Alta", "clase": "alta", "promedio": 3.67, "n": 104},  # Romania - Liga 1 Feminin
    "romania|liga i": {"nivel": "Baja", "clase": "baja", "promedio": 2.55, "n": 321},  # Romania - Liga I
    "romania|liga ii": {"nivel": "Baja", "clase": "baja", "promedio": 2.71, "n": 318},  # Romania - Liga II
    "romania|liga iii play offs": {"nivel": "Media", "clase": "media", "promedio": 3.12, "n": 131},  # Romania - Liga III - Play-offs
    "romania|liga iii serie 1": {"nivel": "Media", "clase": "media", "promedio": 3.04, "n": 159},  # Romania - Liga III - Serie 1
    "romania|liga iii serie 2": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.91, "n": 159},  # Romania - Liga III - Serie 2
    "romania|liga iii serie 3": {"nivel": "Alta", "clase": "alta", "promedio": 3.54, "n": 160},  # Romania - Liga III - Serie 3
    "romania|liga iii serie 4": {"nivel": "Media", "clase": "media", "promedio": 3.08, "n": 159},  # Romania - Liga III - Serie 4
    "romania|liga iii serie 5": {"nivel": "Media", "clase": "media", "promedio": 2.92, "n": 133},  # Romania - Liga III - Serie 5
    "romania|liga iii serie 6": {"nivel": "Alta", "clase": "alta", "promedio": 3.22, "n": 160},  # Romania - Liga III - Serie 6
    "romania|liga iii serie 7": {"nivel": "Alta", "clase": "alta", "promedio": 3.20, "n": 153},  # Romania - Liga III - Serie 7
    "romania|liga iii serie 8": {"nivel": "Media", "clase": "media", "promedio": 2.84, "n": 153},  # Romania - Liga III - Serie 8
    "russia|cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.72, "n": 158},  # Russia - Cup
    "russia|first league": {"nivel": "Baja", "clase": "baja", "promedio": 2.32, "n": 305},  # Russia - First League
    "russia|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.52, "n": 244},  # Russia - Premier League
    "russia|second league group 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.38, "n": 238},  # Russia - Second League - Group 1
    "russia|second league group 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.57, "n": 210},  # Russia - Second League - Group 2
    "russia|second league group 3": {"nivel": "Media", "clase": "media", "promedio": 2.87, "n": 222},  # Russia - Second League - Group 3
    "russia|second league group 4": {"nivel": "Media", "clase": "media", "promedio": 2.92, "n": 172},  # Russia - Second League - Group 4
    "russia|second league a division a gold": {"nivel": "Baja", "clase": "baja", "promedio": 2.32, "n": 180},  # Russia - Second League A - Division A Gold
    "russia|second league a division a silver": {"nivel": "Baja", "clase": "baja", "promedio": 2.55, "n": 145},  # Russia - Second League A - Division A Silver
    "russia|supreme division women": {"nivel": "Baja", "clase": "baja", "promedio": 2.65, "n": 144},  # Russia - Supreme Division Women
    "russia|youth championship": {"nivel": "Alta", "clase": "alta", "promedio": 3.29, "n": 252},  # Russia - Youth Championship
    "rwanda|national soccer league": {"nivel": "Baja", "clase": "baja", "promedio": 2.14, "n": 306},  # Rwanda - National Soccer League
    "san marino|campionato": {"nivel": "Baja", "clase": "baja", "promedio": 2.77, "n": 256},  # San-Marino - Campionato
    "san marino|coppa titano": {"nivel": "Baja", "clase": "baja", "promedio": 2.37, "n": 27},  # San-Marino - Coppa Titano
    "saudi arabia|division 1": {"nivel": "Media", "clase": "media", "promedio": 2.96, "n": 308},  # Saudi-Arabia - Division 1
    "saudi arabia|division 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.70, "n": 482},  # Saudi-Arabia - Division 2
    "saudi arabia|king's cup": {"nivel": "Media", "clase": "media", "promedio": 2.94, "n": 31},  # Saudi-Arabia - King's Cup
    "saudi arabia|premier league women": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.41, "n": 56},  # Saudi-Arabia - Premier League Women
    "saudi arabia|pro league": {"nivel": "Media", "clase": "media", "promedio": 3.01, "n": 306},  # Saudi-Arabia - Pro League
    "scotland|challenge cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.76, "n": 121},  # Scotland - Challenge Cup
    "scotland|championship": {"nivel": "Baja", "clase": "baja", "promedio": 2.42, "n": 186},  # Scotland - Championship
    "scotland|fa cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.36, "n": 127},  # Scotland - FA Cup
    "scotland|football league highland league": {"nivel": "Alta", "clase": "alta", "promedio": 3.32, "n": 306},  # Scotland - Football League - Highland League
    "scotland|football league lowland league": {"nivel": "Alta", "clase": "alta", "promedio": 3.67, "n": 306},  # Scotland - Football League - Lowland League
    "scotland|league cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.33, "n": 95},  # Scotland - League Cup
    "scotland|league one": {"nivel": "Baja", "clase": "baja", "promedio": 2.67, "n": 186},  # Scotland - League One
    "scotland|league two": {"nivel": "Media", "clase": "media", "promedio": 2.92, "n": 182},  # Scotland - League Two
    "scotland|premiership": {"nivel": "Baja", "clase": "baja", "promedio": 2.75, "n": 234},  # Scotland - Premiership
    "scotland|swpl cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 5.16, "n": 19},  # Scotland - SWPL Cup
    "senegal|ligue 1": {"nivel": "Baja", "clase": "baja", "promedio": 1.66, "n": 264},  # Senegal - Ligue 1
    "serbia|cup": {"nivel": "Media", "clase": "media", "promedio": 3.03, "n": 34},  # Serbia - Cup
    "serbia|prva liga": {"nivel": "Baja", "clase": "baja", "promedio": 2.32, "n": 300},  # Serbia - Prva Liga
    "serbia|srpska liga belgrade": {"nivel": "Media", "clase": "media", "promedio": 3.01, "n": 181},  # Serbia - Srpska Liga - Belgrade
    "serbia|srpska liga east": {"nivel": "Alta", "clase": "alta", "promedio": 3.66, "n": 232},  # Serbia - Srpska Liga - East
    "serbia|srpska liga vojvodina": {"nivel": "Baja", "clase": "baja", "promedio": 2.72, "n": 238},  # Serbia - Srpska Liga - Vojvodina
    "serbia|srpska liga west": {"nivel": "Baja", "clase": "baja", "promedio": 2.26, "n": 240},  # Serbia - Srpska Liga - West
    "serbia|super liga": {"nivel": "Baja", "clase": "baja", "promedio": 2.66, "n": 296},  # Serbia - Super Liga
    "singapore|cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.47, "n": 15},  # Singapore - Cup
    "singapore|premier league": {"nivel": "Alta", "clase": "alta", "promedio": 3.61, "n": 84},  # Singapore - Premier League
    "slovakia|2. liga": {"nivel": "Media", "clase": "media", "promedio": 2.96, "n": 243},  # Slovakia - 2. liga
    "slovakia|3. liga center": {"nivel": "Alta", "clase": "alta", "promedio": 3.32, "n": 182},  # Slovakia - 3. liga - Center
    "slovakia|3. liga east": {"nivel": "Alta", "clase": "alta", "promedio": 3.37, "n": 182},  # Slovakia - 3. liga - East
    "slovakia|3. liga west": {"nivel": "Alta", "clase": "alta", "promedio": 3.28, "n": 238},  # Slovakia - 3. liga - West
    "slovakia|cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.98, "n": 292},  # Slovakia - Cup
    "slovakia|i liga women": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.17, "n": 128},  # Slovakia - I Liga - Women
    "slovakia|super liga": {"nivel": "Media", "clase": "media", "promedio": 2.82, "n": 192},  # Slovakia - Super Liga
    "slovenia|1. snl": {"nivel": "Media", "clase": "media", "promedio": 3.06, "n": 163},  # Slovenia - 1. SNL
    "slovenia|2. snl": {"nivel": "Media", "clase": "media", "promedio": 2.82, "n": 240},  # Slovenia - 2. SNL
    "slovenia|3. snl east": {"nivel": "Media", "clase": "media", "promedio": 3.02, "n": 161},  # Slovenia - 3. SNL - East
    "slovenia|3. snl west": {"nivel": "Media", "clase": "media", "promedio": 3.19, "n": 181},  # Slovenia - 3. SNL - West
    "slovenia|cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.87, "n": 31},  # Slovenia - Cup
    "south africa|1st division": {"nivel": "Baja", "clase": "baja", "promedio": 2.28, "n": 239},  # South-Africa - 1st Division
    "south africa|cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.03, "n": 39},  # South-Africa - Cup
    "south africa|diski challenge": {"nivel": "Media", "clase": "media", "promedio": 3.02, "n": 240},  # South-Africa - Diski Challenge
    "south africa|league cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.73, "n": 15},  # South-Africa - League Cup
    "south africa|premier soccer league": {"nivel": "Baja", "clase": "baja", "promedio": 2.00, "n": 250},  # South-Africa - Premier Soccer League
    "south korea|k league 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.54, "n": 213},  # South-Korea - K League 1
    "south korea|k league 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.59, "n": 283},  # South-Korea - K League 2
    "south korea|k3 league": {"nivel": "Baja", "clase": "baja", "promedio": 2.44, "n": 218},  # South-Korea - K3 League
    "south korea|wk league": {"nivel": "Baja", "clase": "baja", "promedio": 2.76, "n": 99},  # South-Korea - WK-League
    "spain|copa del rey": {"nivel": "Alta", "clase": "alta", "promedio": 3.23, "n": 137},  # Spain - Copa del Rey
    "spain|copa federacion": {"nivel": "Media", "clase": "media", "promedio": 3.06, "n": 31},  # Spain - Copa Federacion
    "spain|la liga": {"nivel": "Baja", "clase": "baja", "promedio": 2.69, "n": 380},  # Spain - La Liga
    "spain|primera division femenina": {"nivel": "Media", "clase": "media", "promedio": 2.88, "n": 240},  # Spain - Primera División Femenina
    "spain|primera division rfef group 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.42, "n": 380},  # Spain - Primera División RFEF - Group 1
    "spain|primera division rfef group 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.25, "n": 380},  # Spain - Primera División RFEF - Group 2
    "spain|segunda division": {"nivel": "Baja", "clase": "baja", "promedio": 2.63, "n": 468},  # Spain - Segunda División
    "spain|segunda division rfef group 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.54, "n": 306},  # Spain - Segunda División RFEF - Group 1
    "spain|segunda division rfef group 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.51, "n": 306},  # Spain - Segunda División RFEF - Group 2
    "spain|segunda division rfef group 3": {"nivel": "Baja", "clase": "baja", "promedio": 2.42, "n": 306},  # Spain - Segunda División RFEF - Group 3
    "spain|segunda division rfef group 4": {"nivel": "Baja", "clase": "baja", "promedio": 2.28, "n": 306},  # Spain - Segunda División RFEF - Group 4
    "spain|segunda division rfef group 5": {"nivel": "Baja", "clase": "baja", "promedio": 2.56, "n": 306},  # Spain - Segunda División RFEF - Group 5
    "spain|segunda division rfef play offs": {"nivel": "Baja", "clase": "baja", "promedio": 2.00, "n": 34},  # Spain - Segunda División RFEF - Play-offs
    "spain|tercera division rfef group 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.44, "n": 312},  # Spain - Tercera División RFEF - Group 1
    "spain|tercera division rfef group 10": {"nivel": "Baja", "clase": "baja", "promedio": 2.47, "n": 312},  # Spain - Tercera División RFEF - Group 10
    "spain|tercera division rfef group 11": {"nivel": "Baja", "clase": "baja", "promedio": 2.74, "n": 312},  # Spain - Tercera División RFEF - Group 11
    "spain|tercera division rfef group 12": {"nivel": "Baja", "clase": "baja", "promedio": 2.47, "n": 312},  # Spain - Tercera División RFEF - Group 12
    "spain|tercera division rfef group 13": {"nivel": "Baja", "clase": "baja", "promedio": 2.38, "n": 312},  # Spain - Tercera División RFEF - Group 13
    "spain|tercera division rfef group 14": {"nivel": "Baja", "clase": "baja", "promedio": 2.49, "n": 311},  # Spain - Tercera División RFEF - Group 14
    "spain|tercera division rfef group 15": {"nivel": "Baja", "clase": "baja", "promedio": 2.72, "n": 312},  # Spain - Tercera División RFEF - Group 15
    "spain|tercera division rfef group 16": {"nivel": "Media", "clase": "media", "promedio": 2.84, "n": 312},  # Spain - Tercera División RFEF - Group 16
    "spain|tercera division rfef group 17": {"nivel": "Baja", "clase": "baja", "promedio": 2.38, "n": 312},  # Spain - Tercera División RFEF - Group 17
    "spain|tercera division rfef group 18": {"nivel": "Baja", "clase": "baja", "promedio": 2.15, "n": 312},  # Spain - Tercera División RFEF - Group 18
    "spain|tercera division rfef group 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.61, "n": 312},  # Spain - Tercera División RFEF - Group 2
    "spain|tercera division rfef group 3": {"nivel": "Baja", "clase": "baja", "promedio": 2.62, "n": 312},  # Spain - Tercera División RFEF - Group 3
    "spain|tercera division rfef group 4": {"nivel": "Baja", "clase": "baja", "promedio": 2.56, "n": 310},  # Spain - Tercera División RFEF - Group 4
    "spain|tercera division rfef group 5": {"nivel": "Baja", "clase": "baja", "promedio": 2.42, "n": 311},  # Spain - Tercera División RFEF - Group 5
    "spain|tercera division rfef group 6": {"nivel": "Baja", "clase": "baja", "promedio": 2.29, "n": 312},  # Spain - Tercera División RFEF - Group 6
    "spain|tercera division rfef group 7": {"nivel": "Baja", "clase": "baja", "promedio": 2.67, "n": 312},  # Spain - Tercera División RFEF - Group 7
    "spain|tercera division rfef group 8": {"nivel": "Baja", "clase": "baja", "promedio": 2.38, "n": 312},  # Spain - Tercera División RFEF - Group 8
    "spain|tercera division rfef group 9": {"nivel": "Baja", "clase": "baja", "promedio": 2.20, "n": 312},  # Spain - Tercera División RFEF - Group 9
    "spain|tercera division rfef promotion play offs": {"nivel": "Baja", "clase": "baja", "promedio": 2.28, "n": 18},  # Spain - Tercera División RFEF - Promotion - Play-offs
    "sudan|sudani premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.30, "n": 175},  # Sudan - Sudani Premier League
    "suriname|eerste divisie": {"nivel": "Alta", "clase": "alta", "promedio": 3.26, "n": 121},  # Suriname - Eerste Divisie
    "sweden|allsvenskan": {"nivel": "Media", "clase": "media", "promedio": 3.00, "n": 225},  # Sweden - Allsvenskan
    "sweden|damallsvenskan": {"nivel": "Media", "clase": "media", "promedio": 3.18, "n": 170},  # Sweden - Damallsvenskan
    "sweden|division 2 norra gotaland": {"nivel": "Alta", "clase": "alta", "promedio": 3.21, "n": 184},  # Sweden - Division 2 - Norra Götaland
    "sweden|division 2 norra svealand": {"nivel": "Alta", "clase": "alta", "promedio": 3.43, "n": 184},  # Sweden - Division 2 - Norra Svealand
    "sweden|division 2 norrland": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.72, "n": 170},  # Sweden - Division 2 - Norrland
    "sweden|division 2 sodra gotaland": {"nivel": "Alta", "clase": "alta", "promedio": 3.34, "n": 184},  # Sweden - Division 2 - Södra Götaland
    "sweden|division 2 sodra svealand": {"nivel": "Alta", "clase": "alta", "promedio": 3.64, "n": 183},  # Sweden - Division 2 - Södra Svealand
    "sweden|division 2 vastra gotaland": {"nivel": "Alta", "clase": "alta", "promedio": 3.52, "n": 184},  # Sweden - Division 2 - Västra Götaland
    "sweden|elitettan": {"nivel": "Media", "clase": "media", "promedio": 3.08, "n": 183},  # Sweden - Elitettan
    "sweden|ettan norra": {"nivel": "Alta", "clase": "alta", "promedio": 3.38, "n": 232},  # Sweden - Ettan - Norra
    "sweden|ettan sodra": {"nivel": "Media", "clase": "media", "promedio": 3.06, "n": 232},  # Sweden - Ettan - Södra
    "sweden|superettan": {"nivel": "Media", "clase": "media", "promedio": 2.91, "n": 244},  # Sweden - Superettan
    "sweden|svenska cupen": {"nivel": "Alta", "clase": "alta", "promedio": 3.46, "n": 128},  # Sweden - Svenska Cupen
    "sweden|svenska cupen women": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.98, "n": 61},  # Sweden - Svenska Cupen - Women
    "switzerland|1. liga classic group 1": {"nivel": "Alta", "clase": "alta", "promedio": 3.44, "n": 239},  # Switzerland - 1. Liga Classic - Group 1
    "switzerland|1. liga classic group 2": {"nivel": "Alta", "clase": "alta", "promedio": 3.42, "n": 239},  # Switzerland - 1. Liga Classic - Group 2
    "switzerland|1. liga classic group 3": {"nivel": "Alta", "clase": "alta", "promedio": 3.42, "n": 240},  # Switzerland - 1. Liga Classic - Group 3
    "switzerland|1. liga promotion": {"nivel": "Alta", "clase": "alta", "promedio": 3.69, "n": 307},  # Switzerland - 1. Liga Promotion
    "switzerland|axa women’s super league": {"nivel": "Media", "clase": "media", "promedio": 2.91, "n": 120},  # Switzerland - AXA Women’s Super League
    "switzerland|challenge league": {"nivel": "Media", "clase": "media", "promedio": 3.06, "n": 180},  # Switzerland - Challenge League
    "switzerland|erste liga cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.44, "n": 32},  # Switzerland - Erste Liga Cup
    "switzerland|schweizer cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.60, "n": 63},  # Switzerland - Schweizer Cup
    "switzerland|super league": {"nivel": "Alta", "clase": "alta", "promedio": 3.27, "n": 230},  # Switzerland - Super League
    "syria|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.49, "n": 228},  # Syria - Premier League
    "tajikistan|vysshaya liga": {"nivel": "Baja", "clase": "baja", "promedio": 2.52, "n": 126},  # Tajikistan - Vysshaya Liga
    "tanzania|ligi kuu bara": {"nivel": "Baja", "clase": "baja", "promedio": 2.21, "n": 234},  # Tanzania - Ligi kuu Bara
    "thailand|fa cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.75, "n": 63},  # Thailand - FA Cup
    "thailand|league cup": {"nivel": "Media", "clase": "media", "promedio": 2.92, "n": 48},  # Thailand - League Cup
    "thailand|thai league 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.67, "n": 240},  # Thailand - Thai League 1
    "thailand|thai league 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.77, "n": 312},  # Thailand - Thai League 2
    "trinidad and tobago|pro league": {"nivel": "Alta", "clase": "alta", "promedio": 3.38, "n": 130},  # Trinidad-And-Tobago - Pro League
    "tunisia|cup": {"nivel": "Media", "clase": "media", "promedio": 2.83, "n": 59},  # Tunisia - Cup
    "tunisia|ligue 1": {"nivel": "Baja", "clase": "baja", "promedio": 1.72, "n": 237},  # Tunisia - Ligue 1
    "tunisia|ligue 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.22, "n": 368},  # Tunisia - Ligue 2
    "turkey|1. lig": {"nivel": "Media", "clase": "media", "promedio": 2.92, "n": 384},  # Turkey - 1. Lig
    "turkey|2. lig": {"nivel": "Media", "clase": "media", "promedio": 2.96, "n": 622},  # Turkey - 2. Lig
    "turkey|3. lig group 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.43, "n": 240},  # Turkey - 3. Lig - Group 1
    "turkey|3. lig group 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.62, "n": 239},  # Turkey - 3. Lig - Group 2
    "turkey|3. lig group 3": {"nivel": "Baja", "clase": "baja", "promedio": 2.55, "n": 240},  # Turkey - 3. Lig - Group 3
    "turkey|3. lig group 4": {"nivel": "Media", "clase": "media", "promedio": 2.85, "n": 236},  # Turkey - 3. Lig - Group 4
    "turkey|3. lig play offs": {"nivel": "Baja", "clase": "baja", "promedio": 2.38, "n": 26},  # Turkey - 3. Lig - Play-offs
    "turkey|super lig": {"nivel": "Baja", "clase": "baja", "promedio": 2.65, "n": 306},  # Turkey - Süper Lig
    "turkey|turkiye kupası": {"nivel": "Alta", "clase": "alta", "promedio": 3.35, "n": 182},  # Turkey - Türkiye Kupası
    "turkmenistan|yokary liga": {"nivel": "Media", "clase": "media", "promedio": 2.97, "n": 112},  # Turkmenistan - Ýokary Liga
    "uganda|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.09, "n": 237},  # Uganda - Premier League
    "ukraine|cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.49, "n": 57},  # Ukraine - Cup
    "ukraine|druha liga": {"nivel": "Media", "clase": "media", "promedio": 2.92, "n": 316},  # Ukraine - Druha Liga
    "ukraine|persha liga": {"nivel": "Baja", "clase": "baja", "promedio": 2.28, "n": 238},  # Ukraine - Persha Liga
    "ukraine|premier league": {"nivel": "Baja", "clase": "baja", "promedio": 2.56, "n": 243},  # Ukraine - Premier League
    "ukraine|u19 league": {"nivel": "Media", "clase": "media", "promedio": 3.15, "n": 240},  # Ukraine - U19 League
    "united arab emirates|division 1": {"nivel": "Media", "clase": "media", "promedio": 2.90, "n": 210},  # United-Arab-Emirates - Division 1
    "united arab emirates|league cup": {"nivel": "Media", "clase": "media", "promedio": 2.84, "n": 25},  # United-Arab-Emirates - League Cup
    "united arab emirates|presidents cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.71, "n": 28},  # United-Arab-Emirates - Presidents Cup
    "united arab emirates|pro league": {"nivel": "Media", "clase": "media", "promedio": 2.82, "n": 182},  # United-Arab-Emirates - Pro League
    "united arab emirates|pro league u23": {"nivel": "Alta", "clase": "alta", "promedio": 3.24, "n": 182},  # United-Arab-Emirates - Pro League U23
    "uruguay|copa de la liga auf": {"nivel": "Baja", "clase": "baja", "promedio": 1.93, "n": 15},  # Uruguay - Copa De La Liga Auf
    "uruguay|copa uruguay": {"nivel": "Baja", "clase": "baja", "promedio": 2.65, "n": 31},  # Uruguay - Copa Uruguay
    "uruguay|primera division apertura": {"nivel": "Baja", "clase": "baja", "promedio": 2.45, "n": 176},  # Uruguay - Primera División - Apertura
    "uruguay|primera division clausura": {"nivel": "Baja", "clase": "baja", "promedio": 2.28, "n": 124},  # Uruguay - Primera División - Clausura
    "uruguay|segunda division": {"nivel": "Baja", "clase": "baja", "promedio": 2.30, "n": 230},  # Uruguay - Segunda División
    "usa|major league soccer": {"nivel": "Alta", "clase": "alta", "promedio": 3.22, "n": 492},  # USA - Major League Soccer
    "usa|mls next pro": {"nivel": "Alta", "clase": "alta", "promedio": 3.46, "n": 445},  # USA - MLS Next Pro
    "usa|npsl": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.23, "n": 121},  # USA - NPSL
    "usa|nwsl women": {"nivel": "Baja", "clase": "baja", "promedio": 2.49, "n": 198},  # USA - NWSL Women
    "usa|us open cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.27, "n": 82},  # USA - US Open Cup
    "usa|usl championship": {"nivel": "Baja", "clase": "baja", "promedio": 2.68, "n": 376},  # USA - USL Championship
    "usa|usl league one": {"nivel": "Media", "clase": "media", "promedio": 2.85, "n": 242},  # USA - USL League One
    "usa|usl league one cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.76, "n": 107},  # USA - USL League One Cup
    "usa|usl league two": {"nivel": "Alta", "clase": "alta", "promedio": 3.62, "n": 982},  # USA - USL League Two
    "usa|usl super league": {"nivel": "Baja", "clase": "baja", "promedio": 2.65, "n": 129},  # USA - USL Super League
    "usa|usl w league": {"nivel": "Alta", "clase": "alta", "promedio": 3.61, "n": 466},  # USA - USL W League
    "usa|wpsl": {"nivel": "Alta", "clase": "alta", "promedio": 3.67, "n": 222},  # USA - WPSL
    "uzbekistan|pro league a": {"nivel": "Media", "clase": "media", "promedio": 2.83, "n": 102},  # Uzbekistan - Pro League A
    "uzbekistan|super league": {"nivel": "Baja", "clase": "baja", "promedio": 2.51, "n": 237},  # Uzbekistan - Super League
    "venezuela|copa venezuela": {"nivel": "Baja", "clase": "baja", "promedio": 2.77, "n": 70},  # Venezuela - Copa Venezuela
    "venezuela|primera division": {"nivel": "Baja", "clase": "baja", "promedio": 2.42, "n": 233},  # Venezuela - Primera División
    "venezuela|segunda division": {"nivel": "Baja", "clase": "baja", "promedio": 2.39, "n": 270},  # Venezuela - Segunda División
    "vietnam|cup": {"nivel": "Media", "clase": "media", "promedio": 2.85, "n": 27},  # Vietnam - Cup
    "vietnam|v.league 1": {"nivel": "Baja", "clase": "baja", "promedio": 2.63, "n": 191},  # Vietnam - V.League 1
    "vietnam|v.league 2": {"nivel": "Baja", "clase": "baja", "promedio": 2.55, "n": 137},  # Vietnam - V.League 2
    "wales|faw championship": {"nivel": "Alta", "clase": "alta", "promedio": 3.26, "n": 481},  # Wales - FAW Championship
    "wales|league cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.76, "n": 45},  # Wales - League Cup
    "wales|premier league": {"nivel": "Media", "clase": "media", "promedio": 2.87, "n": 195},  # Wales - Premier League
    "wales|welsh cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.26, "n": 100},  # Wales - Welsh Cup
    "world|afc challenge league": {"nivel": "Alta", "clase": "alta", "promedio": 3.37, "n": 49},  # World - AFC Challenge League
    "world|afc champions league elite": {"nivel": "Baja", "clase": "baja", "promedio": 2.66, "n": 117},  # World - AFC Champions League Elite
    "world|afc champions league two": {"nivel": "Media", "clase": "media", "promedio": 2.88, "n": 119},  # World - AFC Champions League Two
    "world|afc u17 asian cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.27, "n": 113},  # World - AFC U17 Asian Cup
    "world|afc u17 asian cup women": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.40, "n": 25},  # World - AFC U17 Asian Cup - Women
    "world|afc u20 asian cup women": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.68, "n": 73},  # World - AFC U20 Asian Cup - Women
    "world|afc u23 asian cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.28, "n": 32},  # World - AFC U23 Asian Cup
    "world|afc u23 asian cup qualification": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.11, "n": 66},  # World - AFC U23 Asian Cup - Qualification
    "world|afc women's champions league": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.98, "n": 52},  # World - AFC Women's Champions League
    "world|africa cup of nations": {"nivel": "Baja", "clase": "baja", "promedio": 2.37, "n": 52},  # World - Africa Cup of Nations
    "world|africa cup of nations women": {"nivel": "Baja", "clase": "baja", "promedio": 2.54, "n": 26},  # World - Africa Cup of Nations - Women
    "world|african nations championship": {"nivel": "Baja", "clase": "baja", "promedio": 2.05, "n": 44},  # World - African Nations Championship
    "world|agcff gulf champions league": {"nivel": "Baja", "clase": "baja", "promedio": 2.70, "n": 27},  # World - AGCFF Gulf Champions League
    "world|all island cup women": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.84, "n": 32},  # World - All-Island Cup - Women
    "world|arab cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.45, "n": 38},  # World - Arab Cup
    "world|arabian gulf cup u23": {"nivel": "Baja", "clase": "baja", "promedio": 2.33, "n": 15},  # World - Arabian Gulf Cup U23
    "world|asean championship u19": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.95, "n": 19},  # World - ASEAN Championship U19
    "world|asean championship u23": {"nivel": "Media", "clase": "media", "promedio": 3.19, "n": 16},  # World - ASEAN Championship U23
    "world|asean championship women": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.12, "n": 16},  # World - Asean Championship Women
    "world|asean club championship": {"nivel": "Alta", "clase": "alta", "promedio": 3.23, "n": 40},  # World - ASEAN Club Championship
    "world|asian cup qualification": {"nivel": "Alta", "clase": "alta", "promedio": 3.31, "n": 48},  # World - Asian Cup - Qualification
    "world|asian cup women": {"nivel": "Alta", "clase": "alta", "promedio": 3.59, "n": 27},  # World - Asian Cup Women
    "world|asian cup women qualification": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.77, "n": 56},  # World - Asian Cup Women - Qualification
    "world|caf champions league": {"nivel": "Baja", "clase": "baja", "promedio": 1.97, "n": 154},  # World - CAF Champions League
    "world|caf confederation cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.30, "n": 146},  # World - CAF Confederation Cup
    "world|caf cup of nations u17": {"nivel": "Baja", "clase": "baja", "promedio": 2.38, "n": 34},  # World - CAF Cup of Nations - U17
    "world|caf women's champions league": {"nivel": "Baja", "clase": "baja", "promedio": 2.31, "n": 16},  # World - CAF Women's Champions League
    "world|concacaf caribbean club championship": {"nivel": "Baja", "clase": "baja", "promedio": 2.50, "n": 28},  # World - CONCACAF Caribbean Club Championship
    "world|concacaf caribbean club shield": {"nivel": "Alta", "clase": "alta", "promedio": 3.36, "n": 28},  # World - CONCACAF Caribbean Club Shield
    "world|concacaf central american cup": {"nivel": "Media", "clase": "media", "promedio": 2.93, "n": 58},  # World - CONCACAF Central American Cup
    "world|concacaf champions league": {"nivel": "Media", "clase": "media", "promedio": 2.92, "n": 51},  # World - CONCACAF Champions League
    "world|concacaf gold cup": {"nivel": "Baja", "clase": "baja", "promedio": 2.36, "n": 25},  # World - CONCACAF Gold Cup
    "world|concacaf series": {"nivel": "Media", "clase": "media", "promedio": 3.11, "n": 35},  # World - CONCACAF Series
    "world|concacaf u20": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.04, "n": 67},  # World - CONCACAF U20
    "world|concacaf u20 qualification": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.04, "n": 67},  # World - CONCACAF U20 - Qualification
    "world|concacaf w champions cup": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 4.00, "n": 24},  # World - CONCACAF W Champions Cup
    "world|concacaf women u17": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 5.90, "n": 68},  # World - CONCACAF Women U17
    "world|conmebol u17": {"nivel": "Baja", "clase": "baja", "promedio": 2.79, "n": 28},  # World - CONMEBOL - U17
    "world|conmebol libertadores": {"nivel": "Baja", "clase": "baja", "promedio": 2.10, "n": 154},  # World - CONMEBOL Libertadores
    "world|conmebol libertadores femenina": {"nivel": "Baja", "clase": "baja", "promedio": 1.91, "n": 32},  # World - CONMEBOL Libertadores Femenina
    "world|conmebol libertadores u20": {"nivel": "Media", "clase": "media", "promedio": 2.82, "n": 22},  # World - CONMEBOL Libertadores U20
    "world|conmebol nations league women": {"nivel": "Media", "clase": "media", "promedio": 3.06, "n": 36},  # World - CONMEBOL Nations League Women
    "world|conmebol sudamericana": {"nivel": "Baja", "clase": "baja", "promedio": 2.20, "n": 157},  # World - CONMEBOL Sudamericana
    "world|conmebol u20 femenino": {"nivel": "Baja", "clase": "baja", "promedio": 2.74, "n": 35},  # World - CONMEBOL U20 Femenino
    "world|copa america femenina": {"nivel": "Alta", "clase": "alta", "promedio": 3.40, "n": 25},  # World - Copa America Femenina
    "world|cosafa u20 championship": {"nivel": "Baja", "clase": "baja", "promedio": 2.75, "n": 16},  # World - COSAFA U20 Championship
    "world|cotif tournament": {"nivel": "Baja", "clase": "baja", "promedio": 2.62, "n": 16},  # World - COTIF Tournament
    "world|fifa club world cup": {"nivel": "Media", "clase": "media", "promedio": 3.09, "n": 55},  # World - FIFA Club World Cup
    "world|fifa series": {"nivel": "Alta", "clase": "alta", "promedio": 3.67, "n": 33},  # World - FIFA Series
    "world|friendlies": {"nivel": "Media", "clase": "media", "promedio": 2.82, "n": 987},  # World - Friendlies
    "world|friendlies clubs": {"nivel": "Alta", "clase": "alta", "promedio": 3.42, "n": 5355},  # World - Friendlies Clubs
    "world|friendlies women": {"nivel": "Media", "clase": "media", "promedio": 3.08, "n": 591},  # World - Friendlies Women
    "world|kings world cup nations": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 10.50, "n": 40},  # World - Kings World Cup Nations
    "world|leagues cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.23, "n": 62},  # World - Leagues Cup
    "world|ofc pro league": {"nivel": "Alta", "clase": "alta", "promedio": 3.21, "n": 72},  # World - OFC Pro League
    "world|premier league international cup": {"nivel": "Alta", "clase": "alta", "promedio": 3.25, "n": 71},  # World - Premier League International Cup
    "world|serie rio de la plata": {"nivel": "Baja", "clase": "baja", "promedio": 2.32, "n": 22},  # World - Serie Rio De La Plata
    "world|tournoi maurice revello": {"nivel": "Media", "clase": "media", "promedio": 3.09, "n": 22},  # World - Tournoi Maurice Revello
    "world|u20 elite league": {"nivel": "Alta", "clase": "alta", "promedio": 3.52, "n": 21},  # World - U20 Elite League
    "world|uefa champions league": {"nivel": "Media", "clase": "media", "promedio": 3.18, "n": 281},  # World - UEFA Champions League
    "world|uefa champions league women": {"nivel": "Alta", "clase": "alta", "promedio": 3.41, "n": 153},  # World - UEFA Champions League Women
    "world|uefa championship women": {"nivel": "Alta", "clase": "alta", "promedio": 3.42, "n": 31},  # World - UEFA Championship - Women
    "world|uefa europa conference league": {"nivel": "Baja", "clase": "baja", "promedio": 2.78, "n": 409},  # World - UEFA Europa Conference League
    "world|uefa europa cup women": {"nivel": "Media", "clase": "media", "promedio": 3.16, "n": 83},  # World - UEFA Europa Cup - Women
    "world|uefa europa league": {"nivel": "Baja", "clase": "baja", "promedio": 2.68, "n": 271},  # World - UEFA Europa League
    "world|uefa nations league women": {"nivel": "Media", "clase": "media", "promedio": 3.05, "n": 20},  # World - UEFA Nations League - Women
    "world|uefa u17 championship": {"nivel": "Media", "clase": "media", "promedio": 3.13, "n": 15},  # World - UEFA U17 Championship
    "world|uefa u17 championship qualification": {"nivel": "Alta", "clase": "alta", "promedio": 3.59, "n": 156},  # World - UEFA U17 Championship - Qualification
    "world|uefa u17 championship women": {"nivel": "Baja", "clase": "baja", "promedio": 2.44, "n": 16},  # World - UEFA U17 Championship - Women
    "world|uefa u19 championship qualification": {"nivel": "Media", "clase": "media", "promedio": 3.17, "n": 196},  # World - UEFA U19 Championship - Qualification
    "world|uefa u21 championship": {"nivel": "Alta", "clase": "alta", "promedio": 3.40, "n": 15},  # World - UEFA U21 Championship
    "world|uefa u21 championship qualification": {"nivel": "Media", "clase": "media", "promedio": 3.12, "n": 169},  # World - UEFA U21 Championship - Qualification
    "world|uefa youth league": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 3.86, "n": 219},  # World - UEFA Youth League
    "world|world cup": {"nivel": "Media", "clase": "media", "promedio": 3.10, "n": 20},  # World - World Cup
    "world|world cup qualification africa": {"nivel": "Baja", "clase": "baja", "promedio": 2.58, "n": 106},  # World - World Cup - Qualification Africa
    "world|world cup qualification concacaf": {"nivel": "Baja", "clase": "baja", "promedio": 2.47, "n": 36},  # World - World Cup - Qualification CONCACAF
    "world|world cup qualification europe": {"nivel": "Alta", "clase": "alta", "promedio": 3.42, "n": 156},  # World - World Cup - Qualification Europe
    "world|world cup u17": {"nivel": "Media", "clase": "media", "promedio": 3.13, "n": 104},  # World - World Cup - U17
    "world|world cup u17 women": {"nivel": "Alta", "clase": "alta", "promedio": 3.37, "n": 52},  # World - World Cup - U17 - Women
    "world|world cup u20": {"nivel": "Media", "clase": "media", "promedio": 2.87, "n": 52},  # World - World Cup - U20
    "world|world cup women qualification concacaf": {"nivel": "Muy alta", "clase": "muy_alta", "promedio": 5.66, "n": 56},  # World - World Cup - Women - Qualification Concacaf
    "world|world cup women qualification europe": {"nivel": "Alta", "clase": "alta", "promedio": 3.43, "n": 168},  # World - World Cup - Women - Qualification Europe
    "world|youth viareggio cup": {"nivel": "Media", "clase": "media", "promedio": 3.04, "n": 47},  # World - Youth Viareggio Cup
    "zambia|super league": {"nivel": "Baja", "clase": "baja", "promedio": 1.74, "n": 304},  # Zambia - Super League
    "zimbabwe|premier soccer league": {"nivel": "Baja", "clase": "baja", "promedio": 1.82, "n": 331},  # Zimbabwe - Premier Soccer League
}


def nivel_liga(pais, liga):
    """Devuelve {"nivel","clase","promedio","n"} para ese pais+liga, o None."""
    return NIVEL_LIGAS.get(_normalizar(pais) + "|" + _normalizar(liga))
