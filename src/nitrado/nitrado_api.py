from nitrado.client import Client
from nitrado.game_server import GameServer
from nitrado.service import Service
import requests
import os


class NitradoAPI:
    NITRADO_API_URL = "https://api.nitrado.net/"
    CLIENT = Client.CLIENT

    @classmethod
    def initialize_client(cls, key=None, url=None):
        if not Client.CLIENT or GameServer.CLIENT or Service.CLIENT or NitradoAPI.CLIENT:
            key = key or os.environ.get("NITRADO_KEY")
            url = url or NitradoAPI.NITRADO_API_URL
            assert key and url or NitradoAPI.CLIENT, f"The url and api key must be provided: url=>{url}, key=>{key}"
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
        return req.text.split('\r\n')

    def __init__(self, key=None, url=None):
        NitradoAPI.initialize_client(key, url)
        self.services = Service.all()
        self.game_servers = GameServer.all()

    def health_check(self):
        return NitradoAPI.CLIENT.get('ping')['message']

    def maintenance_status(self):
        return NitradoAPI.CLIENT.get('maintenance')['data']

    def version(self):
        return NitradoAPI.CLIENT.get('version')['message']



