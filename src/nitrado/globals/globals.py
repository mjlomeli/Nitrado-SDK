from __future__ import annotations
from ..lib import Client
from .maintenance import Maintenance
from .game import Game


class Global:
    @classmethod
    def health_check(cls) -> Global:
        """Health information about the Nitrado API."""
        response = Client.get_without_api_key('/ping')
        kwargs: dict = response.json()
        return cls(**kwargs)

    @classmethod
    def maintenance_status(cls) -> Maintenance:
        response = Client.get_without_api_key('/maintenance')
        kwargs: dict = response.json()
        return Maintenance(**kwargs['data']['maintenance'])

    @classmethod
    def version(cls) -> str:
        """Nitrado API version."""
        response = Client.get_without_api_key('/version')
        kwargs: dict = response.json()
        return cls(**kwargs).message

    @classmethod
    def full_game_list(cls) -> list[Game]:
        """Get all games supported by Nitrado."""
        path = '/gameserver/games'
        response = Client.get_without_api_key(path=path)
        data: dict = response.json()['data']
        return Game.from_data(**data['games'])

    def __init__(self, data: dict = None, message: str = None, status: str = None):
        self.success = status == 'success'
        self.data = data
        self.message = message
        self.status = status

    def __repr__(self):
        params = [f'{k}={repr(v)}' for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"
