from gamedriver.nitrado.Client import Client
import json
web_interface = 'https://server.nitrado.net/eng/services/weblogin/9409179'


def _get_key():
    from pathlib import Path
    import os
    key_file = Path(os.environ.get("KEY")) / Path("keys.json")
    if key_file.exists():
        with open(key_file, "r") as r:
            data = json.load(r)
            return data['api']['https://server.nitrado.net/']['accounts'][0]['key']


class GameServer(Client):
    def __init__(self, service_id: int, access_token: str=_get_key()):
        """
        :param access_token: the token provided by nitrado
        :param service_id: the gameserver id on nitrado
        """
        super(GameServer, self).__init__("https://api.nitrado.net/", access_token)
        self.__service_id = service_id

    def cluster_id(self):
        path = ['services', self.__service_id, 'gameservers', 'games', 'arkse', 'gen_cluster_id']
        return self.get(path=path)['data']['clusterid']

    def details(self):
        return self.get(path=['services', self.__service_id, 'gameservers'])['data']

    def start(self, game):
        path = ['services', self.__service_id, 'gameservers', 'games', 'start']
        params = {'game': game}
        return self.post(path=path, params=params)

    def restart(self, restart_message=None, log_message=None):
        path = ['services', self.__service_id, 'gameservers', 'restart']
        params = {"restart_message": restart_message, "message": log_message}
        return self.post(path=path, params=params)

    def stop(self, message=None, stop_message=None):
        path = ['services', self.__service_id, 'gameservers', 'stop']
        params = {'message': message, 'stop_message': stop_message}
        return self.post(path=path, params=params)

    def list_backups(self):
        path = ['services', self.__service_id, 'gameservers', 'backups']
        return self.get(path=path)['data']

    def command(self, command):
        path = ['services', self.__service_id, 'gameservers', 'app_server', 'command']
        params = {'command': command}
        return self.post(path=path, params=params)

    def ping(self):
        path = ['services', self.__service_id, 'gameservers', 'app_server']
        return self.get(path=path)

    def restore_database(self, db_name, timestamp):
        path = ['services', self.__service_id, 'gameservers', 'backups', 'database']
        params = {'database': db_name, 'timestamp': timestamp}
        return self.post(path=path, params=params)

    def backup_restore(self, folder, backup_id):
        path = ['services', self.__service_id, 'gameservers', 'backups', 'gameserver']
        params = {'folder': folder, 'backup': backup_id}
        return self.post(path=path, params=params)

    def duplicate_file(self, source_path, target_path, target_name):
        path = ['services', self.__service_id, 'gameservers', 'file_server', 'copy']
        params = {'source_path': source_path, 'target_path': target_path, 'target_name': target_name}
        return self.post(path=path, params=params)

    def create_directory(self, dir_path, name):
        path = ['services', self.__service_id, 'gameservers', 'file_server', 'mkdir']
        params = {'path': dir_path, 'name': name}
        return self.post(path=path, params=params)

    def delete_file(self, file_path):
        path = ['services', self.__service_id, 'gameservers', 'file_server', 'delete']
        params = {'path': file_path}
        return self.delete(path=path, params=params)

    def download_file(self, file_path):
        path = ['services', self.__service_id, 'gameservers', 'file_server', 'download']
        # /games/ni*******_1/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame.log
        # /games/ni1299121_3741/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame.log
        # /games/ni1299121_3741/noftp/arkxb/ShooterGame/Saved/Logs/ShooterGame_Last.log
        # curl -H 'Authorization: Bearer <token>' 'https://api.nitrado.net/services/7315782/gameservers/file_server/download?file=%2Fgames%2Fni1299121_3741%2Fnoftp%2Farkxb%2FShooterGame%2FSaved%2FLogs%2FShooterGame.log
        params = {'path': file_path}
        return self.get(path=path, params=params)

    def list_files(self, dir_path=None, search=None):
        path = ['services', self.__service_id, 'gameservers', 'file_server', 'list']
        params = {'dir': dir_path, 'search': search}
        return self.get(path=path, params=params)

    def rename_file(self, file_path, target_path, target_name):
        path = ['services', self.__service_id, 'gameservers', 'file_server', 'move']
        params = {'source_path': file_path, 'target_path': target_path, 'target_filename': target_name}
        return self.post(path=path, params=params)

    def upload_file(self, target_dir, target_name):
        path = ['services', self.__service_id, 'gameservers', 'file_server', 'upload']
        params = {'path': target_dir, 'file': target_name}
        return self.post(path=path, params=params)

    def donation_history(self, page=0):
        path = ['services', self.__service_id, 'gameservers', 'boost', 'history']
        params = {'page': page}
        return self.get(path=path, params=params)

    def donation_settings(self):
        path = ['services', self.__service_id, 'gameservers', 'boost']
        return self.get(path=path)

    def update_donation_settings(self, enable=True, message=None, welcome_message=None):
        path = ['services', self.__service_id, 'gameservers', 'boost']
        params = {'enable': enable, 'message': message, 'welcome_message': welcome_message}
        return self.put(path=path, params=params)

    def list_players_on_server(self):
        path = ["services", self.__service_id, "gameservers", "games", "players"]
        return self.get(path=path)

    def white_list_player(self, gamertag):
        """
        Player_Management - Add Player to Whitelist
        :param server_id: The gameserver id
        :param identifer: Player unique identifier.
        """
        params = {"identifer": gamertag}
        path = ["services", self.__service_id, "gameservers", "games", "whitelist"]
        return self.put(path=path, params=params)

    def make_admin(self, gamertag):
        """ Must whitelist the player first """
        path = ['services', self.__service_id, 'gameservers', 'adminlist']
        params = {'identifier': gamertag}
        return self.post(path=path, params=params)


