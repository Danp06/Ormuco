import requests

port = '9292'

def List_imagen(env_url,headers):
   return requests.get(url=f"{env_url}:{port}/v2/images", headers=headers).json()['images']

def List_imagen_id(env_url,headers,id):
   return requests.get(url=f"{env_url}:{port}/v2/images/{id}", headers=headers).json()