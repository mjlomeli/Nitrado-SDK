import requests
from requests import Response


def assert_response_is_ok(response: Response):
    if not response.ok:
        code = response.status_code
        reason = response.reason
        url = response.url
        raise requests.RequestException(f"[{code} Error]: {reason} ({url})")


def assert_response_is_json(response: Response):
    headers = response.headers
    if 'Content-Type' not in headers and 'application/json' not in headers['Content-Type']:
        raise requests.RequestException(f"[JSON Error]: The response did not reply in JSON format ({response.url})")


def assert_response_is_nitrado_data(response: Response):
    data = response.json()
    if 'status' not in data:
        message = f"[Nitrado Data Error]: Response data does not match Nitrado's data standard ({response.url})"
        hint = "[Hint]: Data must be a JSON with keys containing ['status', (optional) 'message', (optional) 'data']"
        raise requests.RequestException(f"{message}\n{hint}")


def assert_success(response: Response):
    assert_response_is_ok(response)
    assert_response_is_json(response)
    assert_response_is_nitrado_data(response)
    data = response.json()

    if data['status'] != 'success':
        raise requests.RequestException(f"[Nitrado Error]: {data['message']} ({response.url})")

