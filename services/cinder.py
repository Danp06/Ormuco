import requests

env_url = "https://api-uat-001.ormuco.com"
port = '8776'

def List_volumen(headers,project_id):
   return requests.get(url=f"{env_url}:{port}/v3/{project_id}/volumes", headers=headers).json()['volumes']

def create_volumen(headers,project_id):
    data = {
        "volume":
            {
                "name": "test_volume",
                "size": 1
            }
    }
    return requests.post(url=f"{env_url}:{port}/v3/{project_id}/volumes", headers=headers, json=data).json()['volume']