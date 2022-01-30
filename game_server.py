from client import Client


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

    def details(self):
        return GameServer.CLIENT.get(path=['services', self.service_id, 'gameservers'])['data']

    def start(self, game):
        path = ['services', self.service_id, 'gameservers', 'games', 'start']
        params = {'game': game}
        return GameServer.CLIENT.post(path=path, params=params)

    def restart(self, restart_message=None, log_message=None):
        path = ['services', self.service_id, 'gameservers', 'restart']
        params = {"restart_message": restart_message, "message": log_message}
        return GameServer.CLIENT.post(path=path, params=params)

    def stop(self, message=None, stop_message=None):
        path = ['services', self.service_id, 'gameservers', 'stop']
        params = {'message': message, 'stop_message': stop_message}
        return GameServer.CLIENT.post(path=path, params=params)

    def list_backups(self):
        path = ['services', self.service_id, 'gameservers', 'backups']
        return GameServer.CLIENT.get(path=path)['data']

    def command(self, command):
        path = ['services', self.service_id, 'gameservers', 'app_server', 'command']
        params = {'command': command}
        return GameServer.CLIENT.post(path=path, params=params)

    def ping(self):
        path = ['services', self.service_id, 'gameservers', 'app_server']
        return GameServer.CLIENT.get(path=path)

    def restore_database(self, db_name, timestamp):
        path = ['services', self.service_id, 'gameservers', 'backups', 'database']
        params = {'database': db_name, 'timestamp': timestamp}
        return GameServer.CLIENT.post(path=path, params=params)

    def backup_restore(self, folder, backup_id):
        path = ['services', self.service_id, 'gameservers', 'backups', 'gameserver']
        params = {'folder': folder, 'backup': backup_id}
        return GameServer.CLIENT.post(path=path, params=params)

    def duplicate_file(self, source_path, target_path, target_name):
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

    def download_file(self, file_path):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'download']
        # /games/ni*******_1/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame.log
        # /games/ni1299121_3741/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame.log
        # /games/ni1299121_3741/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame_Last.log
        # curl -H 'Authorization: Bearer <token>' 'https://api.nitrado.net/services/7315782/gameservers/file_server/download?file=%2Fgames%2Fni1299121_3741%2Fnoftp%2Farkxb%2FShooterGame%2FSaved%2FLogs%2FShooterGame.log
        params = {'path': file_path}
        return GameServer.CLIENT.get(path=path, params=params)

    def list_files(self, dir_path=None, search=None):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'list']
        params = {'dir': dir_path, 'search': search}
        return GameServer.CLIENT.get(path=path, params=params)

    def rename_file(self, file_path, target_path, target_name):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'move']
        params = {'source_path': file_path, 'target_path': target_path, 'target_filename': target_name}
        return GameServer.CLIENT.post(path=path, params=params)

    def upload_file(self, target_dir, target_name):
        path = ['services', self.service_id, 'gameservers', 'file_server', 'upload']
        params = {'path': target_dir, 'file': target_name}
        return GameServer.CLIENT.post(path=path, params=params)

    def donation_history(self, page=0):
        path = ['services', self.service_id, 'gameservers', 'boost', 'history']
        params = {'page': page}
        return GameServer.CLIENT.get(path=path, params=params)

    def donation_settings(self):
        path = ['services', self.service_id, 'gameservers', 'boost']
        return GameServer.CLIENT.get(path=path)

    def update_donation_settings(self, enable=True, message=None, welcome_message=None):
        path = ['services', self.service_id, 'gameservers', 'boost']
        params = {'enable': enable, 'message': message, 'welcome_message': welcome_message}
        return GameServer.CLIENT.put(path=path, params=params)

    def list_players_on_server(self):
        path = ["services", self.service_id, "gameservers", "games", "players"]
        return GameServer.CLIENT.get(path=path)

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



def test_commands():
    import json
    print("#############   ListBackups    ################")
    import os
    access_token = os.environ.get('NITRADO_KEY')
    client = Client("https://api.nitrado.net/", access_token)
    gameserver = GameServer(client, 9409179)
    zed = 696509819
    # gameserver.command('cheat GiveCreativeModeToPlayer {}'.format(zed))
    gameserver.command("")
    print("\n")


def test_list_backups():
    import json
    def pretty_json(data: dict):
        return json.dumps(data, indent=3, sort_keys=True)

    gameserver = GameServer(9409179)
    print("#############   ListBackups    ################")
    print(pretty_json(gameserver.list_backups()))
    print("\n")


if __name__ == "__main__":
    import os
    access_token = os.environ.get('NITRADO_KEY')
    client = Client("https://api.nitrado.net/", access_token)
    Client.CLIENT = client
    GameServer.CLIENT = client

    zed = '696509819'
    name = 'Zedd'
    # test_commands()
    test_list_backups()

























