from flask import Flask, request, jsonify, render_template, send_file
import sqlite3
import hashlib
import pandas as pd
import xarray as xr
from geopy.geocoders import Nominatim
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT,password TEXT)")
    conn.commit()
    conn.close()

init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():

    data = request.json
    username = data["username"]
    password = hashlib.sha256(data["password"].encode()).hexdigest()

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("INSERT INTO users VALUES (?,?)",(username,password))

    conn.commit()
    conn.close()

    return jsonify({"message":"User created"})


@app.route("/login", methods=["POST"])
def login():

    data = request.json

    username = data["username"]
    password = hashlib.sha256(data["password"].encode()).hexdigest()

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))

    result = c.fetchone()

    conn.close()

    if result:
        return jsonify({"status":"success"})
    else:
        return jsonify({"status":"fail"})


@app.route("/climate", methods=["POST"])
def climate():

    location = request.json["location"]

    geolocator = Nominatim(user_agent="climate_app")
    loc = geolocator.geocode(location)

    lat = loc.latitude
    lon = loc.longitude

    ds = xr.tutorial.open_dataset("air_temperature")

    point = ds.air.sel(lat=lat, lon=lon, method="nearest")

    df = point.to_dataframe().reset_index()

    data = df["air"].tolist()[:12]

    return jsonify(data)


@app.route("/report", methods=["POST"])
def report():

    location = request.json["location"]

    file="climate_report.pdf"

    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(file)

    elements=[]

    elements.append(Paragraph("Climate Report", styles['Title']))
    elements.append(Paragraph(f"Location: {location}", styles['Normal']))

    pdf.build(elements)

    return send_file(file, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
