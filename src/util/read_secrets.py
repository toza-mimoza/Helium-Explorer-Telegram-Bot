import os
import json
def read_secrets() -> dict:
    filename = os.path.join('.secret/secrets.json')
    try:
        with open(filename, mode='r') as secrets_file:
            return json.load(secrets_file)
    except FileNotFoundError:
        return {}