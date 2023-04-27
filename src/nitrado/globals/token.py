from __future__ import annotations
from datetime import datetime


class Token:
    @classmethod
    def from_data(cls, data: dict):
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
