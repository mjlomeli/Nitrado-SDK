
class StartParam:
    @classmethod
    def keys_to_snakecase(cls, data: dict) -> dict:
        return {
            'pvp_structure_decay': data['PvPStructureDecay'],
            'prevent_offline_pvp': data['PreventOfflinePvP'],
            'prevent_offline_pvp_interval': data['PreventOfflinePvPInterval'],
            'show_floating_damage_text': data['ShowFloatingDamageText'],
            'disable_imprint_dino_buff': data['DisableImprintDinoBuff'],
            'allow_anyone_baby_imprint_cuddle': data['AllowAnyoneBabyImprintCuddle'],
            'overide_structure_platform_prevention': data['OverideStructurePlatformPrevention'],
            'enable_extra_structure_prevention_volumes': data['EnableExtraStructurePreventionVolumes'],
            'non_permanent_diseases': data['NonPermanentDiseases'],
            'prevent_diseases': data['PreventDiseases'],
            'override_structure_platform_prevention': data['OverrideStructurePlatformPrevention'],
            'prevent_tribe_alliances': data['PreventTribeAlliances'],
            'allow_raid_dino_feeding': data['AllowRaidDinoFeeding'],
            'allow_hit_markers': data['AllowHitMarkers'],
            'fast_decay_unsnapped_core_structures': data['FastDecayUnsnappedCoreStructures'],
            'tribe_log_destroyed_enemy_structures': data['TribeLogDestroyedEnemyStructures'],
            'override_official_difficulty': data['OverrideOfficialDifficulty'],
            'prevent_download_survivors': data['PreventDownloadSurvivors'],
            'prevent_download_items': data['PreventDownloadItems'],
            'prevent_download_dinos': data['PreventDownloadDinos'],
            'prevent_upload_survivors': data['PreventUploadSurvivors'],
            'prevent_upload_items': data['PreventUploadItems'],
            'prevent_upload_dinos': data['PreventUploadDinos'],
            'force_flyer_explosives': data['ForceFlyerExplosives'],
            'destroy_unconnected_water_pipes': data['DestroyUnconnectedWaterPipes'],
            'pvp_dino_decay': data['PvPDinoDecay'],
            'pve_allow_structures_at_supply_drops': data['PvEAllowStructuresAtSupplyDrops'],
            'allow_crate_spawns_on_top_of_structures': data['AllowCrateSpawnsOnTopOfStructures'],
            'use_optimized_harvesting_health': data['UseOptimizedHarvestingHealth'],
            'clamp_item_spoiling_times': data['ClampItemSpoilingTimes'],
            'auto_destroy_decayed_dinos': data['AutoDestroyDecayedDinos'],
            'allow_flying_stamina_recovery': data['AllowFlyingStaminaRecovery'],
            'allow_multiple_attached_c4': data['AllowMultipleAttachedC4'],
            'b_allow_platform_saddle_multi_floors': data['bAllowPlatformSaddleMultiFloors'],
            'prevent_spawn_animations': data['PreventSpawnAnimations'],
            'auto_destroy_structures': data['AutoDestroyStructures'],
            'minimum_dino_reupload_interval': data['MinimumDinoReuploadInterval'],
            'only_auto_destroy_core_structures': data['OnlyAutoDestroyCoreStructures'],
            'oxygen_swim_speed_stat_multiplier': data['OxygenSwimSpeedStatMultiplier'],
            'server_auto_force_respawn_wild_dinos_interval': data['ServerAutoForceRespawnWildDinosInterval'],
            'cross_a_r_k_allow_foreign_dino_downloads': data['CrossARKAllowForeignDinoDownloads'],
            'clamp_item_stats': data['ClampItemStats'],
            'enable_cryopod_nerf': data['EnableCryopodNerf'],
            'new_year1_utc': data['NewYear1UTC'],
            'new_year2_utc': data['NewYear2UTC'],
        }

    def __init__(
            self,
            service_id: int = None,
            pvp_structure_decay: str = None,
            prevent_offline_pvp: str = None,
            prevent_offline_pvp_interval: str = None,
            show_floating_damage_text: str = None,
            disable_imprint_dino_buff: str = None,
            allow_anyone_baby_imprint_cuddle: str = None,
            overide_structure_platform_prevention: str = None,
            enable_extra_structure_prevention_volumes: str = None,
            non_permanent_diseases: str = None,
            prevent_diseases: str = None,
            override_structure_platform_prevention: str = None,
            prevent_tribe_alliances: str = None,
            allow_raid_dino_feeding: str = None,
            allow_hit_markers: str = None,
            fast_decay_unsnapped_core_structures: str = None,
            tribe_log_destroyed_enemy_structures: str = None,
            override_official_difficulty: str = None,
            prevent_download_survivors: str = None,
            prevent_download_items: str = None,
            prevent_download_dinos: str = None,
            prevent_upload_survivors: str = None,
            prevent_upload_items: str = None,
            prevent_upload_dinos: str = None,
            force_flyer_explosives: str = None,
            destroy_unconnected_water_pipes: str = None,
            pvp_dino_decay: str = None,
            pve_allow_structures_at_supply_drops: str = None,
            allow_crate_spawns_on_top_of_structures: str = None,
            use_optimized_harvesting_health: str = None,
            clamp_item_spoiling_times: str = None,
            auto_destroy_decayed_dinos: str = None,
            allow_flying_stamina_recovery: str = None,
            allow_multiple_attached_c4: str = None,
            b_allow_platform_saddle_multi_floors: str = None,
            prevent_spawn_animations: str = None,
            auto_destroy_structures: str = None,
            minimum_dino_reupload_interval: str = None,
            only_auto_destroy_core_structures: str = None,
            oxygen_swim_speed_stat_multiplier: str = None,
            server_auto_force_respawn_wild_dinos_interval: str = None,
            cross_ark_allow_foreign_dino_downloads: str = None,
            clamp_item_stats: str = None,
            enable_cryopod_nerf: str = None,
            new_year1_utc: str = None,
            new_year2_utc: str = None,
            **kwargs
    ):
        self.service_id = service_id
        self.pvp_structure_decay = pvp_structure_decay
        self.prevent_offline_pvp = prevent_offline_pvp
        self.prevent_offline_pvp_interval = prevent_offline_pvp_interval
        self.show_floating_damage_text = show_floating_damage_text
        self.disable_imprint_dino_buff = disable_imprint_dino_buff
        self.allow_anyone_baby_imprint_cuddle = allow_anyone_baby_imprint_cuddle
        self.overide_structure_platform_prevention = overide_structure_platform_prevention
        self.enable_extra_structure_prevention_volumes = enable_extra_structure_prevention_volumes
        self.non_permanent_diseases = non_permanent_diseases
        self.prevent_diseases = prevent_diseases
        self.override_structure_platform_prevention = override_structure_platform_prevention
        self.prevent_tribe_alliances = prevent_tribe_alliances
        self.allow_raid_dino_feeding = allow_raid_dino_feeding
        self.allow_hit_markers = allow_hit_markers
        self.fast_decay_unsnapped_core_structures = fast_decay_unsnapped_core_structures
        self.tribe_log_destroyed_enemy_structures = tribe_log_destroyed_enemy_structures
        self.override_official_difficulty = override_official_difficulty
        self.prevent_download_survivors = prevent_download_survivors
        self.prevent_download_items = prevent_download_items
        self.prevent_download_dinos = prevent_download_dinos
        self.prevent_upload_survivors = prevent_upload_survivors
        self.prevent_upload_items = prevent_upload_items
        self.prevent_upload_dinos = prevent_upload_dinos
        self.force_flyer_explosives = force_flyer_explosives
        self.destroy_unconnected_water_pipes = destroy_unconnected_water_pipes
        self.pvp_dino_decay = pvp_dino_decay
        self.pve_allow_structures_at_supply_drops = pve_allow_structures_at_supply_drops
        self.allow_crate_spawns_on_top_of_structures = allow_crate_spawns_on_top_of_structures
        self.use_optimized_harvesting_health = use_optimized_harvesting_health
        self.clamp_item_spoiling_times = clamp_item_spoiling_times
        self.auto_destroy_decayed_dinos = auto_destroy_decayed_dinos
        self.allow_flying_stamina_recovery = allow_flying_stamina_recovery
        self.allow_multiple_attached_c4 = allow_multiple_attached_c4
        self.b_allow_platform_saddle_multi_floors = b_allow_platform_saddle_multi_floors
        self.prevent_spawn_animations = prevent_spawn_animations
        self.auto_destroy_structures = auto_destroy_structures
        self.minimum_dino_reupload_interval = minimum_dino_reupload_interval
        self.only_auto_destroy_core_structures = only_auto_destroy_core_structures
        self.oxygen_swim_speed_stat_multiplier = oxygen_swim_speed_stat_multiplier
        self.server_auto_force_respawn_wild_dinos_interval = server_auto_force_respawn_wild_dinos_interval
        self.cross_ark_allow_foreign_dino_downloads = cross_ark_allow_foreign_dino_downloads
        self.clamp_item_stats = clamp_item_stats
        self.enable_cryopod_nerf = enable_cryopod_nerf
        self.new_year1_utc = new_year1_utc
        self.new_year2_utc = new_year2_utc
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"

