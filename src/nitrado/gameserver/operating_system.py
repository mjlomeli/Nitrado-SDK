

class OperatingSystem:
    def __init__(
            self,
            service_id: int,
            hostname: str = None,
            servername: str = None,
            status: str = None,
            **kwargs
    ):
        self.hostname = hostname
        self.servername = servername
        self.status = status
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"
