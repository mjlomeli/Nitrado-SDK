from __future__ import annotations


class Log:

    def __init__(
            self,
            service_id: int,
            category: str = None,
            severity: str = None,
            message: str = None,
            created_at: str = None,
            admin: bool = None,
            **kwargs
    ):
        self.category = category
        self.severity = severity
        self.created_at = created_at
        self.admin = admin
        self.message = message
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f'{k}={repr(v)}' for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"