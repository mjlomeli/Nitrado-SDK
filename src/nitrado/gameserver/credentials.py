

class Credentials:
    def __init__(
            self,
            service_id: int,
            ftp: str = None,
            mysql: str = None,
            **kwargs
    ):
        self.ftp = ftp
        self.mysql = mysql
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"
