from flask import Flask, render_template
import dvs
import ovfiets
from station import get_station
import datetime
import json

with open('config.json') as f: # app version, name and stuff
    app_config = json.load(f)

global config

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
  return render_template("index.html", app_config = app_config)

@app.route("/search")
def search():
  return render_template("search.html")

@app.route("/sw.js")
def sw():
  return Response(r, content_type='application/javascript; charset=utf-8')
  return render_template("/sw.js")

@app.route("/offline")
def offline():
  return render_template("offline.html")

@app.route("/train/today/<trein_nummer>")
def trein_today(trein_nummer):
  return render_template("trein.html", trein = dvs.train("https://dvs.ovdingen.nl", datetime.datetime.today().strftime('%Y-%m-%d'), trein_nummer, None, True), app_config = app_config)

@app.route("/train/today/<trein_nummer>/<station>")
def trein_today_station(trein_nummer, station):
  return render_template("trein.html", trein = dvs.train("https://dvs.ovdingen.nl", datetime.datetime.today().strftime('%Y-%m-%d'), trein_nummer, station, True), cur_station_meta = get_station(station, "https://stations.ovdingen.nl"), app_config = app_config)

@app.route("/drgl/<date>/<trein_nummer>")
def drgl(date, trein_nummer):
  return render_template("drgl.html", trein = dvs.train("https://dvs.ovdingen.nl", date, trein_nummer), config = app_config)

@app.route("/station/<station>/")
def station(station):
  return render_template("station.html", station = dvs.station("https://dvs.ovdingen.nl", station), ovfiets = ovfiets.station("https://ovfiets.ovdingen.nl/", station), meta = get_station(station, "https://stations.ovdingen.nl"), app_config = app_config)

@app.route("/ovfiets/<pup>/")
def ovfietspup(pup):
  return render_template("ovfiets.html", ovfiets = ovfiets.pickuppoint("https://ovfiets.ovdingen.nl", pup), app_config = app_config)
