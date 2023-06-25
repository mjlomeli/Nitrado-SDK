
class Config:
    @classmethod
    def keys_to_snakecase(cls, data: dict) -> dict:
        return {
            'activate_admin_logs': data['activateAdminLogs'],
            'pve_dino_decay_period_multiplier': data['PvEDinoDecayPeriodMultiplier'],
            'player_character_water_drain_multiplier': data['PlayerCharacterWaterDrainMultiplier'],
            'time_to_collapse_rod': data['TimeToCollapseROD'],
            'harvest_amount_multiplier': data['HarvestAmountMultiplier'],
            'admin_list': data['admin-list'],
            'per_platform_max_structures_multiplier': data['PerPlatformMaxStructuresMultiplier'],
            'active_mods': data['active-mods'],
            'disable_death_spectator': data['DisableDeathSpectator'],
            'only_decay_unsnapped_core_structures': data['OnlyDecayUnsnappedCoreStructures'],
            'structure_destruction_tag': data['StructureDestructionTag'],
            'battle_sudden_death_interval': data['BattleSuddenDeathInterval'],
            'disable_structure_decay_pve': data['disable-structure-decay-pve'],
            'disable_dino_riding': data['DisableDinoRiding'],
            'allow_cave_building_pve': data['AllowCaveBuildingPvE'],
            'disable_dino_decay_pve': data['DisableDinoDecayPvE'],
            'random_supply_crate_points': data['RandomSupplyCratePoints'],
            'cryopod_nerf_duration': data['CryopodNerfDuration'],
            'game_log_buffer': data['gameLogBuffer'],
            'prevent_download_dinos': data['prevent-download-dinos'],
            'battle_auto_start_game_interval': data['BattleAutoStartGameInterval'],
            'exlusivejoin': data['exlusivejoin'],
            'map_mod_id': data['map-mod-id'],
            'only_admin_rejoin_as_spectator': data['OnlyAdminRejoinAsSpectator'],
            'allow_cave_building_pvp': data['AllowCaveBuildingPvP'],
            'hardcore': data['hardcore'],
            'default_map': data['default-map'],
            'cryopod_nerf_damage_mult': data['CryopodNerfDamageMult'],
            'allow_hide_damage_source_from_logs': data['AllowHideDamageSourceFromLogs'],
            'players_join_no_check_list': data['players-join-no-check-list'],
            'player_on_map': data['player-on-map'],
            'xp_multiplier': data['XPMultiplier'],
            'prevent_download_items': data['prevent-download-items'],
            'player_resistance_multiplier': data['PlayerResistanceMultiplier'],
            'battle_auto_restart_game_interval': data['BattleAutoRestartGameInterval'],
            'force_respawn_dinos': data['ForceRespawnDinos'],
            'b_show_status_notification_messages': data['bShowStatusNotificationMessages'],
            'clamp_resource_harvest_damage': data['ClampResourceHarvestDamage'],
            'dino_damage_multiplier': data['DinoDamageMultiplier'],
            'dino_character_health_recovery_multiplier': data['DinoCharacterHealthRecoveryMultiplier'],
            'player_character_food_drain_multiplier': data['PlayerCharacterFoodDrainMultiplier'],
            'day_cycle_speed_scale': data['DayCycleSpeedScale'],
            'server_name': data['server-name'],
            'difficulty_offset': data['difficulty-offset'],
            'restart_countdown_seconds': data['restart-countdown-seconds'],
            'motd_duration': data['motd-duration'],
            'disable_weather_fog': data['DisableWeatherFog'],
            'activate_admin_tribe_logs': data['activateAdminTribeLogs'],
            'taming_speed_multiplier': data['TamingSpeedMultiplier'],
            'tribute_dino_expiration_seconds': data['TributeDinoExpirationSeconds'],
            'player_character_health_recovery_multiplier': data['PlayerCharacterHealthRecoveryMultiplier'],
            'no_tribute_downloads': data['no-tribute-downloads'],
            'battle_num_of_tribes_to_start_game': data['BattleNumOfTribesToStartGame'],
            'enable_pvp_gamma': data['enable-pvp-gamma'],
            'disable_pve_gamma': data['DisablePvEGamma'],
            'leave_messages': data['leave-messages'],
            'active_total_conversion': data['active-total-conversion'],
            'map_expert': data['map-expert'],
            'allow_tek_suit_powers_in_genesis': data['AllowTekSuitPowersInGenesis'],
            'max_personal_tamed_dinos': data['MaxPersonalTamedDinos'],
            'dino_character_food_drain_multiplier': data['DinoCharacterFoodDrainMultiplier'],
            'day_time_speed_scale': data['DayTimeSpeedScale'],
            'map': data['map'],
            'spectator_password': data['SpectatorPassword'],
            'prevent_download_survivors': data['prevent-download-survivors'],
            'start_with_backup': data['start-with-backup'],
            'night_time_speed_scale': data['NightTimeSpeedScale'],
            'auto_destroy_old_structures_multiplier': data['AutoDestroyOldStructuresMultiplier'],
            'resources_respawn_period_multiplier': data['ResourcesRespawnPeriodMultiplier'],
            'tribe_name_change_cooldown': data['TribeNameChangeCooldown'],
            'auto_save_period_minutes': data['AutoSavePeriodMinutes'],
            'ban_list_url': data['BanListURL'],
            'third_person': data['3rd-person'],
            'force_all_structure_locking': data['ForceAllStructureLocking'],
            'ban_list': data['ban-list'],
            'disable_pvp': data['disable-pvp'],
            'dino_count_multiplier': data['DinoCountMultiplier'],
            'message_of_the_day': data['message-of-the-day'],
            'item_stack_size_multiplier': data['ItemStackSizeMultiplier'],
            'b_force_can_ride_fliers': data['bForceCanRideFliers'],
            'dino_character_stamina_drain_multiplier': data['DinoCharacterStaminaDrainMultiplier'],
            'join_messages': data['join-messages'],
            'max_structures_in_range': data['max-structures-in-range'],
            'voice_chat': data['voice-chat'],
            'dino_resistance_multiplier': data['DinoResistanceMultiplier'],
            'enable_cryo_sickness_pve': data['EnableCryoSicknessPVE'],
            'server_password': data['server-password'],
            'harvest_health_multiplier': data['HarvestHealthMultiplier'],
            'admin_password': data['admin-password'],
            'no_hud': data['no-hud'],
            'nofishloot': data['nofishloot'],
            'disable_dino_taming': data['DisableDinoTaming'],
            'player_character_stamina_drain_multiplier': data['PlayerCharacterStaminaDrainMultiplier'],
            'players_exclusive_join_list': data['PlayersExclusiveJoinList'],
            'tribute_character_expiration_seconds': data['TributeCharacterExpirationSeconds'],
            'current_admin_password': data['current-admin-password'],
            'tribute_item_expiration_seconds': data['TributeItemExpirationSeconds'],
            'player_damage_multiplier': data['PlayerDamageMultiplier'],
            'structure_resistance_multiplier': data['StructureResistanceMultiplier'],
            'crosshair': data['crosshair'],
            'near_chat_only': data['near-chat-only'],
            'pv_e_structure_decay_period_multiplier': data['PvEStructureDecayPeriodMultiplier'],
            'allow_flyer_carry_pve': data['allow-flyer-carry-pve'],
            'structure_damage_multiplier': data['StructureDamageMultiplier'],
            'b_join_notifications': data['bJoinNotifications'],
            'admin_logging': data['AdminLogging'],
        }

    def __init__(
            self,
            service_id: int = None,
            server_name: str = None,
            admin_password: str = None,
            server_password: str = None,
            player_on_map: str = None,
            disable_pvp: str = None,
            hardcore: str = None,
            crosshair: str = None,
            no_hud: str = None,
            voice_chat: str = None,
            near_chat_only: str = None,
            third_person: str = None,
            leave_messages: str = None,
            join_messages: str = None,
            message_of_the_day: str = None,
            difficulty_offset: str = None,
            motd_duration: str = None,
            disable_structure_decay_pve: str = None,
            allow_flyer_carry_pve: str = None,
            max_structures_in_range: str = None,
            enable_pvp_gamma: str = None,
            no_tribute_downloads: str = None,
            day_cycle_speed_scale: str = None,
            night_time_speed_scale: str = None,
            day_time_speed_scale: str = None,
            dino_damage_multiplier: str = None,
            player_damage_multiplier: str = None,
            structure_damage_multiplier: str = None,
            player_resistance_multiplier: str = None,
            dino_resistance_multiplier: str = None,
            structure_resistance_multiplier: str = None,
            xp_multiplier: str = None,
            taming_speed_multiplier: str = None,
            harvest_amount_multiplier: str = None,
            harvest_health_multiplier: str = None,
            player_character_water_drain_multiplier: str = None,
            player_character_food_drain_multiplier: str = None,
            dino_character_food_drain_multiplier: str = None,
            player_character_stamina_drain_multiplier: str = None,
            dino_character_stamina_drain_multiplier: str = None,
            player_character_health_recovery_multiplier: str = None,
            dino_character_health_recovery_multiplier: str = None,
            dino_count_multiplier: str = None,
            pv_e_structure_decay_period_multiplier: str = None,
            resources_respawn_period_multiplier: str = None,
            clamp_resource_harvest_damage: str = None,
            map: str = None,
            restart_countdown_seconds: str = None,
            active_mods: str = None,
            start_with_backup: str = None,
            players_join_no_check_list: str = None,
            ban_list: str = None,
            prevent_download_survivors: str = None,
            prevent_download_items: str = None,
            prevent_download_dinos: str = None,
            admin_list: str = None,
            default_map: str = None,
            map_mod_id: str = None,
            active_total_conversion: str = None,
            disable_death_spectator: str = None,
            only_admin_rejoin_as_spectator: str = None,
            battle_num_of_tribes_to_start_game: str = None,
            time_to_collapse_rod: str = None,
            battle_auto_start_game_interval: str = None,
            battle_auto_restart_game_interval: str = None,
            battle_sudden_death_interval: str = None,
            structure_destruction_tag: str = None,
            force_respawn_dinos: str = None,
            ban_list_url: str = None,
            auto_save_period_minutes: str = None,
            activate_admin_logs: str = None,
            game_log_buffer: str = None,
            map_expert: str = None,
            disable_dino_decay_pve: str = None,
            pv_e_dino_decay_period_multiplier: str = None,
            disable_pve_gamma: str = None,
            exlusivejoin: str = None,
            players_exclusive_join_list: str = None,
            force_all_structure_locking: str = None,
            auto_destroy_old_structures_multiplier: str = None,
            b_join_notifications: str = None,
            b_show_status_notification_messages: str = None,
            per_platform_max_structures_multiplier: str = None,
            spectator_password: str = None,
            allow_cave_building_pve: str = None,
            nofishloot: str = None,
            disable_dino_riding: str = None,
            disable_dino_taming: str = None,
            max_personal_tamed_dinos: str = None,
            only_decay_unsnapped_core_structures: str = None,
            tribute_item_expiration_seconds: str = None,
            tribute_dino_expiration_seconds: str = None,
            tribute_character_expiration_seconds: str = None,
            current_admin_password: str = None,
            activate_admin_tribe_logs: str = None,
            tribe_name_change_cooldown: str = None,
            allow_hide_damage_source_from_logs: str = None,
            random_supply_crate_points: str = None,
            disable_weather_fog: str = None,
            admin_logging: str = None,
            b_force_can_ride_fliers: str = None,
            allow_tek_suit_powers_in_genesis: str = None,
            enable_cryo_sickness_pve: str = None,
            cryopod_nerf_duration: str = None,
            cryopod_nerf_damage_mult: str = None,
            item_stack_size_multiplier: str = None,
            allow_cave_building_pvp: str = None,
            **kwargs
    ):
        self.service_id = service_id
        self.server_name = server_name
        self.admin_password = admin_password
        self.server_password = server_password
        self.current_admin_password = current_admin_password
        self.player_on_map = player_on_map
        self.disable_pvp = disable_pvp
        self.hardcore = hardcore
        self.crosshair = crosshair
        self.no_hud = no_hud
        self.voice_chat = voice_chat
        self.near_chat_only = near_chat_only
        self.third_person = third_person
        self.leave_messages = leave_messages
        self.join_messages = join_messages
        self.message_of_the_day = message_of_the_day
        self.difficulty_offset = difficulty_offset
        self.motd_duration = motd_duration
        self.disable_structure_decay_pve = disable_structure_decay_pve
        self.allow_flyer_carry_pve = allow_flyer_carry_pve
        self.max_structures_in_range = max_structures_in_range
        self.enable_pvp_gamma = enable_pvp_gamma
        self.no_tribute_downloads = no_tribute_downloads
        self.day_cycle_speed_scale = day_cycle_speed_scale
        self.night_time_speed_scale = night_time_speed_scale
        self.day_time_speed_scale = day_time_speed_scale
        self.dino_damage_multiplier = dino_damage_multiplier
        self.player_damage_multiplier = player_damage_multiplier
        self.structure_damage_multiplier = structure_damage_multiplier
        self.player_resistance_multiplier = player_resistance_multiplier
        self.dino_resistance_multiplier = dino_resistance_multiplier
        self.structure_resistance_multiplier = structure_resistance_multiplier
        self.xp_multiplier = xp_multiplier
        self.taming_speed_multiplier = taming_speed_multiplier
        self.harvest_amount_multiplier = harvest_amount_multiplier
        self.harvest_health_multiplier = harvest_health_multiplier
        self.player_character_water_drain_multiplier = player_character_water_drain_multiplier
        self.player_character_food_drain_multiplier = player_character_food_drain_multiplier
        self.dino_character_food_drain_multiplier = dino_character_food_drain_multiplier
        self.player_character_stamina_drain_multiplier = player_character_stamina_drain_multiplier
        self.dino_character_stamina_drain_multiplier = dino_character_stamina_drain_multiplier
        self.player_character_health_recovery_multiplier = player_character_health_recovery_multiplier
        self.dino_character_health_recovery_multiplier = dino_character_health_recovery_multiplier
        self.dino_count_multiplier = dino_count_multiplier
        self.pv_e_structure_decay_period_multiplier = pv_e_structure_decay_period_multiplier
        self.resources_respawn_period_multiplier = resources_respawn_period_multiplier
        self.clamp_resource_harvest_damage = clamp_resource_harvest_damage
        self.map = map
        self.restart_countdown_seconds = restart_countdown_seconds
        self.active_mods = active_mods
        self.start_with_backup = start_with_backup
        self.players_join_no_check_list = players_join_no_check_list
        self.ban_list = ban_list
        self.prevent_download_survivors = prevent_download_survivors
        self.prevent_download_items = prevent_download_items
        self.prevent_download_dinos = prevent_download_dinos
        self.admin_list = admin_list
        self.default_map = default_map
        self.map_mod_id = map_mod_id
        self.active_total_conversion = active_total_conversion
        self.disable_death_spectator = disable_death_spectator
        self.only_admin_rejoin_as_spectator = only_admin_rejoin_as_spectator
        self.battle_num_of_tribes_to_start_game = battle_num_of_tribes_to_start_game
        self.time_to_collapse_rod = time_to_collapse_rod
        self.battle_auto_start_game_interval = battle_auto_start_game_interval
        self.battle_auto_restart_game_interval = battle_auto_restart_game_interval
        self.battle_sudden_death_interval = battle_sudden_death_interval
        self.structure_destruction_tag = structure_destruction_tag
        self.force_respawn_dinos = force_respawn_dinos
        self.ban_list_url = ban_list_url
        self.auto_save_period_minutes = auto_save_period_minutes
        self.activate_admin_logs = activate_admin_logs
        self.game_log_buffer = game_log_buffer
        self.tribute_character_expiration_seconds = tribute_character_expiration_seconds
        self.map_expert = map_expert
        self.disable_dino_decay_pve = disable_dino_decay_pve
        self.pv_e_dino_decay_period_multiplier = pv_e_dino_decay_period_multiplier
        self.disable_pve_gamma = disable_pve_gamma
        self.exlusivejoin = exlusivejoin
        self.players_exclusive_join_list = players_exclusive_join_list
        self.force_all_structure_locking = force_all_structure_locking
        self.auto_destroy_old_structures_multiplier = auto_destroy_old_structures_multiplier
        self.b_join_notifications = b_join_notifications
        self.b_show_status_notification_messages = b_show_status_notification_messages
        self.per_platform_max_structures_multiplier = per_platform_max_structures_multiplier
        self.spectator_password = spectator_password
        self.allow_cave_building_pve = allow_cave_building_pve
        self.nofishloot = nofishloot
        self.disable_dino_riding = disable_dino_riding
        self.disable_dino_taming = disable_dino_taming
        self.max_personal_tamed_dinos = max_personal_tamed_dinos
        self.only_decay_unsnapped_core_structures = only_decay_unsnapped_core_structures
        self.tribute_item_expiration_seconds = tribute_item_expiration_seconds
        self.tribute_dino_expiration_seconds = tribute_dino_expiration_seconds
        self.activate_admin_tribe_logs = activate_admin_tribe_logs
        self.tribe_name_change_cooldown = tribe_name_change_cooldown
        self.allow_hide_damage_source_from_logs = allow_hide_damage_source_from_logs
        self.random_supply_crate_points = random_supply_crate_points
        self.disable_weather_fog = disable_weather_fog
        self.admin_logging = admin_logging
        self.b_force_can_ride_fliers = b_force_can_ride_fliers
        self.allow_tek_suit_powers_in_genesis = allow_tek_suit_powers_in_genesis
        self.enable_cryo_sickness_pve = enable_cryo_sickness_pve
        self.cryopod_nerf_duration = cryopod_nerf_duration
        self.cryopod_nerf_damage_mult = cryopod_nerf_damage_mult
        self.item_stack_size_multiplier = item_stack_size_multiplier
        self.allow_cave_building_pvp = allow_cave_building_pvp
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"

