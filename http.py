from flask import Flask, render_template
import dvs
import ovfiets
from station import get_station
import datetime

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/search")
def search():
  return render_template("search.html")

@app.route("/train/today/<trein_nummer>")
def trein_today(trein_nummer):
  return render_template("trein.html", trein = dvs.train("https://dvs.ovdingen.nl", datetime.datetime.today().strftime('%Y-%m-%d'), trein_nummer, None, True))

@app.route("/train/today/<trein_nummer>/<station>")
def trein_today_station(trein_nummer, station):
  return render_template("trein.html", trein = dvs.train("https://dvs.ovdingen.nl", datetime.datetime.today().strftime('%Y-%m-%d'), trein_nummer, station, True), cur_station_meta = get_station(station, "https://stations.ovdingen.nl"))

@app.route("/drgl/<date>/<trein_nummer>")
def drgl(date, trein_nummer):
  return render_template("drgl.html", trein = dvs.train("https://dvs.ovdingen.nl", date, trein_nummer))

@app.route("/station/<station>/")
def station(station):
  return render_template("station.html", station = dvs.station("https://dvs.ovdingen.nl", station), ovfiets = ovfiets.station("https://ovfiets.ovdingen.nl/", station), meta = get_station(station, "https://stations.ovdingen.nl"))

@app.route("/ovfiets/<pup>/")
def ovfietspup(pup):
  return render_template("ovfiets.html", ovfiets = ovfiets.pickuppoint("https://ovfiets.ovdingen.nl", pup))
