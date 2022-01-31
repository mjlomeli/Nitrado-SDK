from nitrado_api import NitradoAPI
from service import Service
from game_server import GameServer
from client import Client


def initialize_client(url=None, key=None):
    NitradoAPI.initialize_client(url, key)

