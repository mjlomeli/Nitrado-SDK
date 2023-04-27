import os
from dotenv import load_dotenv
from .lib import Client
from .service import Service
from .gameserver import GameServer
from pathlib import Path


def initialize(api_key: str, save=False) -> None:
    """Saves the Nitrado API key in a local .env file"""
    os.environ[Client.ENV_NAME] = api_key
    if not save:
        return
    if not Path('.env').exists():
        Path('.env').touch()
    with open('.env', 'r+') as r:
        content = []
        found = False
        for line in r.readlines():
            if line.find(f'{Client.ENV_NAME}=') == 0:
                content += [f"{Client.ENV_NAME}={api_key}\n"]
                found = True
            else:
                content += [line]
        if not found:
            content = [f"{Client.ENV_NAME}={api_key}\n"] + content
        r.seek(0)
        r.write(''.join(content))
        load_dotenv()


def services() -> list[Service]:
    """Get a list of all services."""
    return Service.all()


def gameservers() -> list[GameServer]:
    """Get a list of all gameservers."""
    return GameServer.all()


def gameserver_by_service_id(service_id: int) -> GameServer:
    """Get a gameserver by service id."""
    return GameServer.find_by_id(service_id)


def service_by_id(service_id: int) -> Service:
    """Get a service by id."""
    return Service.find_by_id(service_id)


