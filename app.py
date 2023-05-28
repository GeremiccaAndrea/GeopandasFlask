from flask import Flask, request, render_template
app = Flask(__name__)

import geopandas as gpd
import pandas as pd 
import matplotlib.pyplot as plt 
import os 
import contextily as ctx
comuni = gpd.read_file('comuni/Com01012022_WGS84.dbf')

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/Es1')
def Es1():
    utente = request.args.get('comune')
    comune_utente = comuni[comuni['COMUNE'] == utente]
    ax = comune_utente.to_crs(3857).plot(facecolor = 'None')
    ctx.add_basemap(ax)
    #servono per creare l'immagine
    dir = "static/images"
    file_name = "graf.png"
    save_path = os.path.join(dir, file_name) 
    plt.savefig(save_path, dpi = 150)
    return render_template('risultato.html')




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)