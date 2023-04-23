from nitrado import Service
from tests.mocked_client import MockedClient as Client




def get_a_service():
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
        return Service(**data)
    except Exception:
        raise Exception(f"Service could not be constructed with data: {data}")


def test_services():
    services = get_a_service()
    assert services.id == 1
    assert services.type == "gameserver"
    assert str(services.start_date) == "2023-01-02 21:18:43"
    assert str(services.suspend_date) == "2023-04-03 05:21:17"
    assert str(services.delete_date) == "2023-04-10 05:21:17"
    assert services.username == "ni1234567_1"


