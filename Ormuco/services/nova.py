import requests

port = '8774'

def List_servers(env_url,headers):
   return requests.get(url=f"{env_url}:{port}/v2.1/servers", headers=headers).json()['servers']

def create_servers(env_url,headers, data):
   return requests.post(url=f"{env_url}:{port}/v2.1/servers", headers=headers, json=data).json()['server']

def List_flavors(env_url,headers):
   return requests.get(url=f"{env_url}:{port}/v2.1/flavors", headers=headers).json()['flavors']

def List_flavors_details(env_url,headers):
   return requests.get(url=f"{env_url}:{port}/v2.1/flavors/detail", headers=headers).json()['flavors']

def List_keypairs(env_url,headers):
   keypairs = requests.get(url=f"{env_url}:{port}/v2.1/os-keypairs", headers=headers).json()['keypairs']
   return [i['keypair'] for i in keypairs]