from nitrado.client import Client
import requests
from pathlib import Path, WindowsPath


class GameServer:
    CLIENT = Client.CLIENT

    @classmethod
    def find_game_server(cls, service_id):
        try:
            path = ['services', service_id, 'gameservers']
            data = GameServer.CLIENT.get(path=path)['data']['gameserver']
            return GameServer(data)
        except Exception as e:
            return None

    @classmethod
    def all(cls):
        games = []
        try:
            servs = GameServer.CLIENT.get(path='services')
            service_ids = [serv['id'] for serv in servs['data']['services']]
            for id in service_ids:
                games.append(GameServer.find_game_server(id))
            return games
        except Exception as e:
            print(e)
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
        path = ['services', self.service_id, 'gameservers', 'games', 'arkse', 'gen_cluster_id']
        return GameServer.CLIENT.get(path=path)['data']['clusterid']

    def logs_shooter_game(self):
        try:
            path = ['services', self.service_id, 'gameservers', 'file_server', 'download']
            params = {'file': f"/games/{self.username}/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame.log"}
            url = GameServer.CLIENT.get(path=path, params=params)['data']['token']['url']
            req = requests.get(url)
            return req.text.replace("\r\n", "\n")
        except Exception as e:
            print('[error] logs_shooter_game:', e)
            return ''

    def logs_restart(self):
        try:
            path = ['services', self.service_id, 'gameservers', 'file_server', 'download']
            params = {'file': f"/games/{self.username}/ftproot/restart.log"}
            url = GameServer.CLIENT.get(path=path, params=params)['data']['token']['url']
            req = requests.get(url)
            return req.text.replace("\r\n", "\n")
        except Exception as e:
            print('[error] logs_restart:', e)
            return ''

    def logs_shooter_game_last(self):
        try:
            path = ['services', self.service_id, 'gameservers', 'file_server', 'download']
            params = {'file': f"/games/{self.username}/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame_Last.log"}
            url = GameServer.CLIENT.get(path=path, params=params)['data']['token']['url']
            req = requests.get(url)
            return req.text.replace("\r\n", "\n")
        except Exception as e:
            print('[error] logs_shooter_game_last:', e)
            return ''

    def logs_download(self, directory=Path.cwd()):
        assert type(directory) == str or type(directory) == Path or type(directory) == WindowsPath, "Path provided must be of type string"
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
        path = ['services', self.service_id, 'gameservers', 'games', 'start']
        params = {'game': game}
        return GameServer.CLIENT.post(path=path, params=params)

    def backup_restore(self, folder, backup_id):
        path = ['services', self.service_id, 'gameservers', 'backups', 'gameserver']
        params = {'folder': folder, 'backup': backup_id}
        return GameServer.CLIENT.post(path=path, params=params)

    def download_file(self, file_path):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'download']
        # /games/ni*******_1/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame.log
        # /games/ni1299121_3741/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame.log
        # /games/ni1299121_3741/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame_Last.log
        # curl -H 'Authorization: Bearer <token>' 'https://api.nitrado.net/services/7315782/gameservers/file_server/download?file=%2Fgames%2Fni1299121_3741%2Fnoftp%2Farkxb%2FShooterGame%2FSaved%2FLogs%2FShooterGame.log
        params = {'path': file_path}
        return GameServer.CLIENT.get(path=path, params=params)

    def rename_file(self, file_path, target_path, target_name):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'move']
        params = {'source_path': file_path, 'target_path': target_path, 'target_filename': target_name}
        return GameServer.CLIENT.post(path=path, params=params)

    # def rename_file(self, file_path, new_name):
    #     path = ['services', self.service_id, 'gameservers', 'file_server', 'move']
    #     target_path = '/'.join(file_path.split("/")[:-1])
    #     params = {'source_path': file_path, 'target_path': target_path, 'target_filename': new_name}
    #     return self._client.post(path=path, params=params)

    def donation_history(self, page=0):
        path = ['services', self.service_id, 'gameservers', 'boost', 'history']
        params = {'page': page}
        return GameServer.CLIENT.get(path=path, params=params)

    def donation_settings(self):
        path = ['services', self.service_id, 'gameservers', 'boost']
        return GameServer.CLIENT.get(path=path)['data']

    def update_donation_settings(self, enable=True, message=None, welcome_message=None):
        path = ['services', self.service_id, 'gameservers', 'boost']
        params = {'enable': enable, 'message': message, 'welcome_message': welcome_message}
        return GameServer.CLIENT.put(path=path, params=params)

    def players(self):
        try:
            path = ["services", self.service_id, "gameservers", "games", "players"]
            return GameServer.CLIENT.get(path=path)['data']['players']
        except Exception as e:
            print("[error] list_players_on_server():", e)

    def white_list_player(self, gamertag):
        """
        Player_Management - Add Player to Whitelist
        :param server_id: The gameserver id
        :param identifer: Player unique identifier.
        """
        params = {"identifer": gamertag}
        path = ["services", self.service_id, "gameservers", "games", "whitelist"]
        return GameServer.CLIENT.put(path=path, params=params)

    def make_admin(self, gamertag):
        """ Must whitelist the player first """
        path = ['services', self.service_id, 'gameservers', 'adminlist']
        params = {'identifier': gamertag}
        return GameServer.CLIENT.post(path=path, params=params)

    def details(self):
        try:
            path = ['services', self.service_id, 'gameservers']
            return GameServer.CLIENT.get(path=path)['data']['gameserver']
        except Exception as e:
            print("[error] details():", e)

    def restart(self, restart_message: str = None, log_message: str = None):
        try:
            path = ['services', self.service_id, 'gameservers', 'restart']
            params = {"restart_message": restart_message, "message": log_message}
            return GameServer.CLIENT.post(path=path, params=params)['status'] == 'success'
        except Exception as e:
            return False

    def stop(self, message=None, stop_message=None):
        try:
            path = ['services', self.service_id, 'gameservers', 'stop']
            params = {'message': message, 'stop_message': stop_message}
            return GameServer.CLIENT.post(path=path, params=params)['status'] == 'success'
        except Exception as e:
            return False

    def list_backups(self):
        path = ['services', self.service_id, 'gameservers', 'backups']
        return GameServer.CLIENT.get(path=path)

    def command(self, command):
        path = ['services', self.service_id, 'gameservers', 'app_server', 'command']
        params = {'command': command}
        return GameServer.CLIENT.post(path=path, params=params)

    def ping(self, command):
        path = ['services', self.service_id, 'gameservers', 'app_server']
        return GameServer.CLIENT.get(path=path, params={'command': command})

    def restore_database(self, database: str, timestamp: str):
        path = ['services', self.service_id, 'gameservers', 'backups', 'database']
        params = {'database': database, 'timestamp': timestamp}
        return GameServer.CLIENT.post(path=path, params=params)

    def ftp_change_password(self, password: str):
        path = ['services', self.service_id, 'gameservers', 'ftp', 'password']
        params = {'password': password}
        return GameServer.CLIENT.post(path=path, params=params)

    def bookmarks(self):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'bookmarks']
        return GameServer.CLIENT.get(path=path)

    def copy_file(self, source_path: str, target_path: str, target_name: str):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'copy']
        params = {'source_path': source_path, 'target_path': target_path, 'target_name': target_name}
        return GameServer.CLIENT.post(path=path, params=params)

    def create_directory(self, dir_path, name):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'mkdir']
        params = {'path': dir_path, 'name': name}
        return GameServer.CLIENT.post(path=path, params=params)

    def delete_file(self, file_path):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'delete']
        params = {'path': file_path}
        return GameServer.CLIENT.delete(path=path, params=params)

    def list_files(self, dir_path=None, search: str = None):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'list']
        params = {'dir': dir_path, 'search': search}
        return GameServer.CLIENT.get(path=path, params=params)

    def move_file(self, source_path: str, target_path: str):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'move']
        name = source_path.split('/')[-1]
        params = {'source_path': source_path, 'target_path': target_path, 'target_file_name': name}
        return GameServer.CLIENT.post(path=path, params=params)

    def seek_file(self, file_path: str, offset: int, length: int, mode: str = None):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'seek']
        params = {'file': file_path, 'offset': offset, 'length': length, 'mode': mode}
        return GameServer.CLIENT.get(path=path, params=params)

    def file_size(self, file_path):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'size']
        params = {'file': file_path}
        return GameServer.CLIENT.get(path=path, params=params)

    def duplicate_file(self, source_path, target_path, target_name):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'copy']
        params = {'source_path': source_path, 'target_path': target_path, 'target_name': target_name}
        return GameServer.CLIENT.post(path=path, params=params)

    def files_stat(self, files_paths: list):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'stat']
        params = {'files': files_paths}
        return GameServer.CLIENT.get(path=path, params=params)

    def upload_file(self, target_dir: str, file_name: str):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'upload']
        params = {'path': target_dir, 'file': file_name}
        return GameServer.CLIENT.post(path=path, params=params)

    def list_all_games(self):
        path = ['gameserver', 'games']
        return GameServer.CLIENT.get(path=path)

    def install_game(self, game: str, modpack: str = None):
        path = ['services', self.service_id, 'gameservers', 'games', 'install']
        params = {'game': game, 'modpack': modpack}
        return GameServer.CLIENT.post(path=path, params=params)

    def list_games(self):
        path = ['services', self.service_id, 'gameservers', 'games']
        return GameServer.CLIENT.get(path=path)

    def start_game(self, game: str):
        path = ['services', self.service_id, 'gameservers', 'games', 'start']
        params = {'game': game}
        return GameServer.CLIENT.post(path=path, params=params)

    def uninstall_game(self, game: str):
        path = ['services', self.service_id, 'gameservers', 'games', 'uninstall']
        params = {'game': game}
        return GameServer.CLIENT.delete(path=path, params=params)

    def change_mysql_password(self, password: str):
        path = ['services', self.service_id, 'gameservers', 'mysql', 'password']
        params = {'password': password}
        return GameServer.CLIENT.post(path=path, params=params)

    def reset_mysql_database(self, password: str):
        path = ['services', self.service_id, 'gameservers', 'mysql', 'reset']
        params = {'password': password}
        return GameServer.CLIENT.post(path=path, params=params)

    def install_package(self, package: str, version: str = None):
        path = ['services', self.service_id, 'gameservers', 'packages']
        params = {'package': package, 'version': version}
        return GameServer.CLIENT.post(path=path, params=params)

    def list_packages(self):
        path = ['services', self.service_id, 'gameservers', 'packages']
        return GameServer.CLIENT.post(path=path)

    def reinstall_package(self, package: str, version: str = None):
        path = ['services', self.service_id, 'gameservers', 'packages', 'reinstall']
        params = {'package': package, 'version': version}
        return GameServer.CLIENT.put(path=path, params=params)

    def uninstall_package(self, package: str):
        path = ['services', self.service_id, 'gameservers', 'packages', 'uninstall']
        params = {'package': package}
        return GameServer.CLIENT.delete(path=path, params=params)

    def resource_usage(self, hours: int = None):
        path = ['services', self.service_id, 'gameservers', 'stats']
        params = {'hours': hours}
        return GameServer.CLIENT.get(path=path, params=params)

    def create_settings_sets(self, name: str = None):
        path = ['services', self.service_id, 'gameservers', 'settings', 'sets']
        params = {'name': name}
        return GameServer.CLIENT.post(path=path, params=params)

    def delete_settings_sets(self, set_id: int):
        path = ['services', self.service_id, 'gameservers', 'settings', 'sets', set_id]
        return GameServer.CLIENT.delete(path=path)

    def settings_sets(self):
        path = ['services', self.service_id, 'gameservers', 'settings', 'sets']
        sets = GameServer.CLIENT.get(path=path)['data']['sets']
        return [data['data'] for data in sets]

    def restore_settings_sets(self, set_id: int):
        path = ['services', self.service_id, 'gameservers', 'settings', 'sets', set_id, 'restore']
        return GameServer.CLIENT.post(path=path)

    def default_settings(self):
        path = ['services', self.service_id, 'gameservers', 'settings', 'defaults']
        return GameServer.CLIENT.get(path=path)

    def reset_settings(self):
        path = ['services', self.service_id, 'gameservers', 'settings']
        return GameServer.CLIENT.delete(path=path)

    def update_settings(self, category: str=None, key: str=None, value: str=None):
        path = ['services', self.service_id, 'gameservers', 'settings']
        params = {'category': category, 'key': key, 'value': value}
        return GameServer.CLIENT.post(path=path, params=params)

    def boost_history(self, page: int = 0):
        path = ['services', self.service_id, 'gameservers', 'boost', 'history']
        params = {'page': page}
        return GameServer.CLIENT.get(path=path, params=params)

    def boost_settings(self):
        path = ['services', self.service_id, 'gameservers', 'boost']
        return GameServer.CLIENT.get(path=path)

    def update_boost_settings(self, enable: bool = True, message: str = None, welcome_message: str = None):
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

