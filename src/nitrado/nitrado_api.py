from nitrado.tools import Client
from nitrado.lib import GameServer, Service
import requests
from requests import RequestException
import os


def assert_success(response):
    if not response:
        return
    if 'status' not in response or response['status'] != 'success':
        raise AssertionError(f"API returned: {response}")


class NitradoAPI:
    NITRADO_API_URL = "https://api.nitrado.net/"

    @classmethod
    def unofficial_server_list(cls):
        req = requests.get("http://arkdedicated.com/xbox/cache/unofficialserverlist.json")
        if not req.ok:
            code = req.status_code
            reason = req.reason
            raise RequestException(f"Url error => {code} {reason} for:", req.url)
        return req.json()

    @classmethod
    def official_server_list(cls):
        req = requests.get("http://arkdedicated.com/xbox/cache/officialserverlist.json")
        if not req.ok:
            code = req.status_code
            reason = req.reason
            raise RequestException(f"Url error => {code} {reason} for:", req.url)
        return req.json()

    @classmethod
    def banned_list(cls):
        req = requests.get("http://arkdedicated.com/xboxbanlist.txt")
        return req.text.split('\r\n')

    def __init__(self, key: str or None = None, url: str or None = None):
        key = key or os.getenv("NITRADO_KEY")
        url = url or NitradoAPI.NITRADO_API_URL
        self.__client = Client(url or NitradoAPI.NITRADO_API_URL, key)

    def services(self):
        resp_servers = self.__client.get(path='services')
        assert_success(resp_servers)
        servers = resp_servers['data']['services']
        return [Service(self.__client, data) for data in servers]

    def game_servers(self):
        resp = self.__client.get(path='services')
        assert_success(resp)
        service_ids = [serv['id'] for serv in resp['data']['services']]
        games = []
        for serv_id in service_ids:
            game_server = self.find_game_by_service_id(serv_id)
            games.append(game_server)
        return games

    def find_game_by_service_id(self, service_id: str):
        path = ['services', service_id, 'gameservers']
        resp = self.__client.get(path=path)
        assert_success(resp)
        data = resp['data']['gameserver']
        return GameServer(self.__client, data)

    def find_service_by_id(self, service_id: str):
        path = ['services', service_id]
        resp = self.__client.get(path=path)
        assert_success(resp)
        data = resp['data']['services']
        return Service(self.__client, data)

    def health_check(self):
        resp = self.__client.get('ping')
        assert_success(resp)
        return resp['message']

    def maintenance_status(self):
        resp = self.__client.get('maintenance')
        assert_success(resp)
        return resp['data']['maintenance']

    def version(self):
        resp = self.__client.get('version')
        assert_success(resp)
        return resp['message']
