
class General:
    @classmethod
    def keys_to_snakecase(cls, data: dict) -> dict:
        return {
            'expert_mode': data['expertMode'],
            'battleye': data['battleye'],
            'server_language': data['server-language'],
            'vday': data['vday'],
            'mod_update_list': data['mod-update-list'],
            'mod_status_list': data['mod-status-list'],
            'gameplay_log': data['gameplay-log'],
            'force_allow_cave_flyers': data['force-allow-cave-flyers'],
            'vac': data['vac'],
            'gamesettings_saved_utc_timestamp_hidden': data['gamesettings_saved_utc_timestamp_hidden'],
            'automatic_update_mechanism': data['automatic-update-mechanism'],
            'clusterid': data['clusterid'],
            'enablecluster': data['enablecluster'],
            'primitive_plus': data['PrimitivePlus'],
            'enable_idle_player_kick': data['enable-idle-player-kick'],
            'no_anti_speed_hack': data['no-anti-speed-hack'],
            'no_biome_walls': data['no-biome-walls'],
            'notify_admin_commands_in_chat': data['notify-admin-commands-in-chat'],
            'metrics': data['metrics'],
            'cross_play': data['CrossPlay'],
            'active_event': data['ActiveEvent'],
            'structurememopts': data['structurememopts'],
            'noundermeshchecking': data['noundermeshchecking'],
            'noundermeshkilling': data['noundermeshkilling'],
            'new_year_event': data['NewYearEvent'],
            'useitemdupecheck': data['useitemdupecheck'],
        }

    def __init__(
            self,
            service_id: int = None,
            expert_mode: str = None,
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
            primitive_plus: str = None,
            enable_idle_player_kick: str = None,
            no_anti_speed_hack: str = None,
            no_biome_walls: str = None,
            notify_admin_commands_in_chat: str = None,
            metrics: str = None,
            cross_play: str = None,
            active_event: str = None,
            structurememopts: str = None,
            noundermeshchecking: str = None,
            noundermeshkilling: str = None,
            new_year_event: str = None,
            useitemdupecheck: str = None,
            **kwargs
    ):
        self.service_id = service_id
        self.expert_mode = expert_mode
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
        self.primitive_plus = primitive_plus
        self.enable_idle_player_kick = enable_idle_player_kick
        self.no_anti_speed_hack = no_anti_speed_hack
        self.no_biome_walls = no_biome_walls
        self.notify_admin_commands_in_chat = notify_admin_commands_in_chat
        self.metrics = metrics
        self.cross_play = cross_play
        self.active_event = active_event
        self.structurememopts = structurememopts
        self.noundermeshchecking = noundermeshchecking
        self.noundermeshkilling = noundermeshkilling
        self.new_year_event = new_year_event
        self.useitemdupecheck = useitemdupecheck
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"

