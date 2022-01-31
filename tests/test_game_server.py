import json
from src.example_package.client import Client
from src import GameServer


def pretty_json(data: dict):
    return json.dumps(data, indent=3, sort_keys=True)


def test_commands():
    print("#############   ListBackups    ################")
    gameserver = GameServer.all()[0]
    gameserver.command("")
    print("\n")


def test_list_backups():
    gameserver = GameServer.all()[0]
    print("#############   ListBackups    ################")
    print(pretty_json(gameserver.list_backups()))
    print("\n")


if __name__ == "__main__":
    import os
    access_token = os.environ.get('NITRADO_KEY')
    client = Client("https://api.nitrado.net/", access_token)
    Client.CLIENT = client
    GameServer.CLIENT = client

    # test_commands() # requires RCON but I've yet to test it.
    test_list_backups()
