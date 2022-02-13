from nitrado import NitradoAPI, GameServer, Client, Service, initialize_client
import os


def success(response):
    if not response:
        return False
    return 'status' in response and response['status'] == 'success'


def set_client():
    url = "https://api.nitrado.net/"
    key = os.getenv('NITRADO_KEY')
    initialize_client(key, url)


def test_client():
    set_client()
    print(type(NitradoAPI.CLIENT))
    print(type(Client.CLIENT))
    print(type(GameServer.CLIENT))
    print(type(Service.CLIENT))
    assert NitradoAPI.CLIENT is not None
    assert GameServer.CLIENT is not None
    assert Client.CLIENT is not None
    assert Service.CLIENT is not None


def test_nitrado_init():
    api = NitradoAPI()
    assert api is not None


def test_health_check():
    api = NitradoAPI()
    health = api.health_check()
    assert type(health) == str


def test_maintenance():
    api = NitradoAPI()
    maint = api.maintenance_status()
    assert type(maint) == dict


def test_version():
    api = NitradoAPI()
    version = api.version()
    assert type(version) == str


def test_services():
    api = NitradoAPI()
    assert type(api.services) == list
    assert len(api.services) > 0


def test_game_servers():
    api = NitradoAPI()
    assert type(api.game_servers) == list
    assert len(api.game_servers) > 0


def tests():
    test_client()
    test_nitrado_init()
    test_health_check()
    test_maintenance()
    test_version()
    test_services()
    test_game_servers()


if __name__ == '__main__':
    tests()
    print("passing")

