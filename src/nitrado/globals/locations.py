class Location:
    def __init__(
            self,
            id: int = None,
            country: str = None,
            city: str = None,
            **kwargs
    ):
        self.id = id
        self.country = country
        self.city = city
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __str__(self):
        return self.country or ''

    def __repr__(self):
        country = f"country={repr(self.country)}"
        city = f"city={repr(self.city)}"
        params = [s for s in [country, city]]
        return f"<{self.__class__.__name__}({', '.join(params)})>"
