class Action:
    def __init__(self, service_id: int, title: str = None, type: str = None, url: str = None, **kwargs):
        self.title = title
        self.type = type
        self.url = url
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f'{k}={repr(v)}' for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"
