"""
Tests Nitrado connections. If any fail, then this means any of the following:
    - something is wrong with Nitrado
    - the URLs are no longer valid
    - responses from Nitrado has changed
"""
from nitrado.lib import Client




def test_ping():
    path = '/ping'
    try:
        response = Client.get(path)
        json: dict = response.json()
        error_message = f"The url no longer has access to 'status' and 'message' from api request: /{path}"
        assert 'status' in json and 'message' in json, error_message
        api_error_message = 'message' in json or f"Nitrado's api is down or the url is invalid: /{path}"
        assert json['status'] == 'success', api_error_message
    except Exception:
        raise Exception(f"Nitrado's api is down or the url is invalid: /{path}")


def test_maintenance():
    path = '/maintenance'
    try:
        response = Client.get(path)
        json: dict = response.json()
        error_message = f"The url no longer has access to 'status' and 'data' from api request: /{path}"
        assert 'status' in json and 'data' in json, error_message
        api_error_message = 'message' in json or f"Nitrado's api is down or the url is invalid: /{path}"
        assert json['status'] == 'success', api_error_message
    except Exception:
        raise Exception(f"Nitrado's api is down or the url is invalid: /{path}")


def test_version():
    path = "/version"
    try:
        response = Client.get(path)
        json: dict = response.json()
        error_message = f"The url no longer has access to 'status' and 'message' from api request: /{path}"
        assert 'status' in json and 'message' in json, error_message
        api_error_message = 'message' in json or f"Nitrado's api is down or the url is invalid: /{path}"
        assert json['status'] == 'success', api_error_message
    except Exception:
        raise Exception(f"Nitrado's api is down or the url is invalid: /{path}")

