import requests

env_url = "https://api-uat-001.ormuco.com"
port ='9696'

def List_networks(headers):
   return requests.get(url=f"{env_url}:{port}/v2.0/networks", headers=headers).json()['networks']

def List_networks_id(headers,id):
   return requests.get(url=f"{env_url}:{port}/v2.0/networks/{id}", headers=headers).json()['network']

def List_address_scopes(headers):
   return requests.get(url=f"{env_url}:{port}/v2.0/address-scopes", headers=headers).json()['address_scopes']

def List_address_scopes(headers,id):
   return requests.get(url=f"{env_url}:{port}/v2.0/address-scopes/{id}", headers=headers).json()['address_scope']

def List_floatingips(headers):
   return requests.get(url=f"{env_url}:{port}/v2.0/floatingips", headers=headers).json()['floatingips']

def List_security_group(headers):
   return requests.get(url=f"{env_url}:{port}/v2.0/security-groups", headers=headers).json()['security_groups']