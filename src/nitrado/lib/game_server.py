from nitrado.lib.errors import assert_response_is_ok
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

    def logs_shooter_game_last(self):
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

    def start(self, game):
        path = f'/services/{self.service_id}/gameservers/games/start'
        params = {'game': game}
        return self.__client.post(path=path, params=params)

    def backup_restore(self, folder, backup_id):
        path = f'/services/{self.service_id}/gameservers/backups/gameserver'
        params = {'folder': folder, 'backup': backup_id}
        return self.__client.post(path=path, params=params)

    def download_file(self, file_path):
        path = f'/services/{self.service_id}/gameservers/file_server/download'
        params = {'file': file_path}
        return self.__client.get(path=path, params=params)

    def rename_file(self, file_path, target_path, target_name):
        path = f'/services/{self.service_id}/gameservers/file_server/move'
        params = {'source_path': file_path, 'target_path': target_path, 'target_filename': target_name}
        return self.__client.post(path=path, params=params)

    # def rename_file(self, file_path, new_name):
    #     path = f'/services/{self.service_id}/gameservers/file_server/move'
    #     target_path = '/'.join(file_path.split("/")[:-1])
    #     params = {'source_path': file_path, 'target_path': target_path, 'target_filename': new_name}
    #     return self._client.post(path=path, params=params)

    def donation_history(self, page=0):
        path = f'/services/{self.service_id}/gameservers/boost/history'
        params = {'page': page}
        return self.__client.get(path=path, params=params)

    def donation_settings(self):
        path = f'/services/{self.service_id}/gameservers/boost'
        return self.__client.get(path=path)['data']

    def update_donation_settings(self, enable=True, message=None, welcome_message=None):
        path = f'/services/{self.service_id}/gameservers/boost'
        params = {'enable': enable, 'message': message, 'welcome_message': welcome_message}
        return self.__client.put(path=path, params=params)

    def players(self) -> list:
        path = f'/services/{self.service_id}/gameservers/games/players'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data['players']

    def white_list_player(self, gamertag):
        """
        Player_Management - Add Player to Whitelist
        :param gamertag: Player unique identifier.
        """
        params = {"identifer": gamertag}
        path = f'/services/{self.service_id}/gameservers/games/whitelist'
        return self.__client.put(path=path, params=params)

    def make_admin(self, gamertag):
        """ Must whitelist the player first """
        path = f'/services/{self.service_id}/gameservers/adminlist'
        params = {'identifier': gamertag}
        return self.__client.post(path=path, params=params)

    def details(self) -> dict:
        path = f'/services/{self.service_id}/gameservers'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data['gameserver']

    def restart(self, restart_message: str = None, log_message: str = None):
        path = f'/services/{self.service_id}/gameservers/restart'
        params = {"restart_message": restart_message, "message": log_message}
        response = self.__client.post(path=path, params=params)
        return response.json()['status'] == 'success'

    def stop(self, message=None, stop_message=None):
        try:
            path = f'/services/{self.service_id}/gameservers/stop'
            params = {'message': message, 'stop_message': stop_message}
            response = self.__client.post(path=path, params=params)
            return response.json()['status'] == 'success'
        except Exception as e:
            print(e)
            return False

    def list_backups(self) -> dict:
        path = f'/services/{self.service_id}/gameservers/backups'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data

    def command(self, command):
        path = f'/services/{self.service_id}/gameservers/app_server/command'
        params = {'command': command}
        return self.__client.post(path=path, params=params)

    def ping(self, command):
        path = f'/services/{self.service_id}/gameservers/app_server'
        return self.__client.get(path=path, params={'command': command})

    def restore_database(self, database: str, timestamp: str):
        path = f'/services/{self.service_id}/gameservers/backups/database'
        params = {'database': database, 'timestamp': timestamp}
        return self.__client.post(path=path, params=params)

    def ftp_change_password(self, password: str):
        path = f'/services/{self.service_id}/gameservers/ftp/password'
        params = {'password': password}
        return self.__client.post(path=path, params=params)

    def bookmarks(self):
        path = f'/services/{self.service_id}/gameservers/file_server/bookmarks'
        return self.__client.get(path=path)

    def copy_file(self, source_path: str, target_path: str, target_name: str):
        path = f'/services/{self.service_id}/gameservers/file_server/copy'
        params = {'source_path': source_path, 'target_path': target_path, 'target_name': target_name}
        return self.__client.post(path=path, params=params)

    def create_directory(self, dir_path, name):
        path = f'/services/{self.service_id}/gameservers/file_server/mkdir'
        params = {'path': dir_path, 'name': name}
        return self.__client.post(path=path, params=params)

    def delete_file(self, file_path):
        path = f'/services/{self.service_id}/gameservers/file_server/delete'
        params = {'path': file_path}
        return self.__client.delete(path=path, params=params)

    def list_files(self, dir_path=None, search: str = None):
        path = f'/services/{self.service_id}/gameservers/file_server/list'
        params = {'dir': dir_path, 'search': search}
        response = self.__client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data

    def move_file(self, source_path: str, target_path: str):
        path = f'/services/{self.service_id}/gameservers/file_server/move'
        name = source_path.split('/')[-1]
        params = {'source_path': source_path, 'target_path': target_path, 'target_file_name': name}
        return self.__client.post(path=path, params=params)

    def seek_file(self, file_path: str, offset: int, length: int, mode: str = None):
        path = f'/services/{self.service_id}/gameservers/file_server/seek'
        params = {'file': file_path, 'offset': offset, 'length': length, 'mode': mode}
        return self.__client.get(path=path, params=params)

    def file_size(self, file_path):
        path = f'/services/{self.service_id}/gameservers/file_server/size'
        params = {'file': file_path}
        return self.__client.get(path=path, params=params)

    def duplicate_file(self, source_path, target_path, target_name):
        path = f'/services/{self.service_id}/gameservers/file_server/copy'
        params = {'source_path': source_path, 'target_path': target_path, 'target_name': target_name}
        return self.__client.post(path=path, params=params)

    def files_stat(self, files_paths: list):
        path = f'/services/{self.service_id}/gameservers/file_server/stat'
        params = {'files': files_paths}
        return self.__client.get(path=path, params=params)

    def upload_file(self, target_dir: str, file_name: str):
        path = f'/services/{self.service_id}/gameservers/file_server/upload'
        params = {'path': target_dir, 'file': file_name}
        return self.__client.post(path=path, params=params)

    def list_all_games(self):
        path = '/gameserver/games'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data

    def install_game(self, game: str, modpack: str = None):
        path = f'/services/{self.service_id}/gameservers/games/install'
        params = {'game': game, 'modpack': modpack}
        return self.__client.post(path=path, params=params)

    def list_games(self):
        path = f'/services/{self.service_id}/gameservers/games'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data

    def start_game(self, game: str):
        path = f'/services/{self.service_id}/gameservers/games/start'
        params = {'game': game}
        return self.__client.post(path=path, params=params)

    def uninstall_game(self, game: str):
        path = f'/services/{self.service_id}/gameservers/games/uninstall'
        params = {'game': game}
        return self.__client.delete(path=path, params=params)

    def change_mysql_password(self, password: str):
        path = f'/services/{self.service_id}/gameservers/mysql/password'
        params = {'password': password}
        return self.__client.post(path=path, params=params)

    def reset_mysql_database(self, password: str):
        path = f'/services/{self.service_id}/gameservers/mysql/reset'
        params = {'password': password}
        return self.__client.post(path=path, params=params)

    def install_package(self, package: str, version: str = None):
        path = f'/services/{self.service_id}/gameservers/packages'
        params = {'package': package, 'version': version}
        return self.__client.post(path=path, params=params)

    def list_packages(self):
        path = f'/services/{self.service_id}/gameservers/packages'
        return self.__client.get(path=path)

    def reinstall_package(self, package: str, version: str = None):
        path = f'/services/{self.service_id}/gameservers/packages/reinstall'
        params = {'package': package, 'version': version}
        return self.__client.put(path=path, params=params)

    def uninstall_package(self, package: str):
        path = f'/services/{self.service_id}/gameservers/packages/uninstall'
        params = {'package': package}
        return self.__client.delete(path=path, params=params)

    def resource_usage(self, hours: int = None):
        path = f'/services/{self.service_id}/gameservers/stats'
        params = {'hours': hours}
        return self.__client.get(path=path, params=params)

    def create_settings_sets(self, name: str = None):
        path = f'/services/{self.service_id}/gameservers/settings/sets'
        params = {'name': name}
        return self.__client.post(path=path, params=params)

    def delete_settings_sets(self, set_id: int):
        path = f'/services/{self.service_id}/gameservers/settings/sets/{set_id}'
        return self.__client.delete(path=path)

    def settings_sets(self):
        path = f'/services/{self.service_id}/gameservers/settings/sets'
        sets = self.__client.get(path=path)['data']['sets']
        return [data['data'] for data in sets]

    def restore_settings_sets(self, set_id: int):
        path = f'/services/{self.service_id}/gameservers/settings/sets/{set_id}/restore'
        return self.__client.post(path=path)

    def default_settings(self):
        path = f'/services/{self.service_id}/gameservers/settings/defaults'
        return self.__client.get(path=path)

    def reset_settings(self):
        path = f'/services/{self.service_id}/gameservers/settings'
        return self.__client.delete(path=path)

    def update_settings(self, category: str = None, key: str = None, value: str = None):
        path = f'/services/{self.service_id}/gameservers/settings'
        params = {'category': category, 'key': key, 'value': value}
        return self.__client.post(path=path, params=params)

    def boost_history(self, page: int = 1):
        path = f'/services/{self.service_id}/gameservers/boost/history'
        params = {'page': page}
        response = self.__client.get(path=path, params=params)
        data: dict = response.json()['data']
        return data

    def boost_settings(self):
        path = f'/services/{self.service_id}/gameservers/boost'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data

    def update_boost_settings(self, enable: bool = True, message: str = None, welcome_message: str = None):
        path = f'/services/{self.service_id}/gameservers/boost'
        params = {'enable': enable, 'message': message, 'welcome_message': welcome_message}
        return self.__client.put(path=path, params=params)

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
