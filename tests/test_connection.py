"""
Tests Nitrado connections. If any fail, then this means any of the following:
    - something is wrong with Nitrado
    - the URLs are no longer valid
    - responses from Nitrado has changed
"""
from nitrado import Client
import os

URL = "https://api.nitrado.net/"


def get_client():
    key = os.getenv('NITRADO_KEY')
    return Client(URL, key)


def test_ping():
    path = 'ping'
    client = get_client()
    try:
        json = client.get(path)
        error_message = f"The url no longer has access to 'status' and 'message' from api request: {URL}/{path}"
        assert 'status' in json and 'message' in json, error_message
        api_error_message = 'message' in json or f"Nitrado's api is down or the url is invalid: {URL}/{path}"
        assert json['status'] == 'success', api_error_message
    except Exception:
        raise Exception(f"Nitrado's api is down or the url is invalid: {URL}/{path}")


def test_maintenance():
    path = 'maintenance'
    client = get_client()
    try:
        json = client.get(path)
        error_message = f"The url no longer has access to 'status' and 'data' from api request: {URL}/{path}"
        assert 'status' in json and 'data' in json, error_message
        api_error_message = 'message' in json or f"Nitrado's api is down or the url is invalid: {URL}/{path}"
        assert json['status'] == 'success', api_error_message
    except Exception:
        raise Exception(f"Nitrado's api is down or the url is invalid: {URL}/{path}")


def test_version():
    path = "version"
    client = get_client()
    try:
        json = client.get(path)
        error_message = f"The url no longer has access to 'status' and 'message' from api request: {URL}/{path}"
        assert 'status' in json and 'message' in json, error_message
        api_error_message = 'message' in json or f"Nitrado's api is down or the url is invalid: {URL}/{path}"
        assert json['status'] == 'success', api_error_message
    except Exception:
        raise Exception(f"Nitrado's api is down or the url is invalid: {URL}/{path}")

