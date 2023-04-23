
class Query:
    def __init__(
            self,
            service_id: int,
            server_name: str = None,
            connect_ip: str = None,
            map: str = None,
            version: str = None,
            player_current: int = None,
            player_max: int = None,
            players: list = None,
            **kwargs
    ):
        self.server_name = server_name
        self.connect_ip = connect_ip
        self.map = map
        self.version = version
        self.player_current = player_current
        self.player_max = player_max
        self.players = players
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"

