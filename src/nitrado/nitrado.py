from .lib.client import Client
from .service import Service
from .gameserver import GameServer


class Nitrado:

    @classmethod
    def initialize(cls, key: str = None) -> None:
        if key is not None:
            Client.initialize(key)

    @classmethod
    def services(cls) -> list[Service]:
        return Service.all()

    @classmethod
    def gameservers(self) -> list[GameServer]:
        return GameServer.all()

    @classmethod
    def gameserver_by_service_id(self, service_id: int) -> GameServer:
        return GameServer.find_by_id(service_id)

    @classmethod
    def service_by_id(self, service_id: int) -> Service:
        return Service.find_by_id(service_id)


