import requests

env_url = "https://api-uat-001.ormuco.com"
port = '9292'

def List_imagen(headers):
   return requests.get(url=f"{env_url}:{port}/v2/images", headers=headers).json()['images']

def List_imagen_id(headers,id):
   return requests.get(url=f"{env_url}:{port}/v2/images/{id}", headers=headers).json()