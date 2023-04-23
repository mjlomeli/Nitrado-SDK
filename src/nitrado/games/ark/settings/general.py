
class General:
    @classmethod
    def from_data(cls, service_id: int, **kwargs):
        return cls(service_id, **{k.lower().replace('-', '_'): v for k, v in kwargs.items()})

    def __init__(
            self,
            service_id: int,
            expertmode: str = None,
            battleye: str = None,
            server_language: str = None,
            vday: str = None,
            mod_update_list: str = None,
            mod_status_list: str = None,
            gameplay_log: str = None,
            force_allow_cave_flyers: str = None,
            vac: str = None,
            gamesettings_saved_utc_timestamp_hidden: str = None,
            automatic_update_mechanism: str = None,
            clusterid: str = None,
            enablecluster: str = None,
            primitiveplus: str = None,
            enable_idle_player_kick: str = None,
            no_anti_speed_hack: str = None,
            no_biome_walls: str = None,
            notify_admin_commands_in_chat: str = None,
            metrics: str = None,
            crossplay: str = None,
            activeevent: str = None,
            structurememopts: str = None,
            noundermeshchecking: str = None,
            noundermeshkilling: str = None,
            newyearevent: str = None,
            useitemdupecheck: str = None,
            **kwargs
    ):
        self.expertmode = expertmode
        self.battleye = battleye
        self.server_language = server_language
        self.vday = vday
        self.mod_update_list = mod_update_list
        self.mod_status_list = mod_status_list
        self.gameplay_log = gameplay_log
        self.force_allow_cave_flyers = force_allow_cave_flyers
        self.vac = vac
        self.gamesettings_saved_utc_timestamp_hidden = gamesettings_saved_utc_timestamp_hidden
        self.automatic_update_mechanism = automatic_update_mechanism
        self.clusterid = clusterid
        self.enablecluster = enablecluster
        self.primitiveplus = primitiveplus
        self.enable_idle_player_kick = enable_idle_player_kick
        self.no_anti_speed_hack = no_anti_speed_hack
        self.no_biome_walls = no_biome_walls
        self.notify_admin_commands_in_chat = notify_admin_commands_in_chat
        self.metrics = metrics
        self.crossplay = crossplay
        self.activeevent = activeevent
        self.structurememopts = structurememopts
        self.noundermeshchecking = noundermeshchecking
        self.noundermeshkilling = noundermeshkilling
        self.newyearevent = newyearevent
        self.useitemdupecheck = useitemdupecheck
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"

