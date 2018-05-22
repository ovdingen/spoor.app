import requests
import urllib
import json
import datetime
import dateutil.parser

class TimeError(Exception):
    pass

def validate_date(date_in):
    try:
        datetime.datetime.strptime(date_in, '%Y-%m-%d')
        return True
    except ValueError:
        return False



def station(addr, station_code):
    headers = {
        "User-Agent": "Spoor.app website backend/1.0"
    }
    station_code_esc = urllib.quote(station_code, safe='')

    r = requests.get(addr + "/v2/station/" + station_code_esc, headers=headers)
    response = json.loads(r.text)
    
    if response['result'] != "OK":
        return False
    
    return response['vertrektijden']
    
def train(addr, day, service_number, station = None, parse_time = False):
    headers = {
        "User-Agent": "Spoor.app website backend/1.0"
    }

    if validate_date(day) is False:
        raise TimeError("Date input is incorrect")

    day_esc = urllib.quote(day, safe='')
    service_number_esc = urllib.quote(service_number, safe='')

    if station is not None:
        station_esc = urllib.quote(station, safe='')
        url = addr + "/v2/trein/" + service_number_esc + "/" + day_esc + "/" + station_esc
    else:
        url = addr + "/v2/trein/" + service_number_esc + "/" + day_esc

    r = requests.get(url, headers=headers)
    response = json.loads(r.text)
    if response['result'] != "OK":
        return False
    if response['trein'] is None:
        return False
    if parse_time is not False:
        for vleugel in response['trein']['vleugels']:
            for stop in vleugel['stopstations']:
                if 'aankomst' in stop:
                    if stop['aankomst'] is not None:
                        stop['aankomst'] = dateutil.parser.parse(stop['aankomst']).strftime("%H:%M")
                if 'vertrek' in stop:
                    if stop['vertrek'] is not None:
                        stop['vertrek'] = dateutil.parser.parse(stop['vertrek']).strftime("%H:%M")
        if 'aankomst' in response['trein']:
            response['trein']['aankomst'] = dateutil.parser.parse(response['trein']['aankomst']).strftime("%H:%M")
        if 'vertrek' in response['trein']:
            response['trein']['vertrek'] = dateutil.parser.parse(response['trein']['vertrek']).strftime("%H:%M")

    return response['trein']
