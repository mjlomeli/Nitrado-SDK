from nitrado import NitradoAPI, Client
import os


def get_client():
    url = "https://api.nitrado.net/"
    key = os.getenv('NITRADO_KEY')
    return Client(url, key)


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

