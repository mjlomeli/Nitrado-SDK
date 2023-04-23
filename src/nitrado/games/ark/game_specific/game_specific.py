from __future__ import annotations
from .game_features import GameFeatures


class GameSpecific:
    @classmethod
    def from_data(cls, service_id: int, **kwargs) -> GameSpecific:
        kwargs['features'] = GameFeatures(service_id, **kwargs['features'])
        return cls(service_id, **kwargs)

    def __init__(
            self,
            service_id: int,
            path: str = None,
            update_status: str = None,
            last_update: str = None,
            path_available: bool = None,
            features: GameFeatures = None,
            log_files: list = None,
            config_files: list = None,
            curseforge_customer_settings: str = None,
            **kwargs
    ):
        self.path = path
        self.update_status = update_status
        self.last_update = last_update
        self.path_available = path_available
        self.features = features
        self.log_files = log_files
        self.config_files = config_files
        self.curseforge_customer_settings = curseforge_customer_settings
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"

