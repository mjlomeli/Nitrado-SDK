import os
from requests import get, post, put, delete, Response
from dotenv import load_dotenv, dotenv_values
from .errors import assert_success
from requests.exceptions import ConnectionError, ConnectTimeout, Timeout

load_dotenv()


class Client:
    ENV_NAME = "NITRADO_API_KEY"
    NITRADO_API_URL = "https://api.nitrado.net"

    @classmethod
    def headers(cls) -> dict:
        if cls.ENV_NAME in dotenv_values():
            key = dotenv_values()[cls.ENV_NAME]
        elif cls.ENV_NAME in os.environ:
            key = os.getenv(cls.ENV_NAME)
        else:
            raise Exception(f"A Nitrado API must be provided as an environment variable: {cls.ENV_NAME}")
        return {'Authorization': f'Bearer {key}'}

    @classmethod
    def make_path(cls, path: str) -> str:
        return "{}{}".format(cls.NITRADO_API_URL, path)

    @classmethod
    def get_without_api_key(cls, path: str = None, params=None, **kwargs) -> Response:
        try:
            response = get(cls.make_path(path), params=params, **kwargs)
            assert_success(response)
            return response
        except ConnectTimeout:
            return cls.get_without_api_key(path=path, params=params, **kwargs)
        except ConnectionError:
            return cls.get_without_api_key(path=path, params=params, **kwargs)

    @classmethod
    def get(cls, path: str = None, params=None, **kwargs) -> Response:
        try:
            response = get(cls.make_path(path), headers=cls.headers(), params=params, **kwargs)
            assert_success(response)
            return response
        except ConnectTimeout:
            return cls.get(path=path, params=params, **kwargs)
        except ConnectionError:
            return cls.get(path=path, params=params, **kwargs)

    @classmethod
    def post_without_api_key(cls, path: str = None, params=None, **kwargs) -> Response:
        try:
            response = post(cls.make_path(path), params=params, **kwargs)
            assert_success(response)
            return response
        except ConnectTimeout:
            return cls.post_without_api_key(path=path, params=params, **kwargs)
        except ConnectionError:
            return cls.post_without_api_key(path=path, params=params, **kwargs)

    @classmethod
    def post(cls, path: str = None, params=None, **kwargs) -> Response:
        try:
            response = post(cls.make_path(path), headers=cls.headers(), params=params, **kwargs)
            assert_success(response)
            return response
        except ConnectTimeout:
            return cls.post(path=path, params=params, **kwargs)
        except ConnectionError:
            return cls.post(path=path, params=params, **kwargs)

    @classmethod
    def delete(cls, path: str = None, params=None, **kwargs) -> Response:
        try:
            response = delete(cls.make_path(path), headers=cls.headers(), params=params, **kwargs)
            assert_success(response)
            return response
        except ConnectTimeout:
            return cls.delete(path=path, params=params, **kwargs)
        except ConnectionError:
            return cls.delete(path=path, params=params, **kwargs)

    @classmethod
    def put(cls, path: str = None, params=None, **kwargs) -> Response:
        try:
            response = put(cls.make_path(path), headers=cls.headers(), params=params, **kwargs)
            assert_success(response)
            return response
        except ConnectTimeout:
            return cls.put(path=path, params=params, **kwargs)
        except ConnectionError:
            return cls.put(path=path, params=params, **kwargs)
