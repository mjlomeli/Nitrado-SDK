from nitrado.nitrado_api import NitradoAPI
from nitrado.service import Service
from nitrado.game_server import GameServer
from nitrado.client import Client


def initialize_client(key=None, url=None):
    NitradoAPI.initialize_client(key, url)

