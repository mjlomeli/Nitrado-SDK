import os
import json
from src.nitrado import Client


def pretty_json(data: dict):
    return json.dumps(data, indent=3, sort_keys=True)


if __name__ == "__main__":
    NITRAPI_LIVE_URL = "https://api.nitrado.net/"
    access_token = os.environ.get('NITRADO_KEY')
    api = Client(NITRAPI_LIVE_URL, access_token)
    print('Get Nitrado Ping')
    print(pretty_json(api.get('ping')))
    print("\n")

    print('Get Nitrado Maintenance Status')
    print(pretty_json(api.get('maintenance')))
    print("\n")

    print('Get Nitrado Version')
    print(pretty_json(api.get('version')))
    print("\n")
