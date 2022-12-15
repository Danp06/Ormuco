import requests

env_url = "https://api-uat-001.ormuco.com"
port = '8774'

def List_servers(headers):
   return requests.get(url=f"{env_url}:{port}/v2.1/servers", headers=headers).json()['servers']

def create_servers(headers,data,nameIntance,):
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
   return requests.post(url=f"{env_url}:{port}/v2.1/servers", headers=headers, json=data).json()['server']

def List_flavors(headers):
   return requests.get(url=f"{env_url}:{port}/v2.1/flavors", headers=headers).json()['flavors']

def List_flavors_details(headers):
   return requests.get(url=f"{env_url}:{port}/v2.1/flavors/detail", headers=headers).json()['flavors']

def List_keypairs(headers):
   keypairs = requests.get(url=f"{env_url}:{port}/v2.1/os-keypairs", headers=headers).json()['keypairs']
   return [i['keypair'] for i in keypairs]