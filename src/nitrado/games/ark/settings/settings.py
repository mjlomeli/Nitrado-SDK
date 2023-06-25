from __future__ import annotations
from .config import Config
from .feature_settings import FeatureSettings
from .general import General
from .start_param import StartParam
from .game_ini import GameIni


class Settings:
    @classmethod
    def keys_to_snakecase(cls, data: dict) -> dict:
        return {
            "config": data['config'],
            "gameini": data['gameini'],
            "features": data['features'],
            "general": data['general'],
            "start_param": data['start-param'],
            "append": None if "append" in data else data['append']
        }

    def __init__(
            self,
            service_id: int = None,
            config: dict = None,
            gameini: dict = None,
            features: dict = None,
            append: dict = None,
            general: dict = None,
            start_param: dict = None,
            **kwargs
    ):
        self.service_id = service_id
        self.config = Config(service_id=service_id, **Config.keys_to_snakecase(config))
        self.gameini = GameIni(service_id=service_id, **GameIni.keys_to_snake_case(gameini))
        self.features = FeatureSettings(service_id=service_id, **FeatureSettings.keys_to_snakecase(features))
        self.append = append
        self.general = General(service_id=service_id, **General.keys_to_snakecase(general))
        self.start_param = start_param and StartParam(service_id=service_id, **StartParam.keys_to_snakecase(start_param))

        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"

