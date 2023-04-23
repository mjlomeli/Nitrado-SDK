from datetime import datetime


class Notification:
    def __init__(
            self,
            id: int = None,
            service_id: int = None,
            type: str = None,
            level: str = None,
            error_id: bool = False,
            dismissed: bool = False,
            created_at: str = None,
            lifetime: bool = False,
            message: str = None,
            message_bbcode: str = None,
            message_long: str = None,
            message_long_bbcode: str = None,
            actions: list = None,
            data: dict = None,
            created_at_timestamp: int = None,
            **kwargs
    ):
        self.id = id
        self.service_id = service_id
        self.type = type
        self.level = level
        self.error_id = error_id
        self.dismissed = dismissed
        self.created_at = None if created_at is None else datetime.fromisoformat(created_at)
        self.lifetime = lifetime
        self.message = message
        self.message_bbcode = message_bbcode
        self.message_long = message_long
        self.message_long_bbcode = message_long_bbcode
        self.actions = actions
        self.data = data
        self.created_at_timestamp = created_at_timestamp
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f'{k}={repr(v)}' for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"
