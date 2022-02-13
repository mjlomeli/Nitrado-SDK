from nitrado import Client
from nitrado import GameServer
import os


def set_client():
    url = "https://api.nitrado.net/"
    if GameServer.CLIENT:
        return GameServer.CLIENT
    if not Client.CLIENT:
        Client.CLIENT = Client(url, key=os.environ['NITRADO_KEY'])
    GameServer.CLIENT = Client.CLIENT


def test_get_all():
    set_client()
    gameserver = GameServer.all()
    assert len(gameserver) > 0


def test_list_backups():
    test_get_all()
    gameserver = GameServer.all()[0]
    backups_json = gameserver.list_backups()
    assert backups_json
    assert 'status' in backups_json
    assert backups_json['status'] == 'success'


def tests():
    test_get_all()
    test_list_backups()


if __name__ == "__main__":
    tests()
