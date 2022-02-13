from nitrado import initialize_client, GameServer
import os


def set_client():
    url = "https://api.nitrado.net/"
    key = os.getenv('NITRADO_KEY')
    initialize_client(key, url)


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
    print("passing")
