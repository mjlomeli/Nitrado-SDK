import client
from client import Client
from game_server import GameServer
from service import Service
import requests
import os

class NitradoAPI:
    NITRADO_API_URL = "https://api.nitrado.net/"
    CLIENT = Client.CLIENT

    @classmethod
    def initialize_client(cls, url, key):
        client = Client(url, key)
        Client.CLIENT = client
        GameServer.CLIENT = client
        Service.CLIENT = client
        NitradoAPI.CLIENT = client

    @classmethod
    def unofficial_server_list(cls):
        url = "http://arkdedicated.com/xbox/cache/unofficialserverlist.json"
        req = requests.get(url)
        return req.json()

    @classmethod
    def official_server_list(cls):
        url = "http://arkdedicated.com/xbox/cache/officialserverlist.json"
        req = requests.get(url)
        return req.json()

    @classmethod
    def banned_list(cls):
        url = "http://arkdedicated.com/xboxbanlist.txt"
        req = requests.get(url)
        return req.text.split('\n')

    def __init__(self, key=None, url=None):
        key = key or os.environ.get("NITRADO_KEY")
        url = url or NitradoAPI.NITRADO_API_URL
        assert key and url, f"params in NitradoApi({key}, {url}) must be provided"
        NitradoAPI.initialize_client(url, key)
        self.services = Service.all()
        self.games = GameServer.all()

    def health_check(self):
        return NitradoAPI.CLIENT.get('ping')

    def maintenance_status(self):
        return NitradoAPI.CLIENT.get('maintenance')

    def current_api_version(self):
        return NitradoAPI.CLIENT.get('version')


if __name__ == '__main__':
    import json

    def print_json(data: dict):
        print(json.dumps(data, indent=3, sort_keys=True))

    api = NitradoAPI()
    print_json(api.health_check())
    print_json(api.maintenance_status())
    print_json(api.current_api_version())

    for service in api.services:
        print(service)

    for game in api.games:
        print(game)

