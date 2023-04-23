import json
from enum import Enum
from pathlib import Path


class RequestType(Enum):
    GET = 1
    POST = 2
    DELETE = 3
    PUT = 4


def get_responses_dir() -> Path:
    return Path.cwd() / Path('tests/mocked_client/responses/Nitrado')


class MockedResponse:
    @staticmethod
    def __get_data(url: str, request_type: RequestType):
        home_dir = get_responses_dir()
        assert home_dir.exists(), f"Mocked responses directory for Nitrado doesn't exist: {get_responses_dir()}"
        path_dir = home_dir / Path(url[1:])
        assert path_dir.exists(), f"Mocked responses directory for Nitrado doesn't exist: {path_dir}"
        path = path_dir / Path(request_type.name + '.json')
        if not path.exists():
            raise Exception(f"The MockedClient is missing mocked data at: {path}")
        with open(path, 'r') as r:
            return json.load(r)

    def __init__(self, url: str, request_type: RequestType):
        self.__json_data = None
        self.status_code = 404
        self.headers = None
        self.url = None
        self.ok = False
        if url:
            data = self.__get_data(url, request_type)
            assert any(['GET'])
            self.__json_data = 'json' in data and data['json'] or None
            self.status_code = 'status_code' in data and data['status_code'] or 404
            self.headers = 'headers' in data and data['headers'] or None
            self.url = 'url' in data and data['url'] or None
            self.ok = 'ok' in data and data['ok'] or self.status_code == 200

    def json(self):
        return self.__json_data

    def __repr__(self):
        return f"<MockedResponse(status_code={self.status_code})>"


class MockedRequests:
    @classmethod
    def get(cls, path: str, headers: dict = None, data=None, params=None):
        return MockedResponse(path, RequestType.GET)

    @classmethod
    def post(cls, path: str, headers: dict = None, data=None, params=None):
        return MockedResponse(path, RequestType.GET)

    @classmethod
    def put(cls, path: str, headers: dict = None, data=None, params=None):
        return MockedResponse(path, RequestType.GET)

    @classmethod
    def delete(cls, path: str, headers: dict = None, data=None, params=None):
        return MockedResponse(path, RequestType.GET)


class MockedClient:

    @classmethod
    def make_path(cls, path: list or str = None):
        if isinstance(path, str):
            return "{}".format(path)
        elif isinstance(path, list):
            path_list = [str(directory) for directory in path]
            return "{}".format('/'.join(path_list))
        else:
            return ''

    @classmethod
    def get(cls, path: str = None, params=None, **kwargs):
        return MockedRequests.get(cls.make_path(path))

    @classmethod
    def post(cls, path: str = None, params=None, **kwargs):
        return MockedRequests.post(cls.make_path(path))

    @classmethod
    def delete(cls, path: str = None, params=None, **kwargs):
        return MockedRequests.delete(cls.make_path(path))

    @classmethod
    def put(cls, path: str = None, params=None, **kwargs):
        return MockedRequests.put(cls.make_path(path))

