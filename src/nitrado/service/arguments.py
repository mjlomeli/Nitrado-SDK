class Arguments:
    def __init__(
            self,
            service_id: int,
            privacystatus: str = None,
            last_rental_time: str = None,
            startgame: str = None,
            startport: str = None,
            amount: str = None,
            limit_game_tags: str = None,
            wiuser: str = None,
            **kwargs
    ):
        self.privacystatus = privacystatus
        self.last_rental_time = last_rental_time
        self.startgame = startgame
        self.startport = startport
        self.amount = amount
        self.limit_game_tags = limit_game_tags
        self.wiuser = wiuser
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f'{k}={repr(v)}' for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"

