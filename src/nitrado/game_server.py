from nitrado.client import Client
import requests
from pathlib import Path, WindowsPath


def assert_success(response):
    if not response:
        return
    if 'status' not in response or response['status'] != 'success':
        raise AssertionError(f"API returned: {response}")


def assert_request(req):
    if not req.ok:
        code = req.status_code
        reason = req.reason
        raise requests.RequestException(f"Url error => {code} {reason} for:", req.url)


class GameServer:
    CLIENT = Client.CLIENT

    @classmethod
    def find_by_id(cls, service_id):
        path = ['services', service_id, 'gameservers']
        resp = GameServer.CLIENT.get(path=path)
        assert_success(resp)
        data = resp['data']['gameserver']
        return GameServer(data)

    @classmethod
    def all(cls):
        games = []
        resp = GameServer.CLIENT.get(path='services')
        assert_success(resp)
        service_ids = [serv['id'] for serv in resp['data']['services']]
        for serv_id in service_ids:
            games.append(GameServer.find_by_id(serv_id))
        return games

    def __init__(self, data):
        """
        :param service_id: the gameserver id on nitrado
        """
        self.status = data['status'] if 'status' in data else None
        self.last_status_change = data['last_status_change'] if 'last_status_change' in data else None
        self.must_be_started = data['must_be_started'] if 'must_be_started' in data else None
        self.websocket_token = data['websocket_token'] if 'websocket_token' in data else None
        self.hostsystems = data['hostsystems'] if 'hostsystems' in data else None
        self.username = data['username'] if 'username' in data else None
        self.user_id = data['user_id'] if 'user_id' in data else None
        self.service_id = data['service_id'] if 'service_id' in data else None
        self.location_id = data['location_id'] if 'location_id' in data else None
        self.minecraft_mode = data['minecraft_mode'] if 'minecraft_mode' in data else None
        self.ip = data['ip'] if 'ip' in data else None
        self.ipv6 = data['ipv6'] if 'ipv6' in data else None
        self.port = data['port'] if 'port' in data else None
        self.query_port = data['query_port'] if 'query_port' in data else None
        self.rcon_port = data['rcon_port'] if 'rcon_port' in data else None
        self.label = data['label'] if 'label' in data else None
        self.type = data['type'] if 'type' in data else None
        self.memory = data['memory'] if 'memory' in data else None
        self.memory_mb = data['memory_mb'] if 'memory_mb' in data else None
        self.game = data['game'] if 'game' in data else None
        self.game_human = data['game_human'] if 'game_human' in data else None
        self.game_specific = data['game_specific'] if 'game_specific' in data else None
        self.modpacks = data['modpacks'] if 'modpacks' in data else None
        self.slots = data['slots'] if 'slots' in data else None
        self.location = data['location'] if 'location' in data else None
        self.credentials = data['credentials'] if 'credentials' in data else None
        self.settings = data['settings'] if 'settings' in data else None
        self.quota = data['quota'] if 'quota' in data else None
        self.query = data['query'] if 'query' in data else None

    def cluster_id(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'games', 'arkse', 'gen_cluster_id']
        resp = GameServer.CLIENT.get(path=path)
        assert_success(resp)
        return resp['data']['clusterid']

    def logs_shooter_game(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'download']
        params = {'file': f"/games/{self.username}/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame.log"}
        resp_url = GameServer.CLIENT.get(path=path, params=params)
        assert_success(resp_url)
        url = resp_url['data']['token']['url']
        req = requests.get(url)
        assert_request(req)
        return req.text.replace("\r\n", "\n")

    def logs_restart(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'download']
        params = {'file': f"/games/{self.username}/ftproot/restart.log"}
        resp_url = GameServer.CLIENT.get(path=path, params=params)
        assert_success(resp_url)
        url = resp_url['data']['token']['url']
        req = requests.get(url)
        assert_request(req)
        return req.text.replace("\r\n", "\n")

    def logs_shooter_game_last(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'download']
        params = {'file': f"/games/{self.username}/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame_Last.log"}
        resp_url = GameServer.CLIENT.get(path=path, params=params)
        assert_success(resp_url)
        url = resp_url['data']['token']['url']
        req = requests.get(url)
        assert_request(req)
        return req.text.replace("\r\n", "\n")

    def logs_download(self, directory=Path.cwd()):
        assert type(directory) == str or type(directory) == Path or type(
            directory) == WindowsPath, "Path provided must be of type string"
        location = Path(directory)
        if not location.is_dir():
            raise FileNotFoundError(f"The directory provided does not exist: {directory}")
        with open(location / Path('shooter_games.txt'), 'w') as w:
            w.write(self.logs_shooter_game())
        with open(location / Path('shooter_games_last.txt'), 'w') as w:
            w.write(self.logs_shooter_game_last())
        with open(location / Path('restart.txt'), 'w') as w:
            w.write(self.logs_restart())

    def start(self, game):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'games', 'start']
        params = {'game': game}
        return GameServer.CLIENT.post(path=path, params=params)

    def backup_restore(self, folder, backup_id):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'backups', 'gameserver']
        params = {'folder': folder, 'backup': backup_id}
        return GameServer.CLIENT.post(path=path, params=params)

    def download_file(self, file_path):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'download']
        params = {'path': file_path}
        return GameServer.CLIENT.get(path=path, params=params)

    def rename_file(self, file_path, target_path, target_name):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'move']
        params = {'source_path': file_path, 'target_path': target_path, 'target_filename': target_name}
        return GameServer.CLIENT.post(path=path, params=params)

    # def rename_file(self, file_path, new_name):
    #     path = ['services', self.service_id, 'gameservers', 'file_server', 'move']
    #     target_path = '/'.join(file_path.split("/")[:-1])
    #     params = {'source_path': file_path, 'target_path': target_path, 'target_filename': new_name}
    #     return self._client.post(path=path, params=params)

    def donation_history(self, page=0):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'boost', 'history']
        params = {'page': page}
        return GameServer.CLIENT.get(path=path, params=params)

    def donation_settings(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'boost']
        return GameServer.CLIENT.get(path=path)['data']

    def update_donation_settings(self, enable=True, message=None, welcome_message=None):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'boost']
        params = {'enable': enable, 'message': message, 'welcome_message': welcome_message}
        return GameServer.CLIENT.put(path=path, params=params)

    def players(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ["services", self.service_id, "gameservers", "games", "players"]
        resp_players = GameServer.CLIENT.get(path=path)
        assert_success(resp_players)
        return resp_players['data']['players']

    def white_list_player(self, gamertag):
        """
        Player_Management - Add Player to Whitelist
        :param gamertag: Player unique identifier.
        """
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        params = {"identifer": gamertag}
        path = ["services", self.service_id, "gameservers", "games", "whitelist"]
        return GameServer.CLIENT.put(path=path, params=params)

    def make_admin(self, gamertag):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        """ Must whitelist the player first """
        path = ['services', self.service_id, 'gameservers', 'adminlist']
        params = {'identifier': gamertag}
        return GameServer.CLIENT.post(path=path, params=params)

    def details(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers']
        resp_details = GameServer.CLIENT.get(path=path)
        assert_success(resp_details)
        return resp_details['data']['gameserver']

    def restart(self, restart_message: str = None, log_message: str = None):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'restart']
        params = {"restart_message": restart_message, "message": log_message}
        resp_restart = GameServer.CLIENT.post(path=path, params=params)
        assert_success(resp_restart)
        return resp_restart['status'] == 'success'

    def stop(self, message=None, stop_message=None):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        try:
            path = ['services', self.service_id, 'gameservers', 'stop']
            params = {'message': message, 'stop_message': stop_message}
            return GameServer.CLIENT.post(path=path, params=params)['status'] == 'success'
        except Exception as e:
            print(e)
            return False

    def list_backups(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'backups']
        return GameServer.CLIENT.get(path=path)

    def command(self, command):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'app_server', 'command']
        params = {'command': command}
        return GameServer.CLIENT.post(path=path, params=params)

    def ping(self, command):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'app_server']
        return GameServer.CLIENT.get(path=path, params={'command': command})

    def restore_database(self, database: str, timestamp: str):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'backups', 'database']
        params = {'database': database, 'timestamp': timestamp}
        return GameServer.CLIENT.post(path=path, params=params)

    def ftp_change_password(self, password: str):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'ftp', 'password']
        params = {'password': password}
        return GameServer.CLIENT.post(path=path, params=params)

    def bookmarks(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'bookmarks']
        return GameServer.CLIENT.get(path=path)

    def copy_file(self, source_path: str, target_path: str, target_name: str):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'copy']
        params = {'source_path': source_path, 'target_path': target_path, 'target_name': target_name}
        return GameServer.CLIENT.post(path=path, params=params)

    def create_directory(self, dir_path, name):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'mkdir']
        params = {'path': dir_path, 'name': name}
        return GameServer.CLIENT.post(path=path, params=params)

    def delete_file(self, file_path):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'delete']
        params = {'path': file_path}
        return GameServer.CLIENT.delete(path=path, params=params)

    def list_files(self, dir_path=None, search: str = None):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'list']
        params = {'dir': dir_path, 'search': search}
        return GameServer.CLIENT.get(path=path, params=params)

    def move_file(self, source_path: str, target_path: str):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'move']
        name = source_path.split('/')[-1]
        params = {'source_path': source_path, 'target_path': target_path, 'target_file_name': name}
        return GameServer.CLIENT.post(path=path, params=params)

    def seek_file(self, file_path: str, offset: int, length: int, mode: str = None):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'seek']
        params = {'file': file_path, 'offset': offset, 'length': length, 'mode': mode}
        return GameServer.CLIENT.get(path=path, params=params)

    def file_size(self, file_path):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'size']
        params = {'file': file_path}
        return GameServer.CLIENT.get(path=path, params=params)

    def duplicate_file(self, source_path, target_path, target_name):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'copy']
        params = {'source_path': source_path, 'target_path': target_path, 'target_name': target_name}
        return GameServer.CLIENT.post(path=path, params=params)

    def files_stat(self, files_paths: list):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'stat']
        params = {'files': files_paths}
        return GameServer.CLIENT.get(path=path, params=params)

    def upload_file(self, target_dir: str, file_name: str):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'file_server', 'upload']
        params = {'path': target_dir, 'file': file_name}
        return GameServer.CLIENT.post(path=path, params=params)

    def list_all_games(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['gameserver', 'games']
        return GameServer.CLIENT.get(path=path)

    def install_game(self, game: str, modpack: str = None):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'games', 'install']
        params = {'game': game, 'modpack': modpack}
        return GameServer.CLIENT.post(path=path, params=params)

    def list_games(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'games']
        return GameServer.CLIENT.get(path=path)

    def start_game(self, game: str):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'games', 'start']
        params = {'game': game}
        return GameServer.CLIENT.post(path=path, params=params)

    def uninstall_game(self, game: str):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'games', 'uninstall']
        params = {'game': game}
        return GameServer.CLIENT.delete(path=path, params=params)

    def change_mysql_password(self, password: str):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'mysql', 'password']
        params = {'password': password}
        return GameServer.CLIENT.post(path=path, params=params)

    def reset_mysql_database(self, password: str):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'mysql', 'reset']
        params = {'password': password}
        return GameServer.CLIENT.post(path=path, params=params)

    def install_package(self, package: str, version: str = None):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'packages']
        params = {'package': package, 'version': version}
        return GameServer.CLIENT.post(path=path, params=params)

    def list_packages(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'packages']
        return GameServer.CLIENT.post(path=path)

    def reinstall_package(self, package: str, version: str = None):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'packages', 'reinstall']
        params = {'package': package, 'version': version}
        return GameServer.CLIENT.put(path=path, params=params)

    def uninstall_package(self, package: str):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'packages', 'uninstall']
        params = {'package': package}
        return GameServer.CLIENT.delete(path=path, params=params)

    def resource_usage(self, hours: int = None):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'stats']
        params = {'hours': hours}
        return GameServer.CLIENT.get(path=path, params=params)

    def create_settings_sets(self, name: str = None):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'settings', 'sets']
        params = {'name': name}
        return GameServer.CLIENT.post(path=path, params=params)

    def delete_settings_sets(self, set_id: int):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'settings', 'sets', set_id]
        return GameServer.CLIENT.delete(path=path)

    def settings_sets(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'settings', 'sets']
        sets = GameServer.CLIENT.get(path=path)['data']['sets']
        return [data['data'] for data in sets]

    def restore_settings_sets(self, set_id: int):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'settings', 'sets', set_id, 'restore']
        return GameServer.CLIENT.post(path=path)

    def default_settings(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'settings', 'defaults']
        return GameServer.CLIENT.get(path=path)

    def reset_settings(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'settings']
        return GameServer.CLIENT.delete(path=path)

    def update_settings(self, category: str = None, key: str = None, value: str = None):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'settings']
        params = {'category': category, 'key.txt': key, 'value': value}
        return GameServer.CLIENT.post(path=path, params=params)

    def boost_history(self, page: int = 0):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'boost', 'history']
        params = {'page': page}
        return GameServer.CLIENT.get(path=path, params=params)

    def boost_settings(self):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'boost']
        return GameServer.CLIENT.get(path=path)

    def update_boost_settings(self, enable: bool = True, message: str = None, welcome_message: str = None):
        assert GameServer.CLIENT is not None, "A client must be initialized for GameServer"
        path = ['services', self.service_id, 'gameservers', 'boost']
        params = {'enable': enable, 'message': message, 'welcome_message': welcome_message}
        return GameServer.CLIENT.put(path=path, params=params)

    def __repr__(self):
        return f"<GameServer(service_id={self.service_id}, status='{self.status}', query={self.query})>"

    def __str__(self):
        return f"""
        status = '{self.status}'
        last_status_change = {self.last_status_change}
        must_be_started = {self.must_be_started}
        websocket_token = '{self.websocket_token}'
        hostsystems = {self.hostsystems}
        username = '{self.username}'
        user_id = {self.user_id}
        service_id = {self.service_id}
        location_id = {self.location_id}
        minecraft_mode = {self.minecraft_mode}
        ip = '{self.ip}'
        ipv6 = {self.ipv6}
        port = {self.port}
        query_port = {self.query_port}
        rcon_port = {self.rcon_port}
        label = '{self.label}'
        type = '{self.type}'
        memory = '{self.memory}'
        memory_mb = {self.memory_mb}
        game = '{self.game}'
        game_human = {self.game_human}
        game_specific = {self.game_specific}
        modpacks = {self.modpacks}
        slots = {self.slots}
        location = '{self.location}'
        credentials = {self.credentials}
        settings = {self.settings}
        quota = {self.quota}
        query = {self.query}
        """
