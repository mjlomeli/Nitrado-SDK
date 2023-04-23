from datetime import datetime


class Players:
    def __init__(
            self,
            service_id: int,
            name: str = None,
            id: str = None,
            id_type: str = None,
            online: bool = False,
            actions: list = None,
            last_online: str = None,
            **kwargs
    ):
        self.name = name
        self.id = id
        self.id_type = id_type
        self.online = online
        self.actions = actions or []
        self.last_online: datetime = None if last_online is None else datetime.fromisoformat(last_online)
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        name = f"name={repr(self.name)}"
        online = f"online={repr(self.online)}"
        params = [s for s in [name, online]]
        return f"<{self.__class__.__name__}({', '.join(params)})>"
