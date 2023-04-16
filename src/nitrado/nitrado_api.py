from nitrado.lib.errors import assert_response_is_ok, assert_response_is_json
from nitrado.tools import Client
from nitrado.lib import GameServer, Service
import requests
import os


class NitradoAPI:
    NITRADO_API_URL = "https://api.nitrado.net/"

    @classmethod
    def unofficial_server_list(cls) -> dict:
        response = requests.get("http://arkdedicated.com/xbox/cache/unofficialserverlist.json")
        assert_response_is_ok(response)
        assert_response_is_json(response)
        return response.json()

    @classmethod
    def official_server_list(cls) -> dict:
        response = requests.get("http://arkdedicated.com/xbox/cache/officialserverlist.json")
        assert_response_is_ok(response)
        assert_response_is_json(response)
        return response.json()

    @classmethod
    def banned_list(cls) -> list:
        response = requests.get("http://arkdedicated.com/xboxbanlist.txt")
        assert_response_is_ok(response)
        return response.text.split('\r\n')

    def __init__(self, key: str = None, url: str = None):
        self.client = Client(url or NitradoAPI.NITRADO_API_URL, key or os.getenv('NITRADO_KEY'))

    def services(self) -> list:
        response = self.client.get(path='/services')
        data: dict = response.json()['data']
        servers = data['services']
        return [Service(self.client, data) for data in servers]

    def game_servers(self) -> list:
        response = self.client.get(path='/services')
        data: dict = response.json()['data']
        service_ids = [service['id'] for service in data['services']]
        game_servers = []
        for id in service_ids:
            game_server = self.find_game_by_service_id(id)
            game_servers.append(game_server)
        return game_servers
    
    def find_game_by_service_id(self, service_id: str) -> GameServer:
        response = self.client.get(path=f'/services/{service_id}/gameservers')
        data: dict = response.json()['data']
        return GameServer(self.client, data['gameserver'])

    def find_service_by_id(self, service_id: str) -> Service:
        response = self.client.get(path=f'/services/{service_id}')
        data: dict = response.json()['data']
        return Service(self.client, data['service'])

    def health_check(self) -> bool:
        response = self.client.get('/ping')
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def maintenance_status(self) -> dict:
        response = self.client.get('/maintenance')
        data: dict = response.json()['data']
        return data['maintenance']

    def version(self) -> str:
        response = self.client.get('/version')
        data: dict = response.json()
        return data['message']