class Service:
    def __init__(self, client, service_id):
        self.__service_id = service_id
        self = client

    def list_services(self):
        return self.get(path='services')

    def details(self):
        return self.get(path=['services', self.__service_id])

    def logs(self):
        return self.get(path=['services', self.__service_id, 'logs'])

    def notifications(self):
        return self.get(path=['services', self.__service_id, 'notifications'])

    def list_tasks(self):
        path = ['services', self.__service_id, 'tasks']
        return self.get(path=path)

    def create_task(self, action_method, month, day, hour, minute, weekday, action_data=None):
        path = ['services', self.__service_id, 'tasks']
        params = {'action_method': action_method, 'action_data': action_data, 'minute': minute,
                  'hour': hour, 'day': day, 'month': month, 'weekday': weekday}
        return self.post(path=path, params=params)

    def update_task(self, task_id, action_method, month, day, hour, minute, weekday, action_data=None):
        path = ['services', self.__service_id, 'tasks', task_id]
        params = {'action_method': action_method, 'action_data': action_data, 'minute': minute,
                  'hour': hour, 'day': day, 'month': month, 'weekday': weekday}
        return self.put(path=path, params=params)

    def delete_task(self, task_id):
        path = ['services', self.__service_id, 'tasks', task_id]
        return self.delete(path=path)


# GETATTRIBUTE && SET ATTRIBUTE Templates

data = {'name': 'maury', 'date': 'today'}


class User(object):
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __getattribute__(self, name):
        if name == 'name' or name == 'date':
            print("__getattribute__({}):".format(name))
            value = super(User, self).__getattribute__(name)
            print('\tif {} != {}: {}'.format(value, data[name], value != data[name]))
            if value != data[name]:
                self.__dict__[name] = data[name]
                print("\t\tself.{} = {}".format(name, value))
            print("\n")
        return super(User, self).__getattribute__(name)

    def __setattr__(self, name, value):
        if name == 'name' or name == 'date':
            print("__setattr__({}, {}):".format(name, value))
            print("\tself.{} = {}".format(name, value))
        self.__dict__[name] = value
        if name == 'name' or name == 'date':
            print("\tDATA[{}] = {}".format(name, value))
            print("\n")
        data[name] = value


def test_get_set_attributes():
    user = User('maury', 'today')
    data['name'] = "hello"


def test_service_details():
    from gamedriver.nitrado.Client import pretty_json
    client = Client("https://api.nitrado.net/")
    service = Service(client, 9409179)
    print("#############   DETAILS    ################")
    print(pretty_json(service.details()))
    print("\n")


def test_service_logs():
    from gamedriver.nitrado.Client import pretty_json
    client = Client("https://api.nitrado.net/")
    service = Service(client, 9409179)
    print("#############   LOGS    ################")
    print(pretty_json(service.logs()))
    print("\n")


def test_service_list():
    from gamedriver.nitrado.Client import pretty_json
    client = Client("https://api.nitrado.net/")
    service = Service(client, 9409179)
    print("#############   List    ################")
    print(pretty_json(service.list_services()))
    print("\n")


def test_commands():
    print("#############   ListBackups    ################")
    client = Client("https://api.nitrado.net/")
    gameserver = GameServer(client, 9409179)
    zed = 696509819
    # gameserver.command('cheat GiveCreativeModeToPlayer {}'.format(zed))
    gameserver.command("")
    print("\n")


def test_list_backups():
    from gamedriver.nitrado.Client import pretty_json
    client = Client("https://api.nitrado.net/")
    gameserver = GameServer(client, 9409179)
    print("#############   ListBackups    ################")
    print(pretty_json(gameserver.list_backups()))
    print("\n")


if __name__ == "__main__":
    zed = '696509819'
    name = 'Zedd'
    # test_service_logs()
    # test_service_details()
    # test_service_list()
    test_commands()
    # test_list_backups()
