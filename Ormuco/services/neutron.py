import requests

port ='9696'

def List_networks(env_url,headers):
   return requests.get(url=f"{env_url}:{port}/v2.0/networks", headers=headers).json()['networks']

def List_networks_id(env_url,headers,id):
   return requests.get(url=f"{env_url}:{port}/v2.0/networks/{id}", headers=headers).json()['network']

def List_address_scopes(env_url,headers):
   return requests.get(url=f"{env_url}:{port}/v2.0/address-scopes", headers=headers).json()['address_scopes']

def List_address_scopes(env_url,headers,id):
   return requests.get(url=f"{env_url}:{port}/v2.0/address-scopes/{id}", headers=headers).json()['address_scope']

def List_floatingips(env_url,headers):
   return requests.get(url=f"{env_url}:{port}/v2.0/floatingips", headers=headers).json()['address_scope']

def asign_floatingips(env_url,headers):
   return requests.post(url=f"{env_url}:{port}/v2.0/floatingips", headers=headers).json()['floatingip']

def List_security_group(env_url,headers):
   return requests.get(url=f"{env_url}:{port}/v2.0/security-groups", headers=headers).json()['security_groups']