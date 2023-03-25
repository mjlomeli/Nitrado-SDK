from nitrado import Service
from tests.mocked_client import MockedClient


def get_client():
    url = "https://api.nitrado.net/"
    return MockedClient(url)


def get_a_service():
    client = get_client()
    data = {
        "id": 1,
        "location_id": 3,
        "status": "active",
        "websocket_token": "41e4b1157551195144ceaf0677d2",
        "user_id": 1234567,
        "comment": None,
        "auto_extension": False,
        "auto_extension_duration": 720,
        "auto_extension_external": False,
        "type": "gameserver",
        "type_human": "Publicserver 20 Slots",
        "managedroot_id": None,
        "details": {
            "address": "5.62.66.117:10020",
            "name": "[US] - Arkpocalypse - Island",
            "game": "ARK: Survival Evolved (Xbox One)",
            "portlist_short": "arkxb",
            "folder_short": "arkxb",
            "slots": 20
        },
        "start_date": "2023-01-02T21:18:43",
        "suspend_date": "2023-04-03T05:21:17",
        "delete_date": "2023-04-10T05:21:17",
        "suspending_in": 766277,
        "deleting_in": 1371077,
        "username": "ni1234567_1",
        "roles": [
            "ROLE_OWNER"
        ]
    }
    try:
        return Service(client, data)
    except Exception:
        raise Exception(f"Service could not be constructed with data: {data}")


def test_services():
    services = get_a_service()
    assert services.id == 1
    assert services.type == "gameserver"
    assert services.start_date == "2023-01-02T21:18:43"
    assert services.suspend_date == "2023-04-03T05:21:17"
    assert services.delete_date == "2023-04-10T05:21:17"
    assert services.username == "ni1234567_1"


def test_logs():
    service = get_a_service()
    logs = service.logs()
    assert type(logs) == list
    assert len(logs) == 40


def test_tasks():
    service = get_a_service()
    tasks = service.tasks()
    assert type(tasks) == list
    assert tasks == [{'id': 8394912, 'status': 'error', 'minute': '5', 'hour': '3', 'day': '*', 'month': '*', 'weekday': '*', 'next_run': '2023-03-11T03:05:00', 'last_run': '2023-03-10T03:05:16', 'timezone': 'America/Los_Angeles', 'action_method': 'game_server_restart', 'action_data': None}]


def test_notifications():
    service = get_a_service()
    notifications = service.notifications()
    assert type(notifications) == list
    assert notifications == []


