from tests.mocked_client.mocked_client import MockedClient

URL = "https://api.nitrado.net/"


def test_get():
    client = MockedClient(URL)
    json = client.get('services')
    assert 'status' in json
    assert 'data' in json


def test_post():
    client = MockedClient(URL)
    json = client.get('services')
    assert 'status' in json
    assert 'data' in json


def test_delete():
    client = MockedClient(URL)
    json = client.get('services')
    assert 'status' in json
    assert 'data' in json


def test_put():
    client = MockedClient(URL)
    json = client.get('services')
    assert 'status' in json
    assert 'data' in json
