from __future__ import annotations
from .locations import Location


class Game:
    @classmethod
    def from_data(cls, **kwargs) -> list[Game]:
        #steam_id = kwargs['steam_id']
        locations = {loc['id']: loc for loc in kwargs['locations']}
        games = []
        for game in kwargs['games']:
            game['locations'] = [Location(**locations[id]) for id in game['locations']]
            games.append(cls(**game))
        return games

    def __init__(
            self,
            id: int = None,
            steam_id: int = None,
            has_steam_game: str = None,
            name: str = None,
            minecraft_mode: bool = False,
            publicserver_only: bool = False,
            portlist_short: str = None,
            folder_short: str = None,
            minimum_slots: int = 0,
            slot_multiplier: str = None,
            maximum_recommended_slots: str = None,
            modpacks: list = None,
            icons: dict = None,
            tags: list = None,
            preorder_locations: list = None,
            orderlocked_locations: str = None,
            locations: list[int] = None,
            **kwargs
    ):
        self.id = id
        self.steam_id = steam_id
        self.has_steam_game = has_steam_game
        self.name = name
        self.minecraft_mode = minecraft_mode
        self.publicserver_only = publicserver_only
        self.portlist_short = portlist_short
        self.folder_short = folder_short
        self.minimum_slots = minimum_slots
        self.slot_multiplier = slot_multiplier
        self.maximum_recommended_slots = maximum_recommended_slots
        self.modpacks = modpacks or []
        self.icons = icons
        self.tags = tags or []
        self.preorder_locations = preorder_locations or []
        self.orderlocked_locations = orderlocked_locations
        self.locations = locations or []
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        name = f"name={repr(self.name)}"
        shorten_locations = [str(l) for l in self.locations[:3]]
        trunc_locations = ','.join(shorten_locations + (['...'] if len(self.locations) > 3 else []))
        locations = f"locations=[{trunc_locations}]"
        params = [s for s in [name, locations]]
        return f"<{self.__class__.__name__}({', '.join(params)})>"
