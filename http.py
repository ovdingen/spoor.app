from flask import Flask, render_template
import dvs
import ovfiets
import datetime

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/train/today/<trein_nummer>")
def trein_today(trein_nummer):
  return render_template("trein.html", trein = dvs.train("https://dvs.ovdingen.nl", datetime.datetime.today().strftime('%Y-%m-%d'), trein_nummer))

@app.route("/drgl/<date>/<trein_nummer>")
def drgl(date, trein_nummer):
  return render_template("drgl.html", trein = dvs.train("https://dvs.ovdingen.nl", date, trein_nummer))

@app.route("/station/<station>/")
def station(station):
  return render_template("station.html", station = dvs.station("https://dvs.ovdingen.nl", station), ovfiets = ovfiets.station("https://ovfiets.ovdingen.nl/", station))

@app.route("/ovfiets/<pup>/")
def ovfietspup(pup):
  return render_template("ovfiets.html", ovfiets = ovfiets.pickuppoint("https://ovfiets.ovdingen.nl", pup))