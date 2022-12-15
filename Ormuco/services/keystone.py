import requests

port = '5000'

payload = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "name": "workshop2022@utb.edu.co",
                        "domain": {
                            "name": "Default"
                        },
                        "password": "ILOVECLOUD2022"
                    }
                }
            }
        }
    }

def login(env_url):
    token = requests.post(url=f"{env_url}:{port}/v3/auth/tokens", json=payload)
    return token.json()['token']['id']

def get_project_id(env_url):
    token = requests.post(url=f"{env_url}:{port}/v3/auth/tokens", json=payload)
    return token.json()['token']['project']['id']

