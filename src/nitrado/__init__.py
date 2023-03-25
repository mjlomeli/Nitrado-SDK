from nitrado.nitrado_api import NitradoAPI
from nitrado.lib.service import Service
from nitrado.lib.game_server import GameServer
from nitrado.tools import Client



__all__ = ['NitradoAPI', 'Service', 'GameServer', 'Client', 'initialize_client']


def initialize_client(key=None, url=None):
    NitradoAPI.initialize_client(key, url)
