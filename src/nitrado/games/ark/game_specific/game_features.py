
class GameFeatures:
    def __init__(
            self,
            service_id: int = None,
            has_backups: bool = False,
            has_world_backups: bool = False,
            has_rcon: bool = False,
            has_application_server: bool = False,
            has_container_websocket: bool = False,
            has_file_browser: bool = False,
            has_ftp: bool = False,
            has_expert_mode: bool = False,
            has_packages: bool = False,
            has_plugin_system: bool = False,
            has_restart_message_support: bool = False,
            has_database: bool = False,
            has_playermanagement_feature: bool = False,
            has_curseforge_workshop: bool = False,
            **kwargs
    ):
        self.has_backups = has_backups
        self.has_world_backups = has_world_backups
        self.has_rcon = has_rcon
        self.has_application_server = has_application_server
        self.has_container_websocket = has_container_websocket
        self.has_file_browser = has_file_browser
        self.has_ftp = has_ftp
        self.has_expert_mode = has_expert_mode
        self.has_packages = has_packages
        self.has_plugin_system = has_plugin_system
        self.has_restart_message_support = has_restart_message_support
        self.has_database = has_database
        self.has_playermanagement_feature = has_playermanagement_feature
        self.has_curseforge_workshop = has_curseforge_workshop
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"

