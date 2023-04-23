from tests.mocked_client.mocked_client import MockedClient as Client

URL = "https://api.nitrado.net/"


def test_get():
    response = Client.get('/services')
    assert 'status' in response.json()
    assert 'data' in response.json()


def test_post():
    response = Client.get('/services')
    assert 'status' in response.json()
    assert 'data' in response.json()


def test_delete():
    response = Client.get('/services')
    assert 'status' in response.json()
    assert 'data' in response.json()


def test_put():
    response = Client.get('/services')
    assert 'status' in response.json()
    assert 'data' in response.json()
