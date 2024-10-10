import re
import requests
from bs4 import BeautifulSoup

def locality_name(data):
    key = "Adres"
    if key not in data:
        return None
    else:
        return data[key].split("-")[-1].strip()

def postal_code(data):
    key = "Adres"

    if key not in data:
        return None
    else:
        pattern = r"\d{4}"
        code_pattern = re.findall(pattern, data[key])
        return int(code_pattern[0])

def price(data):
    key = "Prijs"

    if key not in data:
        return None
    else:
        pattern = r"\d{4,}"
        price_pattern = re.findall(pattern, data[key])
        return int((price_pattern)[0])

def type_of_property(url):
    subtype =  url.split("zoekertje/")[1].split("/")[0]

    if subtype in ["Benedenverdieping", "Triplex", "Penthouse", "Kot", "Duplux", "Studio", "Loft", "Serviceflat"]:
        return "apartment"
    else:
        return "house"

def subtype_of_property(url):
    return url.split("zoekertje/")[1].split("/")[0]

def type_of_sale(data):
    key = "Plaats van de verkoop"
    if key not in data:
        return 'Vaste prijs'
    else:
        return 'Openbare verkoop'

def nr_or_rooms(data):
    key = "Slaapkamers"
    if key not in data:
        return None
    else:
        return int(data[key])

def living_area(data):
    key = "Bewoonbare oppervlakte"
    if key not in data:
        return None
    else:
        return int(data[key].split(" ")[0].strip())

def equiped_kitchen(data):
    key = "Type keuken"
    if key not in data:
        return None
    else:
        return 1 if "geïnstalleerd" in data[key].lower() else 0

def furnished(data):
    key = "Gemeubeld"
    if key not in data:
        return None
    else:
        return 1 if data[key] == "Ja" else 0

def open_fire(data):
    key = "Aantal open haarden"
    if key not in data:
        return None
    else:
        return 1

def terrace(data):
    key = "Oppervlakte terras"
    if key not in data:
        return None
    else:
        return int(data[key].split(" ")[0].strip())

def garden(data):
    key = "Oppervlakte tuin"
    if key not in data:
        return None
    else:
        return int(data[key].split(" ")[0].strip())

def nr_of_facades(data):
    key = "Aantal gevels"
    if key not in data:
        return None
    else:
        return int(data[key])

def swimming_pool(data):
    key = "Zwembad"
    if key not in data:
        return None
    else:
        return 1 if data[key] == "Ja" else 0

def state_of_building(data):
    key = "Staat van het gebouw"
    if key not in data:
        return None
    else:
        return data[key]
