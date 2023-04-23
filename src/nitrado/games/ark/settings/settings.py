from __future__ import annotations
from .config import Config
from .feature_settings import FeatureSettings
from .general import General
from .start_param import StartParam
from .game_ini import GameIni


class Settings:
    @classmethod
    def from_data(cls, service_id: int, **kwargs) -> Settings:
        kwargs['config'] = Config.from_data(service_id, **kwargs['config'])
        kwargs['features'] = FeatureSettings(service_id, **kwargs['features'])
        kwargs['general'] = General.from_data(service_id, **kwargs['general'])
        kwargs['start_param'] = StartParam.from_data(service_id, **kwargs['start-param'])
        kwargs['gameini'] = GameIni.from_data(service_id, **kwargs['gameini'])
        return cls(service_id, **kwargs)

    def __init__(
            self,
            service_id: int,
            config: Config = None,
            gameini: GameIni = None,
            features: FeatureSettings = None,
            append: dict = None,
            general: General = None,
            start_param: StartParam = None,
            **kwargs
    ):
        self.config = config
        self.gameini = gameini
        self.features = features
        self.append = append
        self.general = general
        self.start_param = start_param
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"

