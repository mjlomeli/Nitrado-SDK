from __future__ import annotations
from ...lib import Client
from ...gameserver import GameServer
from ...gameserver import Players
from .query import Query
from .settings import Settings
from .game_specific import GameSpecific
from ...lib import assert_response_is_ok
from ...lib import assert_response_is_json
import requests


class ArkServer:
    @classmethod
    def unofficial_server_list(cls) -> dict:
        """List of all the unofficial servers."""
        response = requests.get("http://arkdedicated.com/xbox/cache/unofficialserverlist.json")
        assert_response_is_ok(response)
        assert_response_is_json(response)
        return response.json()

    @classmethod
    def official_server_list(cls) -> dict:
        """List of all official servers."""
        response = requests.get("http://arkdedicated.com/xbox/cache/officialserverlist.json")
        assert_response_is_ok(response)
        assert_response_is_json(response)
        return response.json()

    @classmethod
    def banned_list(cls) -> list:
        """List of XUID from all banned players."""
        response = requests.get("http://arkdedicated.com/xboxbanlist.txt")
        assert_response_is_ok(response)
        return response.text.split('\r\n')

    @classmethod
    def find_by_id(cls, service_id: int) -> ArkServer:
        """Find an ArkServer by service id."""
        gameserver = GameServer.find_by_id(service_id)
        if gameserver.game != 'arkxb':
            raise Exception(f"Server ID {service_id} is not from Ark: Survival Evolved (Xbox)")
        data: dict = dict(gameserver)
        data['query'] = Query(service_id, **data['query'])
        data['settings'] = Settings.from_data(service_id, **data['settings'])
        data['game_specific'] = GameSpecific.from_data(service_id, **data['game_specific'])
        return ArkServer(gameserver, **data)

    @classmethod
    def all(cls) -> list[ArkServer]:
        """Get all ArkServers."""
        gameservers = []
        for gameserver in GameServer.all():
            if gameserver.game != 'arkxb':
                continue
            data: dict = dict(gameserver)
            data['query'] = Query(gameserver.service_id, **data['query'])
            data['settings'] = Settings.from_data(gameserver.service_id, **data['settings'])
            data['game_specific'] = GameSpecific.from_data(gameserver.service_id, **data['game_specific'])
            gameservers.append(ArkServer(gameserver, **data))
        return gameservers

    @classmethod
    def find_by_gamertag(cls, gamertag: str) -> ArkServer | None:
        for ark in ArkServer.all():
            for player in ark.players():
                if player.name.lower() == gamertag:
                    return ark

    def __init__(
            self,
            gameserver: GameServer,
            query: Query = None,
            settings: Settings = None,
            game_specific: GameSpecific = None,
            **kwargs
    ):
        self.query = query
        self.settings = settings
        self.game_specific = game_specific
        self.service_id = gameserver.service_id
        self.username = gameserver.username
        self.status = gameserver.status
        self.__gameserver = gameserver
        for k, v in kwargs.items():
            self.__dict__[k] = v

    @property
    def map(self) -> str:
        """The map name."""
        return self.query.map

    @property
    def player_max(self) -> int:
        """Maximum players a server can have."""
        return self.query.player_max

    @property
    def player_current(self) -> int:
        """Number of players in the server."""
        return self.query.player_current

    @property
    def admin_password(self) -> str:
        return self.settings.config.admin_password

    @property
    def server_password(self) -> str:
        return self.settings.config.server_password

    @property
    def spectator_password(self) -> str:
        return self.settings.config.spectatorpassword

    @property
    def current_admin_password(self) -> str:
        return self.settings.config.current_admin_password

    def log_shooter_game(self) -> str:
        """The server's logs. Refreshes about every 15+/- minutes """
        path = f'/services/{self.service_id}/gameservers/file_server/download'
        params = {'file': f"/games/{self.username}/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame.log"}
        response = Client.get(path=path, params=params)
        data: dict = response.json()['data']
        url = data['token']['url']
        log_response = requests.get(url)
        assert_response_is_ok(log_response)
        return log_response.text.replace("\r\n", "\n")

    def log_shooter_game_last(self) -> str:
        """The previous server's logs. Refreshes about every 15+/- minutes """
        path = f'/services/{self.service_id}/gameservers/file_server/download'
        params = {'file': f"/games/{self.username}/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame_Last.log"}
        response = Client.get(path=path, params=params)
        data: dict = response.json()['data']
        url = data['token']['url']
        log_response = requests.get(url)
        assert_response_is_ok(log_response)
        return log_response.text.replace("\r\n", "\n")

    def log_restart(self) -> str:
        """The server's system logs. Refreshes about every 15+/- minutes """
        path = f'/services/{self.service_id}/gameservers/file_server/download'
        params = {'file': f"/games/{self.username}/ftproot/restart.log"}
        response = Client.get(path=path, params=params)
        data: dict = response.json()['data']
        url = data['token']['url']
        log_response = requests.get(url)
        assert_response_is_ok(log_response)
        return log_response.text.replace("\r\n", "\n")

    def cluster_id(self) -> str:
        """The cluster id of the server."""
        path = f'/services/{self.service_id}/gameservers/games/arkse/gen_cluster_id'
        response = Client.get(path=path)
        data: dict = response.json()['data']
        return data['clusterid']

    def players(self) -> list[Players]:
        return self.__gameserver.players()

    def start(self) -> bool:
        """Starts the Ark server."""
        return self.__gameserver.start_game('arkxb')

    def restart(self, restart_message: str = None, log_message: str = None) -> bool:
        """Restarts the Ark server."""
        return self.__gameserver.restart_game(restart_message=restart_message, log_message=log_message)

    def reinstall(self) -> bool:
        """Reinstall the Ark server."""
        return self.__gameserver.install_game('arkxb', modpack=None)

    def stop(self, message: str = None, stop_message: str = None) -> bool:
        """Stops the Ark server."""
        return self.__gameserver.stop_game(message=message, stop_message=stop_message)

    def uninstall(self) -> bool:
        """Uninstall the Ark server."""
        return self.__gameserver.uninstall_game('arkxb')

    def __repr__(self):
        service_id = f"service_id={repr(self.service_id)}"
        server_name = f"server_name={repr(self.settings.config.server_name)}"
        player_current = f"player_current={repr(self.player_current)}"
        status = f"status={repr(self.status)}"
        params = ", ".join([service_id, server_name, player_current, status])
        return f"<ArkSurvival({params}, ...)>"


