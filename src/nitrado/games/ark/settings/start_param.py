
class StartParam:
    @classmethod
    def from_data(cls, service_id: int, **kwargs):
        return cls(service_id, **{k.lower().replace('-', '_'): v for k, v in kwargs.items()})

    def __init__(
            self,
            service_id: int,
            PvPStructureDecay: str = None,
            PreventOfflinePvP: str = None,
            PreventOfflinePvPInterval: str = None,
            ShowFloatingDamageText: str = None,
            DisableImprintDinoBuff: str = None,
            AllowAnyoneBabyImprintCuddle: str = None,
            OverideStructurePlatformPrevention: str = None,
            EnableExtraStructurePreventionVolumes: str = None,
            NonPermanentDiseases: str = None,
            PreventDiseases: str = None,
            OverrideStructurePlatformPrevention: str = None,
            PreventTribeAlliances: str = None,
            AllowRaidDinoFeeding: str = None,
            AllowHitMarkers: str = None,
            FastDecayUnsnappedCoreStructures: str = None,
            TribeLogDestroyedEnemyStructures: str = None,
            OverrideOfficialDifficulty: str = None,
            PreventDownloadSurvivors: str = None,
            PreventDownloadItems: str = None,
            PreventDownloadDinos: str = None,
            PreventUploadSurvivors: str = None,
            PreventUploadItems: str = None,
            PreventUploadDinos: str = None,
            ForceFlyerExplosives: str = None,
            DestroyUnconnectedWaterPipes: str = None,
            PvPDinoDecay: str = None,
            PvEAllowStructuresAtSupplyDrops: str = None,
            AllowCrateSpawnsOnTopOfStructures: str = None,
            UseOptimizedHarvestingHealth: str = None,
            ClampItemSpoilingTimes: str = None,
            AutoDestroyDecayedDinos: str = None,
            AllowFlyingStaminaRecovery: str = None,
            AllowMultipleAttachedC4: str = None,
            bAllowPlatformSaddleMultiFloors: str = None,
            PreventSpawnAnimations: str = None,
            AutoDestroyStructures: str = None,
            MinimumDinoReuploadInterval: str = None,
            OnlyAutoDestroyCoreStructures: str = None,
            OxygenSwimSpeedStatMultiplier: str = None,
            ServerAutoForceRespawnWildDinosInterval: str = None,
            CrossARKAllowForeignDinoDownloads: str = None,
            ClampItemStats: str = None,
            EnableCryopodNerf: str = None,
            NewYear1UTC: str = None,
            NewYear2UTC: str = None,
            **kwargs
    ):
        self.PvPStructureDecay = PvPStructureDecay
        self.PreventOfflinePvP = PreventOfflinePvP
        self.PreventOfflinePvPInterval = PreventOfflinePvPInterval
        self.ShowFloatingDamageText = ShowFloatingDamageText
        self.DisableImprintDinoBuff = DisableImprintDinoBuff
        self.AllowAnyoneBabyImprintCuddle = AllowAnyoneBabyImprintCuddle
        self.OverideStructurePlatformPrevention = OverideStructurePlatformPrevention
        self.EnableExtraStructurePreventionVolumes = EnableExtraStructurePreventionVolumes
        self.NonPermanentDiseases = NonPermanentDiseases
        self.PreventDiseases = PreventDiseases
        self.OverrideStructurePlatformPrevention = OverrideStructurePlatformPrevention
        self.PreventTribeAlliances = PreventTribeAlliances
        self.AllowRaidDinoFeeding = AllowRaidDinoFeeding
        self.AllowHitMarkers = AllowHitMarkers
        self.FastDecayUnsnappedCoreStructures = FastDecayUnsnappedCoreStructures
        self.TribeLogDestroyedEnemyStructures = TribeLogDestroyedEnemyStructures
        self.OverrideOfficialDifficulty = OverrideOfficialDifficulty
        self.PreventDownloadSurvivors = PreventDownloadSurvivors
        self.PreventDownloadItems = PreventDownloadItems
        self.PreventDownloadDinos = PreventDownloadDinos
        self.PreventUploadSurvivors = PreventUploadSurvivors
        self.PreventUploadItems = PreventUploadItems
        self.PreventUploadDinos = PreventUploadDinos
        self.ForceFlyerExplosives = ForceFlyerExplosives
        self.DestroyUnconnectedWaterPipes = DestroyUnconnectedWaterPipes
        self.PvPDinoDecay = PvPDinoDecay
        self.PvEAllowStructuresAtSupplyDrops = PvEAllowStructuresAtSupplyDrops
        self.AllowCrateSpawnsOnTopOfStructures = AllowCrateSpawnsOnTopOfStructures
        self.UseOptimizedHarvestingHealth = UseOptimizedHarvestingHealth
        self.ClampItemSpoilingTimes = ClampItemSpoilingTimes
        self.AutoDestroyDecayedDinos = AutoDestroyDecayedDinos
        self.AllowFlyingStaminaRecovery = AllowFlyingStaminaRecovery
        self.AllowMultipleAttachedC4 = AllowMultipleAttachedC4
        self.bAllowPlatformSaddleMultiFloors = bAllowPlatformSaddleMultiFloors
        self.PreventSpawnAnimations = PreventSpawnAnimations
        self.AutoDestroyStructures = AutoDestroyStructures
        self.MinimumDinoReuploadInterval = MinimumDinoReuploadInterval
        self.OnlyAutoDestroyCoreStructures = OnlyAutoDestroyCoreStructures
        self.OxygenSwimSpeedStatMultiplier = OxygenSwimSpeedStatMultiplier
        self.ServerAutoForceRespawnWildDinosInterval = ServerAutoForceRespawnWildDinosInterval
        self.CrossARKAllowForeignDinoDownloads = CrossARKAllowForeignDinoDownloads
        self.ClampItemStats = ClampItemStats
        self.EnableCryopodNerf = EnableCryopodNerf
        self.NewYear1UTC = NewYear1UTC
        self.NewYear2UTC = NewYear2UTC
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        params = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"

