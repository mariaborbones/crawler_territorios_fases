from flask import Flask,request, render_template, session, redirect,jsonify, json
import atexit
import pandas as pd
import numpy as np
import requests
import json
import os
from bs4 import BeautifulSoup
from flask_swagger_ui import get_swaggerui_blueprint




# encoding: utf-8

app = Flask(__name__, static_url_path='')

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Desescalada-fases-python-REST"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###


# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

def get_info():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    r = requests.get('https://www.lamoncloa.gob.es/covid-19/Paginas/mapa-fases-desescalada.aspx', headers=headers)#, proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content,'lxml')

    fasei=[]
    faseii=[]
    faseiii=[]
    faseiv=[]

    for tag in soup.findAll('h3'):
        if(tag.getText()=='En Fase II'):
            for t in tag.next_siblings:
                print(t.name)
                if(t.name=='h3'):
                    break
                else:
                    faseii.append(t)



        else:
            if(tag.getText()=='En Fase I'):
                fasei=tag.find_next_siblings()
                print(type(fasei))

            else:
                if(tag.getText()=='En Fase III'):
                    faseiii=tag.find_next_siblings()

                else:
                    if(tag.getText()=='En Fase IV'):
                        faseiv=tag.find_next_siblings()


    #Creamos estructura de JSON para almacenar las provincias
    provincias_fase = {'fases':[{
    'fase': 1,
    'provincias': ''
    },
    {
    'fase':2,
    'provincias': ''
    },
    {
    'fase':3,
    'provincias': ''
    },
    {
    'fase':4,
    'provincias': ''
    }]
    ,
    'provincia': 'false'}

    #Leemos las provincias de fase 1

    provincias_fasei = ''
    for zones in fasei:
        s_zones = BeautifulSoup(str(zones),'lxml')
        subzones=s_zones.findAll('span',{"class": "subzone"})

        for s in subzones:
            s= s.text.split('|')
            sz= ''
            for sz in s:
                sz=sz.strip()
                sz= sz.replace('\n',' ')
                sz= sz.replace('\t','')
                sz= sz.replace('\r','')
                provincias_fasei+= ' '+sz +','


    provincias_fase['fases'][0]['provincias']=provincias_fasei

    #Leemos las provincias de fase 2

    provincias_faseii = ''

    for zones in faseii:


        s_zones = BeautifulSoup(str(zones),'lxml')
        subzones=s_zones.findAll('span',{"class": "subzone"})

        for s in subzones:
            s= s.text.split('|')
            sz= ''
            for sz in s:
                sz=sz.strip()
                sz= sz.replace('\n',' ')
                sz= sz.replace('\t','')
                sz= sz.replace('\r','')
                provincias_faseii+= ' '+sz +','
    provincias_fase['fases'][1]['provincias']=provincias_faseii


    #Leemos las provincias de fase 3
    provincias_faseiii = ''
    for zones in faseiii:
        s_zones = BeautifulSoup(str(zones),'lxml')
        subzones=s_zones.findAll('span',{"class": "subzone"})

        for s in subzones:
            s= s.text.split('|')
            sz= ''
            for sz in s:
                sz=sz.strip()
                sz= sz.replace('\n',' ')
                sz= sz.replace('\t','')
                sz= sz.replace('\r','')
                provincias_faseiii+= ' '+sz +','
    provincias_fase['fases'][2]['provincias']=provincias_faseiii

    #Leemos las provincias de fase 4

    provincias_faseiv = ''
    for zones in faseiv:
        s_zones = BeautifulSoup(str(zones),'lxml')
        subzones=s_zones.findAll('span',{"class": "subzone"})

        for s in subzones:
            s= s.text.split('|')
            sz= ''
            for sz in s:
                sz=sz.strip()
                sz= sz.replace('\n',' ')
                sz= sz.replace('\t','')
                sz= sz.replace('\r','')
                provincias_faseiv+= ' '+sz +','
    provincias_fase['fases'][3]['provincias']=provincias_faseiv
    return provincias_fase




@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/fases', methods=['POST'])
def fases_desescalada():
    provincias_fase = get_info()
    return jsonify(provincias_fase)


@app.route('/fases_provincia', methods=['POST'])
def fases_provincia():
    provincias_fase = get_info()
    j = request.json
    print("json= "+str(j))
    city = j['provincia'].lower()
    fase = 0
    #print(params['provincia'])
    for p in provincias_fase['fases']:
        if(p['provincias'].lower().find(city)!=-1):
            print(p['fase'])
            fase = p['fase']


    if(fase > 0):
        return jsonify({'provincia':'true','fase':fase})
    else:
        return jsonify(provincias_fase)





@atexit.register
def shutdown():
    if client:
        client.disconnect()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
