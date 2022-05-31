from flask import Flask, render_template, request, Response, redirect, url_for
app = Flask(__name__)

import io
import geopandas as gpd
import pandas as pd
import contextily as ctx
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import folium
from folium import plugins
import requests
from xml.etree import ElementTree
import numpy as np

palestre = pd.read_csv('/workspace/Progetto/csv/palestre.csv', sep=",")

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/esercizi', methods=['GET'])
def esercizi():
    return render_template('esercizi.html')

@app.route('/grafico', methods=['GET'])
def grafico():
    return render_template('grafico.html')

@app.route('/addominali', methods=['GET'])
def addominali():
    return render_template('Addominali.html')

@app.route('/bicipiti', methods=['GET'])
def bicipiti():
    return render_template('Bicipiti.html')

@app.route('/avambraccio', methods=['GET'])
def avambraccio():
    return render_template('Avambraccio.html')

@app.route('/bicipitefemorale', methods=['GET'])
def bicipitefemorale():
    return render_template('Bicipite Femorale.html')

@app.route('/dorsali', methods=['GET'])
def dorsali():
    return render_template('Dorsali.html')

@app.route('/glutei', methods=['GET'])
def glutei():
    return render_template('Glutei.html')

@app.route('/petto', methods=['GET'])
def petto():
    return render_template('Petto.html')

@app.route('/polpaccio', methods=['GET'])
def polpaccio():
    return render_template('Polpaccio.html')

@app.route('/quadricipiti', methods=['GET'])
def quadricipiti():
    return render_template('Quadricipiti.html')

@app.route('/spalle', methods=['GET'])
def spalle():
    return render_template('Spalle.html')

@app.route('/trapezio', methods=['GET'])
def trapezio():
    return render_template('Trapezio.html')

@app.route('/trapezio2', methods=['GET'])
def trapezio2():
    return render_template('Trapezio2.html')

@app.route('/zonalombare', methods=['GET'])
def zonalombare():
    return render_template('Zona Lombare.html')

@app.route('/tricipiti', methods=['GET'])
def tricipiti():
    return render_template('Tricipiti.html')

@app.route('/pagmappa', methods=['GET'])
def pagmappa():
    return render_template("paginaperlamappa.html")

@app.route('/mappa', methods=['GET'])
def mappa():
    m = folium.Map(location=[45.50,9.20], tiles="OpenStreetMap", zoom_start=12)
    minimap = plugins.MiniMap()
    m.add_child(minimap)
    for i in range(0,len(palestre)):
        folium.Marker(
            location=[palestre.iloc[i]['Latitudine'], palestre.iloc[i]['Longitudine']],
            popup=palestre.iloc[i]['Nome']
        ).add_to(m)
    m.save('templates/mappa.html')
    return render_template("mappa.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)





