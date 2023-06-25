
class GameIni:

    @classmethod
    def keys_to_snake_case(cls, data: dict) -> dict:
        return {
            'dino_spawn_weight_multipliers': data['DinoSpawnWeightMultipliers'],
            'override_engram_entries': data['OverrideEngramEntries'],
            'level_experience_ramp_overrides': data['LevelExperienceRampOverrides'],
            'override_player_level_engram_points': data['OverridePlayerLevelEngramPoints'],
            'tamed_dino_class_damage_multipliers': data['TamedDinoClassDamageMultipliers'],
            'tamed_dino_class_resistance_multipliers': data['TamedDinoClassResistanceMultipliers'],
            'exclude_item_indices': data['ExcludeItemIndices'],
            'harvest_resource_item_amount_class_multipliers': data['HarvestResourceItemAmountClassMultipliers'],
            'override_named_engram_entries': data['OverrideNamedEngramEntries'],
            'b_only_allow_specified_engrams': data['bOnlyAllowSpecifiedEngrams'],
            'global_spoiling_time_multiplier': data['GlobalSpoilingTimeMultiplier'],
            'global_item_decomposition_time_multiplier': data['GlobalItemDecompositionTimeMultiplier'],
            'global_corpse_decomposition_time_multiplier': data['GlobalCorpseDecompositionTimeMultiplier'],
            'override_max_experience_points_player': data['OverrideMaxExperiencePointsPlayer'],
            'override_max_experience_points_dino': data['OverrideMaxExperiencePointsDino'],
            'pv_p_zone_structure_damage_multiplier': data['PvPZoneStructureDamageMultiplier'],
            'b_pv_e_disable_friendly_fire': data['bPvEDisableFriendlyFire'],
            'resource_no_replenish_radius_players': data['ResourceNoReplenishRadiusPlayers'],
            'resource_no_replenish_radius_structures': data['ResourceNoReplenishRadiusStructures'],
            'b_auto_pv_e_timer': data['bAutoPvETimer'],
            'b_auto_pv_e_use_system_time': data['bAutoPvEUseSystemTime'],
            'auto_pv_e_start_time_seconds': data['AutoPvEStartTimeSeconds'],
            'auto_pv_e_stop_time_seconds': data['AutoPvEStopTimeSeconds'],
            'lay_egg_interval_multiplier': data['LayEggIntervalMultiplier'],
            'dino_turret_damage_multiplier': data['DinoTurretDamageMultiplier'],
            'b_disable_loot_crates': data['bDisableLootCrates'],
            'dino_harvesting_damage_multiplier': data['DinoHarvestingDamageMultiplier'],
            'b_disable_friendly_fire': data['bDisableFriendlyFire'],
            'custom_recipe_effectiveness_multiplier': data['CustomRecipeEffectivenessMultiplier'],
            'custom_recipe_skill_multiplier': data['CustomRecipeSkillMultiplier'],
            'mating_interval_multiplier': data['MatingIntervalMultiplier'],
            'egg_hatch_speed_multiplier': data['EggHatchSpeedMultiplier'],
            'baby_mature_speed_multiplier': data['BabyMatureSpeedMultiplier'],
            'b_passive_defenses_damage_riderless_dinos': data['bPassiveDefensesDamageRiderlessDinos'],
            'kill_x_p_multiplier': data['KillXPMultiplier'],
            'harvest_x_p_multiplier': data['HarvestXPMultiplier'],
            'craft_x_p_multiplier': data['CraftXPMultiplier'],
            'generic_x_p_multiplier': data['GenericXPMultiplier'],
            'special_x_p_multiplier': data['SpecialXPMultiplier'],
            'p_g_map_name': data['PGMapName'],
            'p_g_terrain_properties_string': data['PGTerrainPropertiesString'],
            'config_override_supply_crate_items': data['ConfigOverrideSupplyCrateItems'],
            'b_disable_dino_riding': data['bDisableDinoRiding'],
            'b_disable_dino_taming': data['bDisableDinoTaming'],
            'b_use_corpse_locator': data['bUseCorpseLocator'],
            'b_disable_structure_placement_collision': data['bDisableStructurePlacementCollision'],
            'fast_decay_interval': data['FastDecayInterval'],
            'b_use_singleplayer_settings': data['bUseSingleplayerSettings'],
            'b_allow_unlimited_respecs': data['bAllowUnlimitedRespecs'],
            'supply_crate_loot_quality_multiplier': data['SupplyCrateLootQualityMultiplier'],
            'fishing_loot_quality_multiplier': data['FishingLootQualityMultiplier'],
            'per_level_stats_multiplier': data['PerLevelStatsMultiplier'],
            'baby_cuddle_interval_multiplier': data['BabyCuddleIntervalMultiplier'],
            'baby_cuddle_grace_period_multiplier': data['BabyCuddleGracePeriodMultiplier'],
            'baby_cuddle_lose_imprint_quality_speed_multiplier': data['BabyCuddleLoseImprintQualitySpeedMultiplier'],
            'baby_imprinting_stat_scale_multiplier': data['BabyImprintingStatScaleMultiplier'],
            'player_harvesting_damage_multiplier': data['PlayerHarvestingDamageMultiplier'],
            'crop_growth_speed_multiplier': data['CropGrowthSpeedMultiplier'],
            'baby_food_consumption_speed_multiplier': data['BabyFoodConsumptionSpeedMultiplier'],
            'dino_class_damage_multipliers': data['DinoClassDamageMultipliers'],
            'b_pv_e_allow_tribe_war': data['bPvEAllowTribeWar'],
            'b_pv_e_allow_tribe_war_cancel': data['bPvEAllowTribeWarCancel'],
            'crop_decay_speed_multiplier': data['CropDecaySpeedMultiplier'],
            'hair_growth_speed_multiplier': data['HairGrowthSpeedMultiplier'],
            'fuel_consumption_interval_multiplier': data['FuelConsumptionIntervalMultiplier'],
            'kick_idle_players_period': data['KickIdlePlayersPeriod'],
            'max_number_of_players_in_tribe': data['MaxNumberOfPlayersInTribe'],
            'use_corpse_life_span_multiplier': data['UseCorpseLifeSpanMultiplier'],
            'global_powered_battery_durability_decrease_per_second': data['GlobalPoweredBatteryDurabilityDecreasePerSecond'],
            'b_limit_turrets_in_range': data['bLimitTurretsInRange'],
            'limit_turrets_range': data['LimitTurretsRange'],
            'limit_turrets_num': data['LimitTurretsNum'],
            'b_hard_limit_turrets_in_range': data['bHardLimitTurretsInRange'],
            'b_show_creative_mode': data['bShowCreativeMode'],
            'prevent_offline_pv_p_connection_invincible_interval': data['PreventOfflinePvPConnectionInvincibleInterval'],
            'tamed_dino_character_food_drain_multiplier': data['TamedDinoCharacterFoodDrainMultiplier'],
            'wild_dino_character_food_drain_multiplier': data['WildDinoCharacterFoodDrainMultiplier'],
            'wild_dino_torpor_drain_multiplier': data['WildDinoTorporDrainMultiplier'],
            'passive_tame_interval_multiplier': data['PassiveTameIntervalMultiplier'],
            'tamed_dino_torpor_drain_multiplier': data['TamedDinoTorporDrainMultiplier'],
            'b_ignore_structures_prevention_volumes': data['bIgnoreStructuresPreventionVolumes'],
            'b_genesis_use_structures_prevention_volumes': data['bGenesisUseStructuresPreventionVolumes'],
            'b_disable_genesis_missions': data['bDisableGenesisMissions'],
            'baby_imprint_amount_multiplier': data['BabyImprintAmountMultiplier'],
            'hexagon_reward_multiplier': data['HexagonRewardMultiplier'],
            'b_allow_flyer_speed_leveling': data['bAllowFlyerSpeedLeveling'],
            'prevent_transfer_for_class_names': data['PreventTransferForClassNames'],
        }

    def __init__(
            self,
            service_id: int = None,
            dino_spawn_weight_multipliers: str = None,
            override_engram_entries: str = None,
            level_experience_ramp_overrides: str = None,
            override_player_level_engram_points: str = None,
            tamed_dino_class_damage_multipliers: str = None,
            tamed_dino_class_resistance_multipliers: str = None,
            exclude_item_indices: str = None,
            harvest_resource_item_amount_class_multipliers: str = None,
            override_named_engram_entries: str = None,
            b_only_allow_specified_engrams: str = None,
            global_spoiling_time_multiplier: str = None,
            global_item_decomposition_time_multiplier: str = None,
            global_corpse_decomposition_time_multiplier: str = None,
            override_max_experience_points_player: str = None,
            override_max_experience_points_dino: str = None,
            pvp_zone_structure_damage_multiplier: str = None,
            b_pve_disable_friendly_fire: str = None,
            resource_no_replenish_radius_players: str = None,
            resource_no_replenish_radius_structures: str = None,
            b_auto_pve_timer: str = None,
            b_auto_pve_use_system_time: str = None,
            auto_pve_start_time_seconds: str = None,
            auto_pve_stop_time_seconds: str = None,
            lay_egg_interval_multiplier: str = None,
            dino_turret_damage_multiplier: str = None,
            b_disable_loot_crates: str = None,
            dino_harvesting_damage_multiplier: str = None,
            b_disable_friendly_fire: str = None,
            custom_recipe_effectiveness_multiplier: str = None,
            custom_recipe_skill_multiplier: str = None,
            mating_interval_multiplier: str = None,
            egg_hatch_speed_multiplier: str = None,
            baby_mature_speed_multiplier: str = None,
            b_passive_defenses_damage_riderless_dinos: str = None,
            kill_xp_multiplier: str = None,
            harvest_xp_multiplier: str = None,
            craft_xp_multiplier: str = None,
            generic_xp_multiplier: str = None,
            special_xp_multiplier: str = None,
            pg_map_name: str = None,
            pg_terrain_properties_string: str = None,
            config_override_supply_crate_items: str = None,
            b_disable_dino_riding: str = None,
            b_disable_dino_taming: str = None,
            b_use_corpse_locator: str = None,
            b_disable_structure_placement_collision: str = None,
            fast_decay_interval: str = None,
            b_use_singleplayer_settings: str = None,
            b_allow_unlimited_respecs: str = None,
            supply_crate_loot_quality_multiplier: str = None,
            fishing_loot_quality_multiplier: str = None,
            per_level_stats_multiplier: str = None,
            baby_cuddle_interval_multiplier: str = None,
            baby_cuddle_grace_period_multiplier: str = None,
            baby_cuddle_lose_imprint_quality_speed_multiplier: str = None,
            baby_imprinting_stat_scale_multiplier: str = None,
            player_harvesting_damage_multiplier: str = None,
            crop_growth_speed_multiplier: str = None,
            baby_food_consumption_speed_multiplier: str = None,
            dino_class_damage_multipliers: str = None,
            b_pve_allow_tribe_war: str = None,
            b_pve_allow_tribe_war_cancel: str = None,
            crop_decay_speed_multiplier: str = None,
            hair_growth_speed_multiplier: str = None,
            fuel_consumption_interval_multiplier: str = None,
            kick_idle_players_period: str = None,
            max_number_of_players_in_tribe: str = None,
            use_corpse_life_span_multiplier: str = None,
            global_powered_battery_durability_decrease_per_second: str = None,
            b_limit_turrets_in_range: str = None,
            limit_turrets_range: str = None,
            limit_turrets_num: str = None,
            b_hard_limit_turrets_in_range: str = None,
            b_show_creative_mode: str = None,
            prevent_offline_pvp_connection_invincible_interval: str = None,
            tamed_dino_character_food_drain_multiplier: str = None,
            wild_dino_character_food_drain_multiplier: str = None,
            wild_dino_torpor_drain_multiplier: str = None,
            passive_tame_interval_multiplier: str = None,
            tamed_dino_torpor_drain_multiplier: str = None,
            b_ignore_structures_prevention_volumes: str = None,
            b_genesis_use_structures_prevention_volumes: str = None,
            b_disable_genesis_missions: str = None,
            baby_imprint_amount_multiplier: str = None,
            hexagon_reward_multiplier: str = None,
            b_allow_flyer_speed_leveling: str = None,
            prevent_transfer_for_class_names: str = None,
            **kwargs
    ):
        self.service_id = service_id
        self.dino_spawn_weight_multipliers = dino_spawn_weight_multipliers
        self.override_engram_entries = override_engram_entries
        self.level_experience_ramp_overrides = level_experience_ramp_overrides
        self.override_player_level_engram_points = override_player_level_engram_points
        self.tamed_dino_class_damage_multipliers = tamed_dino_class_damage_multipliers
        self.tamed_dino_class_resistance_multipliers = tamed_dino_class_resistance_multipliers
        self.exclude_item_indices = exclude_item_indices
        self.harvest_resource_item_amount_class_multipliers = harvest_resource_item_amount_class_multipliers
        self.override_named_engram_entries = override_named_engram_entries
        self.b_only_allow_specified_engrams = b_only_allow_specified_engrams
        self.global_spoiling_time_multiplier = global_spoiling_time_multiplier
        self.global_item_decomposition_time_multiplier = global_item_decomposition_time_multiplier
        self.global_corpse_decomposition_time_multiplier = global_corpse_decomposition_time_multiplier
        self.override_max_experience_points_player = override_max_experience_points_player
        self.override_max_experience_points_dino = override_max_experience_points_dino
        self.pv_p_zone_structure_damage_multiplier = pvp_zone_structure_damage_multiplier
        self.b_pv_e_disable_friendly_fire = b_pve_disable_friendly_fire
        self.resource_no_replenish_radius_players = resource_no_replenish_radius_players
        self.resource_no_replenish_radius_structures = resource_no_replenish_radius_structures
        self.b_auto_pv_e_timer = b_auto_pve_timer
        self.b_auto_pv_e_use_system_time = b_auto_pve_use_system_time
        self.auto_pv_e_start_time_seconds = auto_pve_start_time_seconds
        self.auto_pv_e_stop_time_seconds = auto_pve_stop_time_seconds
        self.lay_egg_interval_multiplier = lay_egg_interval_multiplier
        self.dino_turret_damage_multiplier = dino_turret_damage_multiplier
        self.b_disable_loot_crates = b_disable_loot_crates
        self.dino_harvesting_damage_multiplier = dino_harvesting_damage_multiplier
        self.b_disable_friendly_fire = b_disable_friendly_fire
        self.custom_recipe_effectiveness_multiplier = custom_recipe_effectiveness_multiplier
        self.custom_recipe_skill_multiplier = custom_recipe_skill_multiplier
        self.mating_interval_multiplier = mating_interval_multiplier
        self.egg_hatch_speed_multiplier = egg_hatch_speed_multiplier
        self.baby_mature_speed_multiplier = baby_mature_speed_multiplier
        self.b_passive_defenses_damage_riderless_dinos = b_passive_defenses_damage_riderless_dinos
        self.kill_x_p_multiplier = kill_xp_multiplier
        self.harvest_x_p_multiplier = harvest_xp_multiplier
        self.craft_x_p_multiplier = craft_xp_multiplier
        self.generic_x_p_multiplier = generic_xp_multiplier
        self.special_x_p_multiplier = special_xp_multiplier
        self.p_g_map_name = pg_map_name
        self.p_g_terrain_properties_string = pg_terrain_properties_string
        self.config_override_supply_crate_items = config_override_supply_crate_items
        self.b_disable_dino_riding = b_disable_dino_riding
        self.b_disable_dino_taming = b_disable_dino_taming
        self.b_use_corpse_locator = b_use_corpse_locator
        self.b_disable_structure_placement_collision = b_disable_structure_placement_collision
        self.fast_decay_interval = fast_decay_interval
        self.b_use_singleplayer_settings = b_use_singleplayer_settings
        self.b_allow_unlimited_respecs = b_allow_unlimited_respecs
        self.supply_crate_loot_quality_multiplier = supply_crate_loot_quality_multiplier
        self.fishing_loot_quality_multiplier = fishing_loot_quality_multiplier
        self.per_level_stats_multiplier = per_level_stats_multiplier
        self.baby_cuddle_interval_multiplier = baby_cuddle_interval_multiplier
        self.baby_cuddle_grace_period_multiplier = baby_cuddle_grace_period_multiplier
        self.baby_cuddle_lose_imprint_quality_speed_multiplier = baby_cuddle_lose_imprint_quality_speed_multiplier
        self.baby_imprinting_stat_scale_multiplier = baby_imprinting_stat_scale_multiplier
        self.player_harvesting_damage_multiplier = player_harvesting_damage_multiplier
        self.crop_growth_speed_multiplier = crop_growth_speed_multiplier
        self.baby_food_consumption_speed_multiplier = baby_food_consumption_speed_multiplier
        self.dino_class_damage_multipliers = dino_class_damage_multipliers
        self.b_pv_e_allow_tribe_war = b_pve_allow_tribe_war
        self.b_pv_e_allow_tribe_war_cancel = b_pve_allow_tribe_war_cancel
        self.crop_decay_speed_multiplier = crop_decay_speed_multiplier
        self.hair_growth_speed_multiplier = hair_growth_speed_multiplier
        self.fuel_consumption_interval_multiplier = fuel_consumption_interval_multiplier
        self.kick_idle_players_period = kick_idle_players_period
        self.max_number_of_players_in_tribe = max_number_of_players_in_tribe
        self.use_corpse_life_span_multiplier = use_corpse_life_span_multiplier
        self.global_powered_battery_durability_decrease_per_second = global_powered_battery_durability_decrease_per_second
        self.b_limit_turrets_in_range = b_limit_turrets_in_range
        self.limit_turrets_range = limit_turrets_range
        self.limit_turrets_num = limit_turrets_num
        self.b_hard_limit_turrets_in_range = b_hard_limit_turrets_in_range
        self.b_show_creative_mode = b_show_creative_mode
        self.prevent_offline_pvp_connection_invincible_interval = prevent_offline_pvp_connection_invincible_interval
        self.tamed_dino_character_food_drain_multiplier = tamed_dino_character_food_drain_multiplier
        self.wild_dino_character_food_drain_multiplier = wild_dino_character_food_drain_multiplier
        self.wild_dino_torpor_drain_multiplier = wild_dino_torpor_drain_multiplier
        self.passive_tame_interval_multiplier = passive_tame_interval_multiplier
        self.tamed_dino_torpor_drain_multiplier = tamed_dino_torpor_drain_multiplier
        self.b_ignore_structures_prevention_volumes = b_ignore_structures_prevention_volumes
        self.b_genesis_use_structures_prevention_volumes = b_genesis_use_structures_prevention_volumes
        self.b_disable_genesis_missions = b_disable_genesis_missions
        self.baby_imprint_amount_multiplier = baby_imprint_amount_multiplier
        self.hexagon_reward_multiplier = hexagon_reward_multiplier
        self.b_allow_flyer_speed_leveling = b_allow_flyer_speed_leveling
        self.prevent_transfer_for_class_names = prevent_transfer_for_class_names
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"

