from gamedriver.nitrado.Client import Client
import json

class NitrAPI:
    NITRAPI_LIVE_URL = "https://api.nitrado.net/"

    @classmethod
    def __default_access(cls):
        from pathlib import Path
        import os
        key_file = Path(os.environ.get("KEY")) / Path("keys.json")
        if key_file.exists():
            with open(key_file, "r") as r:
                data = json.load(r)
                return data['api']['https://server.nitrado.net/']['accounts'][0]['key']

    def __init__(self, access_token=None, nitrapi_url=None):
        self.__access_token = access_token or NitrAPI.__default_access()
        self.__nitrapi_url = nitrapi_url or NitrAPI.NITRAPI_LIVE_URL
        self.__application_name = "nitrapi"
        self.__servers = []

    def health_check(self):
        return self.__get_public_data(path='ping')

    def maintenance_status(self):
        return self.__get_public_data(path='maintenance')

    def current_api_version(self):
        return self.__get_public_data(path='version')


def test():
    from gamedriver.nitrado.Nitrapi import NitrAPI
    api = NitrAPI()
    api.restart(9409179, restart_message="lets restart this server!")


if __name__ == '__main__':
    test()
