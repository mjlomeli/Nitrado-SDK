import os
from requests import get, post, put, delete, Response
from dotenv import load_dotenv, dotenv_values
from .errors import assert_success

load_dotenv()


class Client:
    ENV_NAME = "NITRADO_API_KEY"
    NITRADO_API_URL = "https://api.nitrado.net"

    @classmethod
    def initialize(cls, api_key: str):
        """Saves the Nitrado API key in a local .env file"""
        with open('.env', 'r+') as r:
            content = []
            found = False
            for line in r.readlines():
                if line.find(f'{cls.ENV_NAME}=') == 0:
                    content += [f"{cls.ENV_NAME}={api_key}\n"]
                    found = True
                else:
                    content += [line]
            if not found:
                content = [f"{cls.ENV_NAME}={api_key}\n"] + content
            r.seek(0)
            r.write(''.join(content))
            load_dotenv()

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
    def get(cls, path: str = None, params=None, **kwargs) -> Response:
        response = get(cls.make_path(path), headers=cls.headers(), params=params, **kwargs)
        assert_success(response)
        return response

    @classmethod
    def post(cls, path: str = None, params=None, **kwargs) -> Response:
        response = post(cls.make_path(path), headers=cls.headers(), params=params, **kwargs)
        assert_success(response)
        return response

    @classmethod
    def delete(cls, path: str = None, params=None, **kwargs) -> Response:
        response = delete(cls.make_path(path), headers=cls.headers(), params=params, **kwargs)
        assert_success(response)
        return response

    @classmethod
    def put(cls, path: str = None, params=None, **kwargs) -> Response:
        response = put(cls.make_path(path), headers=cls.headers(), params=params, **kwargs)
        assert_success(response)
        return response
