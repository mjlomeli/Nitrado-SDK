import json
from src.nitrado_api import NitradoAPI


def print_json(data: dict):
    print(json.dumps(data, indent=3, sort_keys=True))


if __name__ == '__main__':
    api = NitradoAPI()
    print_json(api.health_check())
    print_json(api.maintenance_status())
    print_json(api.version())

    for service in api.services:
        print(service)

    for game in api.game_servers:
        print(game)
