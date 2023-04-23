from .lib.client import Client
from .service import Service
from .gameserver import GameServer


def initialize(key: str = None) -> None:
    if key is not None:
        Client.initialize(key)


def services() -> list[Service]:
    return Service.all()


def gameservers() -> list[GameServer]:
    return GameServer.all()


def gameserver_by_service_id(service_id: int) -> GameServer:
    return GameServer.find_by_id(service_id)


def service_by_id(service_id: int) -> Service:
    return Service.find_by_id(service_id)


