from nitrado import Client
import os


def get_client():
    if Client.CLIENT:
        return Client.CLIENT
    url = "https://api.nitrado.net/"
    key = os.getenv('NITRADO_KEY')
    return Client(url, key)


def test_ping():
    client = get_client()
    ping_json = client.get('ping')
    assert ping_json is not None
    assert 'status' in ping_json
    assert ping_json['status'] == 'success'


def test_maintenance():
    client = get_client()
    maint = client.get('maintenance')
    assert maint is not None
    assert 'status' in maint
    assert maint['status'] == 'success'


def test_version():
    client = get_client()
    version = client.get('version')
    assert version is not None
    assert 'status' in version
    assert version['status'] == 'success'


def test():
    test_ping()
    test_version()
    test_maintenance()


if __name__ == "__main__":
    test()
    print("passing")

