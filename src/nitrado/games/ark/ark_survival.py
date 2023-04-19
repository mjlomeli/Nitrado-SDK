from nitrado.lib.game_server import GameServer
from nitrado.lib.service import Service


class ArkSurvivalServer:
    def __init__(self, gameserver: GameServer):
        self.__service = None
        self.gameserver = gameserver

        self.status = gameserver.status
        self.game_name = gameserver.game_human
        self.settings = gameserver.settings
        self.query = gameserver.query
        self.service_id = gameserver.service_id
        self.memory = gameserver.memory  # in MB
        self.slots = gameserver.slots
        self.location = gameserver.location

    def map(self) -> str:
        return self.query['map']

    def player_max(self) -> int:
        return self.query['player_max']

    def player_current(self) -> int:
        return self.query['player_current']

    def players(self) -> list:
        return self.gameserver.players()

    def server_name(self) -> str:
        return self.config()['server-name']

    def service(self) -> Service:
        if self.__service is None:
            self.__service = self.gameserver.service()
        return self.__service

    def log_shooter_game(self) -> str:
        """ Refreshes about every 15+/- minutes """
        return self.gameserver.logs_shooter_game()

    def log_shooter_game_last(self) -> str:
        """ Refreshes about every 15+/- minutes """
        return self.gameserver.logs_shooter_game_last()

    def log_restart(self) -> str:
        """ Refreshes about every 15+/- minutes """
        return self.gameserver.logs_restart()

    def config(self) -> dict:
        return self.gameserver.settings['config']

    def ini(self) -> dict:
        return self.gameserver.settings['gameini']

    def general_settings(self) -> dict:
        return self.gameserver.settings['general']

    def start_param(self) -> dict:
        return self.gameserver.settings['start-param']

    def cluster_id(self) -> str:
        return self.gameserver.cluster_id()

    def start_server(self) -> bool:
        return self.gameserver.start('arkxb')

    def restart_server(self, restart_message: str = None, log_message: str = None) -> bool:
        return self.gameserver.restart(restart_message=restart_message, log_message=log_message)

    def reinstall_server(self) -> bool:
        return self.gameserver.install_game('arkxb', modpack=None)

    def stop_server(self, message: str = None, stop_message: str = None) -> bool:
        return self.gameserver.stop(message=message, stop_message=stop_message)

    def uninstall_game(self) -> bool:
        return self.gameserver.uninstall_game('arkxb')

    def white_list_player(self, gamertag: str) -> bool:
        return self.gameserver.white_list_player(gamertag)

    def admin_list(self) -> list:
        return self.gameserver.admin_list()

    def backups_list(self) -> dict:
        return self.gameserver.backups_list()

    def admin_password(self) -> str:
        return self.config()['admin-password']

    def server_password(self) -> str:
        return self.config()['server-password']

    def spectator_password(self) -> str:
        return self.config()['SpectatorPassword']

    def current_admin_password(self) -> str:
        return self.config()['current-admin-password']

    def __repr__(self):
        service_id = f"service_id={repr(self.service_id)}"
        server_name = f"server_name={repr(self.server_name())}"
        player_current = f"player_current={repr(self.player_current())}"
        status = f"status={repr(self.status)}"
        params = ", ".join([service_id, server_name, player_current, status])
        return f"<ArkSurvival({params})>"


