import requests
import json
import urllib

def station(addr, station_code):
    headers = {
        "User-Agent": "Trein.app website backend/1.0"
    }
    station_code_esc = urllib.quote(station_code, safe='')

    r = requests.get(addr + "/v1/station/" + station_code_esc, headers=headers)
    response = json.loads(r.text)
    
    if response['status'] != "OK":
        return False
    
    return response['availability']

def pickuppoint(addr, point_code):
    headers = {
        "User-Agent": "Trein.app website backend/1.0"
    }
    point_code_esc = urllib.quote(point_code, safe='')

    r = requests.get(addr + "/v1/afgiftepunt/" + point_code_esc, headers=headers)
    response = json.loads(r.text)
    
    if response['status'] != "OK":
        return False
    
    return response['availability']