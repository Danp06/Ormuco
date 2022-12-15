import requests
import utils.specificationForIntance as utils
import services.keystone as keystone
import services.glance as glance
import services.neutron as neutron
import services.nova as nova
import services.cinder as cinder

#Login
env_url = "https://api-uat-001.ormuco.com"

#Services port
ports = {'swift' : '6780'}

token_id = keystone.login(env_url)
headers = {"X-Auth-Token": token_id}

#List Resources
images = glance.List_imagen(env_url,headers)
networks = neutron.List_networks(env_url,headers)
flavors = nova.List_flavors(env_url,headers)
keypairs = nova.List_keypairs(env_url,headers)
security_groups = neutron.List_security_group(env_url,headers)

#i = utils.get_resource_id('web',security_groups)
server_specification = utils.server_specification('ubuntu-18',images,'default',networks,'general.pico.uat.linux'
                                                  ,flavors,'Daniel_Pena',keypairs,'web',security_groups)
print(server_specification)