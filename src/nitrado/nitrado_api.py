from nitrado.lib.errors import assert_response_is_ok, assert_response_is_json
from nitrado.lib.client import Client
from nitrado.lib import GameServer, Service
from nitrado.games.ark import ArkSurvivalAPI
import requests
import os


class NitradoAPI:

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

    def __init__(self, key: str = None):
        if key is not None:
            Client.initialize(key)

    def services(self) -> list[Service]:
        response = Client.get(path='/services')
        data: dict = response.json()['data']
        servers = data['services']
        return [Service(data) for data in servers]

    def game_servers(self) -> list[GameServer]:
        response = Client.get(path='/services')
        data: dict = response.json()['data']
        service_ids = [service['id'] for service in data['services']]
        game_servers = []
        for id in service_ids:
            game_server = self.find_game_by_service_id(id)
            game_servers.append(game_server)
        return game_servers

    def ark_xbox_servers(self) -> list[ArkSurvivalAPI]:
        games = []
        for game in self.game_servers():
            if game.game == 'arkxb':
                games.append(ArkSurvivalAPI(game))
        return games

    def find_game_by_service_id(self, service_id: str) -> GameServer:
        response = Client.get(path=f'/services/{service_id}/gameservers')
        data: dict = response.json()['data']
        return GameServer(data['gameserver'])

    def find_service_by_id(self, service_id: str) -> Service:
        response = Client.get(path=f'/services/{service_id}')
        data: dict = response.json()['data']
        return Service(data['service'])


