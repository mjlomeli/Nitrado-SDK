
class Details:
    def __init__(
            self,
            service_id: int,
            address: str = None,
            name: str = None,
            game: str = None,
            portlist_short: str = None,
            folder_short: str = None,
            slots: int = 0,
            **kwargs
    ):
        self.address = address
        self.name = name
        self.game = game
        self.portlist_short = portlist_short
        self.folder_short = folder_short
        self.slots = slots
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        name = f"name={repr(self.name)}"
        slots = f"slots={repr(self.slots)}"
        game = f"game={repr(self.game)}"
        params = [s for s in [name, slots, game]]
        return f"<{self.__class__.__name__}({', '.join(params)}, ...)>"
