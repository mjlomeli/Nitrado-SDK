from __future__ import annotations
from datetime import datetime
from ..lib.client import Client
from ..lib.errors import assert_success
from dotenv import dotenv_values
import os
from requests import get


class Token:
    @classmethod
    def from_api_token(cls, api_key: str = None) -> Token:
        """Gets api token from parameters or .env variables if not provided"""
        path = '/token'
        if api_key is not None:
            key = api_key
        elif Client.ENV_NAME in dotenv_values():
            key = dotenv_values()[Client.ENV_NAME]
        elif Client.ENV_NAME in os.environ:
            key = os.environ[Client.ENV_NAME]
        else:
            return Token()
        headers = {'Authorization': f'Bearer {key}'}
        try:
            response = get(Client.make_path(path), headers=headers)
            assert_success(response)
            kwargs: dict = response.json()
            if 'data' in kwargs and 'status' in kwargs and kwargs['status'] == 'success':
                return Token.from_data(kwargs['data'])
        except Exception:
            pass
        return Token()

    @classmethod
    def from_data(cls, data: dict) -> Token:
        token = data['token']
        return cls(
            id=token['id'],
            user_id=token['user']['id'],
            username=token['user']['username'],
            expires_at=token['expires_at'],
            valid_until=token['valid_until'],
            scopes=token['scopes'],
            two_factor_method=token['two_factor_method'],
            employee=token['employee'],
            valid=True,
        )

    def __init__(
            self,
            id: int = None,
            user_id: int = None,
            username: str = None,
            expires_at: int = None,
            valid_until: str = None,
            two_factor_method: str = None,
            scopes: list = None,
            employee: bool = False,
            valid: bool = False,
            **kwargs
    ):
        self.id = id
        self.user_id = user_id
        self.username = username
        self.expires_at = expires_at
        self.valid_until = None if valid_until is None else datetime.fromisoformat(valid_until)
        self.two_factor_method = two_factor_method
        self.scopes = scopes or []
        self.employee = employee
        self.valid = valid
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        username = f"username={repr(self.username)}"
        valid = f"valid={repr(self.valid)}"
        expires = f"expires_at={repr(self.expires_at)}"
        params = [s for s in [username, valid, expires]]
        return f"<{self.__class__.__name__}({', '.join(params)})>"
