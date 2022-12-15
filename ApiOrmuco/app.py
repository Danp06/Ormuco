from flask import Flask, render_template
import requests
import utils.specificationForIntance as utils
import services.keystone as keystone
import services.glance as glance
import services.neutron as neutron
import services.nova as nova
import services.cinder as cinder

app = Flask(__name__)

env_url = "https://api-uat-001.ormuco.com"
user = "workshop2022@utb.edu.co"
password = "ILOVECLOUD2022"
headers = keystone.login(user,password)
nameServer = 'DefaultServer_Daniel'

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/images')
def list_images():
    imagen = glance.List_imagen(headers)
    return imagen

@app.route('/networks')
def list_networks():
    network = neutron.List_networks(headers)
    return network

@app.route('/keypairs')
def list_keypairs():
    keypair = nova.List_flavors(headers)
    return keypair

@app.route('/flavors')
def list_flavors():
    flavor = nova.List_keypairs(headers)
    return flavor

@app.route('/security_groups')
def list_security_groups():
    security_group = neutron.List_security_group(headers)
    return security_group

@app.route('/servers')
def list_servers():
    return nova.List_servers(headers)

@app.route('/info')
def info():
    data = {"imagen":list_images(),
            "network":list_networks(),
            "keypair":list_keypairs(),
            "flavor":list_flavors(),
            "security_group":list_security_groups()}
    return data

@app.route('/images/<id_imagen>')
def getimage(id_imagen):
    return utils.get_resource(id_imagen,info()['imagen'])

@app.route('/create_servers')
def createServer():
    specification = utils.server_specification(info())
    response = nova.create_servers(headers,specification,nameServer)
    return response


if __name__ == '__main__':
    app.run(debug=True, port=8000)