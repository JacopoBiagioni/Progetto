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

tabella = pd.read_csv('/workspace/Progetto/csv/Tabella esercizi - Tabella.csv', sep=',')

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/esercizi', methods=['GET'])
def directory():
    return render_template('directory.html')

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

@app.route('/mappa', methods=['GET'])
def mappa():
    return render_template('mappa.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)