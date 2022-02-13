import os
from nitrado import Service
from nitrado import Client


def set_client():
    url = "https://api.nitrado.net/"
    if Service.CLIENT:
        return Service.CLIENT
    if not Client.CLIENT:
        Client.CLIENT = Client(url, key=os.environ['NITRADO_KEY'])
    Service.CLIENT = Client.CLIENT


def test_services():
    services = Service.all()
    assert len(services) > 0


def test_logs():
    service = Service.all()[0]
    logs = service.logs()
    assert type(logs) == list


def test_tasks():
    service = Service.all()[0]
    tasks = service.tasks()
    assert type(tasks) == list


def test_notifications():
    service = Service.all()[0]
    notif = service.notifications()
    assert type(notif) == list


if __name__ == "__main__":
    access_token = os.environ.get('NITRADO_KEY')
    client = Client("https://api.nitrado.net/", access_token)
    Client.CLIENT = client
    Service.CLIENT = client

    test_services()
    test_notifications()
    test_logs()
    test_tasks()
