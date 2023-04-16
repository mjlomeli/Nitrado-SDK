from requests import get, post, put, delete, Response
from nitrado.lib.errors import assert_success


class Client:
    def __init__(self, url: str, key: str = None):
        assert type(url) == str, "A string url must be provided in Client(api_url, key)"
        assert "http" in url, "Nitrado's API url should include 'http://' or 'https://'"
        self.url = url if url[-1] != '/' else url[:-1]
        self.headers = {}
        if key is not None:
            self.headers = {'Authorization': key}

    def make_path(self, path: str) -> str:
        return "{}{}".format(self.url, path)

    def get(self, path: str = None, data: dict = None, params=None) -> Response:
        response = get(self.make_path(path), headers=self.headers, data=data, params=params)
        assert_success(response)
        return response

    def post(self, path: str = None, data: dict = None, params=None) -> Response:
        response = post(self.make_path(path), headers=self.headers, data=data, params=params)
        assert_success(response)
        return response

    def delete(self, path: str = None, data: dict = None, params=None) -> Response:
        response = delete(self.make_path(path), headers=self.headers, data=data, params=params)
        assert_success(response)
        return response

    def put(self, path: str = None, data: dict = None, params=None) -> Response:
        response = put(self.make_path(path), headers=self.headers, data=data, params=params)
        assert_success(response)
        return response
