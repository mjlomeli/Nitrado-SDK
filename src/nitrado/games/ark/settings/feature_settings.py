

class FeatureSettings:
    def __init__(
            self,
            service_id: int,
            engine_settings: str = None,
            **kwargs
    ):
        self.engine_settings = engine_settings
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"

