import requests

env_url = "https://api-uat-001.ormuco.com"
port = '5000'

def payload(user,password):
    return {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "name": user,
                        "domain": {
                            "name": "Default"
                        },
                        "password": password
                    }
                }
            }
        }
    }

def login(user,password):
    token = requests.post(url=f"{env_url}:{port}/v3/auth/tokens", json=payload(user,password))
    return {"X-Auth-Token": token.json()['token']['id']}

def get_project_id(user,password):
    token = requests.post(url=f"{env_url}:{port}/v3/auth/tokens", json=payload(user,password))
    return token.json()['token']['project']['id']

