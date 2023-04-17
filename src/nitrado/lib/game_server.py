from nitrado.lib.errors import assert_response_is_ok
from nitrado.lib.service import Service
from nitrado.tools import Client
import requests
from pathlib import Path
import json


class GameServer:
    def __init__(self, client: Client, data: dict):
        self.__client = client
        self.__data = data

        self.status = None
        self.last_status_change = None
        self.must_be_started = None
        self.websocket_token = None
        self.hostsystems = None
        self.username = None
        self.user_id = None
        self.service_id = None
        self.location_id = None
        self.minecraft_mode = None
        self.ip = None
        self.ipv6 = None
        self.port = None
        self.query_port = None
        self.rcon_port = None
        self.label = None
        self.type = None
        self.memory = None
        self.memory_mb = None
        self.game = None
        self.game_human = None
        self.game_specific = None
        self.modpacks = None
        self.slots = None
        self.location = None
        self.credentials = None
        self.settings = None
        self.quota = None
        self.query = None
        for k, v in data.items():
            self.__dict__[k] = v

    def service(self) -> Service:
        response = self.__client.get(path=f'/services/{self.service_id}')
        data: dict = response.json()['data']
        return Service(self.__client, data['service'])

    def cluster_id(self) -> str:
        path = f'/services/{self.service_id}/gameservers/games/arkse/gen_cluster_id'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data['clusterid']

    def logs_shooter_game(self) -> str:
        path = f'/services/{self.service_id}/gameservers/file_server/download'
        params = {'file': f"/games/{self.username}/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame.log"}
        response = self.__client.get(path=path, params=params)
        data: dict = response.json()['data']
        url = data['token']['url']
        log_response = requests.get(url)
        assert_response_is_ok(log_response)
        return log_response.text.replace("\r\n", "\n")

    def logs_restart(self) -> str:
        path = f'/services/{self.service_id}/gameservers/file_server/download'
        params = {'file': f"/games/{self.username}/ftproot/restart.log"}
        response = self.__client.get(path=path, params=params)
        data: dict = response.json()['data']
        url = data['token']['url']
        log_response = requests.get(url)
        assert_response_is_ok(log_response)
        return log_response.text.replace("\r\n", "\n")

    def logs_shooter_game_last(self) -> str:
        path = f'/services/{self.service_id}/gameservers/file_server/download'
        params = {'file': f"/games/{self.username}/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame_Last.log"}
        response = self.__client.get(path=path, params=params)
        data: dict = response.json()['data']
        url = data['token']['url']
        log_response = requests.get(url)
        assert_response_is_ok(log_response)
        return log_response.text.replace("\r\n", "\n")

    def logs_download(self, directory: str = None) -> None:
        location = Path(directory or Path.cwd())
        if not location.is_dir():
            raise NotADirectoryError(f"Directory does not exist: {directory}")
        with open(location / Path('shooter_games.txt'), 'w') as w:
            w.write(self.logs_shooter_game())
        with open(location / Path('shooter_games_last.txt'), 'w') as w:
            w.write(self.logs_shooter_game_last())
        with open(location / Path('restart.txt'), 'w') as w:
            w.write(self.logs_restart())

    def start(self, game: str) -> bool:
        """ :param game: Provide the Folder Short of the specific game. """
        path = f'/services/{self.service_id}/gameservers/games/start'
        params = {'game': game}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def is_gameserver_restorable(self, folder, backup_id) -> bool:
        path = f'/services/{self.service_id}/gameservers/backups/restore_possible'
        params = {'folder': folder, 'backup': backup_id}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def gameserver_restore(self, folder, backup_id) -> bool:
        path = f'/services/{self.service_id}/gameservers/backups/gameserver'
        params = {'folder': folder, 'backup': backup_id}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def download_file(self, file_path) -> dict:
        path = f'/services/{self.service_id}/gameservers/file_server/download'
        params = {'file': file_path}
        response = self.__client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data

    def rename_file(self, file_path, target_path, target_name) -> bool:
        path = f'/services/{self.service_id}/gameservers/file_server/move'
        params = {'source_path': file_path, 'target_path': target_path, 'target_filename': target_name}
        response = self.__client.post(path=path, params=params)
        data:dict = response.json()
        return response.ok and data['status'] == 'success'

    # def rename_file(self, file_path, new_name):
    #     path = f'/services/{self.service_id}/gameservers/file_server/move'
    #     target_path = '/'.join(file_path.split("/")[:-1])
    #     params = {'source_path': file_path, 'target_path': target_path, 'target_filename': new_name}
    #     return self._client.post(path=path, params=params)

    def donation_history(self, page=0) -> dict:
        path = f'/services/{self.service_id}/gameservers/boost/history'
        params = {'page': page}
        response = self.__client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data

    def donation_settings(self) -> dict:
        path = f'/services/{self.service_id}/gameservers/boost'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data['boosting']

    def update_donation_settings(self, enable=True, message=None, welcome_message=None) -> dict:
        path = f'/services/{self.service_id}/gameservers/boost'
        params = {'enable': enable, 'message': message, 'welcome_message': welcome_message}
        response = self.__client.put(path=path, params=params)
        data: dict = response.json()
        return data['boosting']

    def players(self) -> list:
        path = f'/services/{self.service_id}/gameservers/games/players'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data['players']

    def white_list_player(self, gamertag: str) -> bool:
        """
        Player_Management - Add Player to Whitelist
        :param gamertag: Player unique identifier.
        """
        params = {"identifer": gamertag}
        path = f'/services/{self.service_id}/gameservers/games/whitelist'
        response = self.__client.put(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def admin_list(self) -> list:
        path = f'/services/{self.service_id}/gameservers/games/adminlist'
        response = self.__client.post(path=path)
        data: dict = response.json()['data']
        return data['adminlist']

    def admin_make(self, gamertag):
        """ Must whitelist the player first """
        path = f'/services/{self.service_id}/gameservers/adminlist'
        params = {'identifier': gamertag}
        return self.__client.post(path=path, params=params)

    def details(self) -> dict:
        path = f'/services/{self.service_id}/gameservers'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data['gameserver']

    def restart(self, restart_message: str = None, log_message: str = None) -> bool:
        path = f'/services/{self.service_id}/gameservers/restart'
        params = {"restart_message": restart_message, "message": log_message}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def stop(self, message=None, stop_message=None) -> bool:
        path = f'/services/{self.service_id}/gameservers/stop'
        params = {'message': message, 'stop_message': stop_message}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def backups_list(self) -> dict:
        path = f'/services/{self.service_id}/gameservers/backups'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data['backups']

    def command(self, command) -> bool:
        path = f'/services/{self.service_id}/gameservers/app_server/command'
        params = {'command': command}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def ping(self, command) -> bool:
        path = f'/services/{self.service_id}/gameservers/app_server'
        response = self.__client.get(path=path, params={'command': command})
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def restore_database(self, database: str, timestamp: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/backups/database'
        params = {'database': database, 'timestamp': timestamp}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def ftp_change_password(self, password: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/ftp/password'
        params = {'password': password}
        response = self.__client.post(path=path, params=params)
        data:dict = response.json()
        return response.ok and data['status'] == 'success'

    def bookmarks(self) -> list:
        path = f'/services/{self.service_id}/gameservers/file_server/bookmarks'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data['bookmarks']

    def file_copy(self, source_path: str, target_path: str, target_name: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/file_server/copy'
        params = {'source_path': source_path, 'target_path': target_path, 'target_name': target_name}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def create_directory(self, dir_path, name) -> bool:
        path = f'/services/{self.service_id}/gameservers/file_server/mkdir'
        params = {'path': dir_path, 'name': name}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def file_delete(self, file_path) -> bool:
        path = f'/services/{self.service_id}/gameservers/file_server/delete'
        params = {'path': file_path}
        response = self.__client.delete(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def files_list(self, dir_path=None, search: str = None) -> list:
        path = f'/services/{self.service_id}/gameservers/file_server/list'
        params = {'dir': dir_path, 'search': search}
        response = self.__client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data['entries']

    def file_move(self, source_path: str, target_path: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/file_server/move'
        name = source_path.split('/')[-1]
        params = {'source_path': source_path, 'target_path': target_path, 'target_file_name': name}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def file_seek(self, file_path: str, offset: int, length: int, mode: str = None) -> dict:
        path = f'/services/{self.service_id}/gameservers/file_server/seek'
        params = {'file': file_path, 'offset': offset, 'length': length, 'mode': mode}
        response = self.__client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data

    def file_size(self, file_path) -> int:
        path = f'/services/{self.service_id}/gameservers/file_server/size'
        params = {'file': file_path}
        response = self.__client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data['size']

    def file_copy(self, source_path, target_path, target_name) -> bool:
        path = f'/services/{self.service_id}/gameservers/file_server/copy'
        params = {'source_path': source_path, 'target_path': target_path, 'target_name': target_name}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def files_stat(self, files_paths: list) -> list:
        path = f'/services/{self.service_id}/gameservers/file_server/stat'
        params = {'files': files_paths}
        response = self.__client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data['entries']

    def file_download(self, file_path) -> dict:
        path = f'/services/{self.service_id}/gameservers/file_server/download'
        params = {'file': file_path}
        response = self.__client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data

    def file_upload(self, target_dir: str, file_name: str) -> dict:
        path = f'/services/{self.service_id}/gameservers/file_server/upload'
        params = {'path': target_dir, 'file': file_name}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()['data']
        return data

    def full_game_list(self) -> dict:
        path = '/gameserver/games'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data['games']

    def install_game(self, game: str, modpack: str = None) -> bool:
        path = f'/services/{self.service_id}/gameservers/games/install'
        params = {'game': game, 'modpack': modpack}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def list_games(self) -> list:
        path = f'/services/{self.service_id}/gameservers/games'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data['games']

    def start_game(self, game: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/games/start'
        params = {'game': game}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def uninstall_game(self, game: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/games/uninstall'
        params = {'game': game}
        response = self.__client.delete(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def change_mysql_password(self, password: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/mysql/password'
        params = {'password': password}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def reset_mysql_database(self, password: str) -> bool:
        path = f'/services/{self.service_id}/gameservers/mysql/reset'
        params = {'password': password}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def package_install(self, package: str, version: str = None) -> dict:
        path = f'/services/{self.service_id}/gameservers/packages/install'
        params = {'package': package, 'version': version}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return data

    def packages_list(self) -> dict:
        path = f'/services/{self.service_id}/gameservers/packages'
        response = self.__client.get(path=path)
        data: dict = response.json()
        return data['packages']

    def package_reinstall(self, package: str, version: str = None) -> dict:
        path = f'/services/{self.service_id}/gameservers/packages/reinstall'
        params = {'package': package, 'version': version}
        response = self.__client.put(path=path, params=params)
        data: dict = response.json()
        return data

    def package_uninstall(self, package: str) -> dict:
        path = f'/services/{self.service_id}/gameservers/packages/uninstall'
        params = {'package': package}
        response = self.__client.delete(path=path, params=params)
        data: dict = response.json()
        return data

    def resource_usage(self, hours: int = None) -> dict:
        path = f'/services/{self.service_id}/gameservers/stats'
        params = {'hours': hours}
        response = self.__client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data['stats']

    def settings_sets_create(self, name: str = None) -> bool:
        path = f'/services/{self.service_id}/gameservers/settings/sets'
        params = {'name': name}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def settings_sets_delete(self, set_id: int) -> bool:
        path = f'/services/{self.service_id}/gameservers/settings/sets/{set_id}'
        response = self.__client.delete(path=path)
        data: dict = response.json()
        return response.ok and data['success'] == 'success'

    def settings_sets(self) -> list:
        path = f'/services/{self.service_id}/gameservers/settings/sets'
        response = self.__client.get(path=path)
        data:dict = response.json()['data']
        return data['sets']

    def settings_sets_restore(self, set_id: int) -> bool:
        path = f'/services/{self.service_id}/gameservers/settings/sets/{set_id}/restore'
        response = self.__client.post(path=path)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def default_settings(self) -> dict:
        path = f'/services/{self.service_id}/gameservers/settings/defaults'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data

    def reset_settings(self) -> bool:
        path = f'/services/{self.service_id}/gameservers/settings'
        response = self.__client.delete(path=path)
        data: dict = response.json()
        return response.ok and data['status'] == "success"

    def update_settings(self, category: str = None, key: str = None, value: str = None) -> dict:
        path = f'/services/{self.service_id}/gameservers/settings'
        params = {'category': category, 'key': key, 'value': value}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()['data']
        return data['settings']

    def boost_history(self, page: int = 1) -> dict:
        path = f'/services/{self.service_id}/gameservers/boost/history'
        params = {'page': page}
        response = self.__client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data

    def boost_settings(self) -> dict:
        path = f'/services/{self.service_id}/gameservers/boost'
        response = self.__client.get(path=path)
        data: dict = response.json()
        return data['boosting']

    def boost_settings_update(self, enable: bool = True, message: str = None, welcome_message: str = None) -> dict:
        path = f'/services/{self.service_id}/gameservers/boost'
        params = {'enable': enable, 'message': message, 'welcome_message': welcome_message}
        response = self.__client.put(path=path, params=params)
        data: dict = response.json()
        return data['boosting']

    def __contains__(self, item):
        return item in self.__data

    def __getitem__(self, item):
        return self.__data[item]

    def keys(self):
        return self.__data.keys()

    def __iter__(self):
        return iter(self.__data)

    def __repr__(self):
        service_id = f"service_id={repr(self.service_id)}"
        location = f"location={repr(self.location)}"
        slots = f"slots={repr(self.slots)}"
        game_human = f"game_human={repr(self.game_human)}"
        ip = f"ip={repr(self.ip)}"
        params = ", ".join([service_id, location, slots, ip, game_human])
        return f"<GameServer({params})>"

    def __str__(self):
        return json.dumps(self.__data, indent=3)
