from __future__ import annotations
from ..lib import Client
from ..service import Service
from .host_systems import HostSystem
from .operating_system import OperatingSystem
from .credentials import Credentials
from .players import Players


class GameServer:
    @classmethod
    def find_by_id(cls, service_id: int) -> GameServer:
        response = Client.get(path=f'/services/{service_id}/gameservers')
        data: dict = response.json()['data']['gameserver']
        data['hostsystems'] = HostSystem(service_id, **{
            name: OperatingSystem(service_id, **values)
            for name, values in data['hostsystems'].items()
        })
        data['credentials'] = Credentials(service_id, **data['credentials'])
        return GameServer(**data)

    @classmethod
    def all(cls) -> list[GameServer]:
        game_servers = []
        for service in Service.all():
            game_server = cls.find_by_id(service.id)
            game_servers.append(game_server)
        return game_servers

    def __init__(
            self,
            status: str = None,
            last_status_change: int = None,
            must_be_started: bool = None,
            websocket_token: str = None,
            hostsystems: dict = None,
            username: str = None,
            user_id: int = None,
            service_id: int = None,
            location_id: int = None,
            minecraft_mode: bool = None,
            ip: str = None,
            ipv6: str = None,
            port: int = None,
            query_port: int = None,
            rcon_port: int = None,
            label: str = None,
            type: str = None,
            memory: str = None,
            memory_mb: int = None,
            game: str = None,
            game_human: str = None,
            game_specific: dict = None,
            modpacks: dict = None,
            slots: int = None,
            location: str = None,
            credentials: dict = None,
            settings: dict = None,
            quota: str = None,
            query: dict = None,
            **kwargs
    ):
        self.status = status
        self.last_status_change = last_status_change
        self.must_be_started = must_be_started
        self.websocket_token = websocket_token
        self.hostsystems = hostsystems
        self.username = username
        self.user_id = user_id
        self.service_id = service_id
        self.location_id = location_id
        self.minecraft_mode = minecraft_mode
        self.ip = ip
        self.ipv6 = ipv6
        self.port = port
        self.query_port = query_port
        self.rcon_port = rcon_port
        self.label = label
        self.type = type
        self.memory = memory
        self.memory_mb = memory_mb
        self.game = game
        self.game_human = game_human
        self.game_specific = game_specific
        self.modpacks = modpacks
        self.slots = slots
        self.location = location
        self.credentials = credentials
        self.settings = settings
        self.quota = quota
        self.query = query
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def players(self) -> list[Players]:
        path = f'/services/{self.service_id}/gameservers/games/players'
        response = Client.get(path=path)
        data: dict = response.json()['data']
        return [Players(self.service_id, **player) for player in data['players']]

    def is_gameserver_restorable(self, folder, backup_id) -> bool:
        path = f'/services/{self.service_id}/gameservers/backups/restore_possible'
        params = {'folder': folder, 'backup': backup_id}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def gameserver_restore(self, folder, backup_id) -> bool:
        path = f'/services/{self.service_id}/gameservers/backups/gameserver'
        params = {'folder': folder, 'backup': backup_id}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def white_list_player(self, gamertag: str) -> bool:
        """
        Player_Management - Add Player to Whitelist
        :param gamertag: Player unique identifier.
        """
        params = {"identifier": gamertag}
        path = f'/services/{self.service_id}/gameservers/games/whitelist'
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def admin_list(self) -> list:
        path = f'/services/{self.service_id}/gameservers/games/adminlist'
        response = Client.get(path=path)
        data: dict = response.json()['data']
        return data['adminlist']

    def make_admin(self, gamertag: str) -> bool:
        """ Must whitelist the player first """
        if not self.white_list_player(gamertag):
            return False
        path = f'/services/{self.service_id}/gameservers/games/adminlist'
        params = {'identifier': gamertag}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def details(self) -> dict:
        path = f'/services/{self.service_id}/gameservers'
        response = Client.get(path=path)
        data: dict = response.json()['data']
        return data['gameserver']

    def download_file(self, file_path) -> dict:
        path = f'/services/{self.service_id}/gameservers/file_server/download'
        params = {'file': file_path}
        response = Client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data

    def rename_file(self, file_path, target_path, target_name) -> bool:
        path = f'/services/{self.service_id}/gameservers/file_server/move'
        params = {'source_path': file_path, 'target_path': target_path, 'target_filename': target_name}
        response = Client.post(path=path, params=params)
        data:dict = response.json()
        return response.ok and data['status'] == 'success'

    def start_game(self, game: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/games/start'
        params = {'game': game}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def stop_game(self, message=None, stop_message=None) -> bool:
        path = f'/services/{self.service_id}/gameservers/stop'
        params = {'message': message, 'stop_message': stop_message}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def restart_game(self, restart_message: str = None, log_message: str = None) -> bool:
        path = f'/services/{self.service_id}/gameservers/restart'
        params = {"restart_message": restart_message, "message": log_message}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def install_game(self, game: str, modpack: str = None) -> bool:
        path = f'/services/{self.service_id}/gameservers/games/install'
        params = {'game': game, 'modpack': modpack}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def uninstall_game(self, game: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/games/uninstall'
        params = {'game': game}
        response = Client.delete(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def backups_list(self) -> dict:
        path = f'/services/{self.service_id}/gameservers/backups'
        response = Client.get(path=path)
        data: dict = response.json()['data']
        return data['backups']

    def command(self, command) -> bool:
        path = f'/services/{self.service_id}/gameservers/app_server/command'
        params = {'command': command}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def ping(self, command) -> bool:
        path = f'/services/{self.service_id}/gameservers/app_server'
        response = Client.get(path=path, params={'command': command})
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def restore_database(self, database: str, timestamp: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/backups/database'
        params = {'database': database, 'timestamp': timestamp}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def ftp_change_password(self, password: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/ftp/password'
        params = {'password': password}
        response = Client.post(path=path, params=params)
        data:dict = response.json()
        return response.ok and data['status'] == 'success'

    def bookmarks(self) -> list:
        path = f'/services/{self.service_id}/gameservers/file_server/bookmarks'
        response = Client.get(path=path)
        data: dict = response.json()['data']
        return data['bookmarks']

    def file_copy(self, source_path: str, target_path: str, target_name: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/file_server/copy'
        params = {'source_path': source_path, 'target_path': target_path, 'target_name': target_name}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def create_directory(self, dir_path, name) -> bool:
        path = f'/services/{self.service_id}/gameservers/file_server/mkdir'
        params = {'path': dir_path, 'name': name}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def file_delete(self, file_path) -> bool:
        path = f'/services/{self.service_id}/gameservers/file_server/delete'
        params = {'path': file_path}
        response = Client.delete(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def files_list(self, dir_path=None, search: str = None) -> list:
        path = f'/services/{self.service_id}/gameservers/file_server/list'
        params = {'dir': dir_path, 'search': search}
        response = Client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data['entries']

    def file_move(self, source_path: str, target_path: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/file_server/move'
        name = source_path.split('/')[-1]
        params = {'source_path': source_path, 'target_path': target_path, 'target_file_name': name}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def file_seek(self, file_path: str, offset: int, length: int, mode: str = None) -> dict:
        path = f'/services/{self.service_id}/gameservers/file_server/seek'
        params = {'file': file_path, 'offset': offset, 'length': length, 'mode': mode}
        response = Client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data

    def file_size(self, file_path) -> int:
        path = f'/services/{self.service_id}/gameservers/file_server/size'
        params = {'file': file_path}
        response = Client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data['size']

    def files_stat(self, files_paths: list) -> list:
        path = f'/services/{self.service_id}/gameservers/file_server/stat'
        params = {'files': files_paths}
        response = Client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data['entries']

    def file_download(self, file_path) -> dict:
        path = f'/services/{self.service_id}/gameservers/file_server/download'
        params = {'file': file_path}
        response = Client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data

    def file_upload(self, target_dir: str, file_name: str) -> dict:
        path = f'/services/{self.service_id}/gameservers/file_server/upload'
        params = {'path': target_dir, 'file': file_name}
        response = Client.post(path=path, params=params)
        data: dict = response.json()['data']
        return data

    def list_games(self) -> list:
        path = f'/services/{self.service_id}/gameservers/games'
        response = Client.get(path=path)
        data: dict = response.json()['data']
        return data['games']

    def change_mysql_password(self, password: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/mysql/password'
        params = {'password': password}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def reset_mysql_database(self, password: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/mysql/reset'
        params = {'password': password}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def package_install(self, package: str, version: str = None) -> dict:
        path = f'/services/{self.service_id}/gameservers/packages/install'
        params = {'package': package, 'version': version}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return data

    def packages_list(self) -> dict:
        path = f'/services/{self.service_id}/gameservers/packages'
        response = Client.get(path=path)
        data: dict = response.json()
        return data['packages']

    def package_reinstall(self, package: str, version: str = None) -> dict:
        path = f'/services/{self.service_id}/gameservers/packages/reinstall'
        params = {'package': package, 'version': version}
        response = Client.put(path=path, params=params)
        data: dict = response.json()
        return data

    def package_uninstall(self, package: str) -> dict:
        path = f'/services/{self.service_id}/gameservers/packages/uninstall'
        params = {'package': package}
        response = Client.delete(path=path, params=params)
        data: dict = response.json()
        return data

    def resource_usage(self, hours: int = None) -> dict:
        path = f'/services/{self.service_id}/gameservers/stats'
        params = {'hours': hours}
        response = Client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data['stats']

    def settings_sets_create(self, name: str = None) -> bool:
        path = f'/services/{self.service_id}/gameservers/settings/sets'
        params = {'name': name}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def settings_sets_delete(self, set_id: int) -> bool:
        path = f'/services/{self.service_id}/gameservers/settings/sets/{set_id}'
        response = Client.delete(path=path)
        data: dict = response.json()
        return response.ok and data['success'] == 'success'

    def settings_sets(self) -> list:
        path = f'/services/{self.service_id}/gameservers/settings/sets'
        response = Client.get(path=path)
        data:dict = response.json()['data']
        return data['sets']

    def settings_sets_restore(self, set_id: int) -> bool:
        path = f'/services/{self.service_id}/gameservers/settings/sets/{set_id}/restore'
        response = Client.post(path=path)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def default_settings(self) -> dict:
        path = f'/services/{self.service_id}/gameservers/settings/defaults'
        response = Client.get(path=path)
        data: dict = response.json()['data']
        return data['settings']

    def reset_settings(self) -> bool:
        path = f'/services/{self.service_id}/gameservers/settings'
        response = Client.delete(path=path)
        data: dict = response.json()
        return response.ok and data['status'] == "success"

    def update_settings(self, category: str = None, key: str = None, value: str = None) -> dict:
        path = f'/services/{self.service_id}/gameservers/settings'
        params = {'category': category, 'key': key, 'value': value}
        response = Client.post(path=path, params=params)
        data: dict = response.json()['data']
        return data['settings']

    def boost_history(self, page: int = 1) -> dict:
        path = f'/services/{self.service_id}/gameservers/boost/history'
        params = {'page': page}
        response = Client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data

    def boost_settings(self) -> dict:
        path = f'/services/{self.service_id}/gameservers/boost'
        response = Client.get(path=path)
        data: dict = response.json()['data']
        return data['boosting']

    def boost_settings_update(self, enable: bool = True, message: str = None, welcome_message: str = None) -> dict:
        path = f'/services/{self.service_id}/gameservers/boost'
        params = {'enable': enable, 'message': message, 'welcome_message': welcome_message}
        response = Client.put(path=path, params=params)
        data: dict = response.json()['data']
        return data['boosting']

    def __getitem__(self, item):
        return self.__dict__[item]

    def keys(self):
        return self.__dict__.keys()

    def __repr__(self):
        service_id = f"service_id={repr(self.service_id)}"
        status = f"status={repr(self.status)}"
        slots = f"slots={repr(self.slots)}"
        memory_mb = f"memory_mb={repr(self.memory_mb)}"
        game_human = f"game_human={repr(self.game_human)}"
        params = [s for s in [service_id, status, slots, memory_mb, game_human]]
        return f"<{self.__class__.__name__}({', '.join(params)}, ...)>"

