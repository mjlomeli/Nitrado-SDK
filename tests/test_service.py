import json
import os
from src import Service
from src.example_package.client import Client


def pretty_json(data: dict):
    return json.dumps(data, indent=3, sort_keys=True)


def test_service_list():
    services = Service.all()
    print("#############   Services    ################")
    for service in services:
        print(service)
        print("\n")
    print("\n")


def test_service_details():
    service = Service.all()[0]
    print("#############   DETAILS    ################")
    print(pretty_json(service.details))
    print("\n")


def test_service_logs():
    service = Service.all()[0]
    print("#############   LOGS    ################")
    print(pretty_json(service.logs()))
    print("\n")


def test_service_tasks():
    service = Service.all()[0]
    print("#############   Tasks    ################")
    print(pretty_json(service.tasks()))
    print("\n")


if __name__ == "__main__":
    access_token = os.environ.get('NITRADO_KEY')
    client = Client("https://api.nitrado.net/", access_token)
    Client.CLIENT = client
    Service.CLIENT = client

    test_service_details()
    test_service_list()
    test_service_logs()
    test_service_tasks()
