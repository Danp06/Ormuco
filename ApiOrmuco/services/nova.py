import requests
import utils.specificationForIntance as utils
import services.neutron as neutron

env_url = "https://api-uat-001.ormuco.com"
port = '8774'

def List_servers(headers):
   return requests.get(url=f"{env_url}:{port}/v2.1/servers", headers=headers).json()['servers']

def create_servers(headers,data,nameIntance):
   data = {
        "server": {
            "name": nameIntance,
            "imageRef": data['imagen']['id'],
            "flavorRef": data['flavor']['id'],
            "networks": [{"uuid": data['network']['id']}],
            "key_name": data['keypair']['name'],
            "security_groups": [{"name": data['security_group']['name'] }]
        }
    }
   return requests.post(url=f"{env_url}:{port}/v2.1/servers", headers=headers, json=data)

def List_flavors(headers):
   return requests.get(url=f"{env_url}:{port}/v2.1/flavors", headers=headers).json()['flavors']

def List_flavors_details(headers):
   return requests.get(url=f"{env_url}:{port}/v2.1/flavors/detail", headers=headers).json()['flavors']

def List_keypairs(headers):
   keypairs = requests.get(url=f"{env_url}:{port}/v2.1/os-keypairs", headers=headers).json()['keypairs']
   return [i['keypair'] for i in keypairs]

def asing_server_ip(headers,name_server,servers):
   id_server = utils.get_resource_id(name_server,servers)
   listips = neutron.List_floatingips
   data = {
			"addFloatingIp" : {
					"address": utils.get_ipDown(listips),
					"fixed_address": getPrivateIp(headers,id_server)
			}
	}
   res = requests.post(url=f"{env_url}:{port}/v2.1/servers/{id_server}/action", headers=headers,json=data).json()
   return res

def getPrivateIp(headers,id_server):
   PrivateIp = requests.get(url=f"{env_url}:{port}/v2.1/servers/{id_server}/ips", headers=headers).json()['addresses']['addr']
   return PrivateIp