from tests.mocked_client.mocked_client import MockedClient

URL = "https://api.nitrado.net/"


def test_get():
    client = MockedClient(URL)
    response = client.get('/services')
    assert 'status' in response.json()
    assert 'data' in response.json()


def test_post():
    client = MockedClient(URL)
    response = client.get('/services')
    assert 'status' in response.json()
    assert 'data' in response.json()


def test_delete():
    client = MockedClient(URL)
    response = client.get('/services')
    assert 'status' in response.json()
    assert 'data' in response.json()


def test_put():
    client = MockedClient(URL)
    response = client.get('/services')
    assert 'status' in response.json()
    assert 'data' in response.json()
