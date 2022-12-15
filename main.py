import requests
import utils.specificationForIntance as utils
import services.keystone as keystone
import services.glance as glance
import services.neutron as neutron
import services.nova as nova
import services.cinder as cinder

#Login
env_url = "https://api-uat-001.ormuco.com"
user = "workshop2022@utb.edu.co"
password = "ILOVECLOUD2022"

#Services port
token_id = keystone.login(user,password)
headers = {"X-Auth-Token": token_id}

#List Resources
images = glance.List_imagen(headers)
networks = neutron.List_networks(headers)
flavors = nova.List_flavors(headers)
keypairs = nova.List_keypairs(headers)
security_groups = neutron.List_security_group(headers)

server_specification = utils.server_specification('ubuntu-18',images,'default',networks,'general.pico.uat.linux'
                                                  ,flavors,'Daniel_Pena',keypairs,'web',security_groups)

instance = nova.create_servers(headers,server_specification,'Daniel_instance')