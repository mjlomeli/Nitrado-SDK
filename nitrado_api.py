from client import Client


class NitradoAPI:
    NITRADO_API_URL = "https://api.nitrado.net/"

    @classmethod
    def __default_access(cls):
        import os
        return os.environ.get("NITRADO_KEY")

    def __init__(self, key=None, url=None):
        key = key or NitradoAPI.__default_access()
        url = url or NitradoAPI.NITRADO_API_URL
        assert key and url, f"params in NitradoApi({key}, {url}) must be provided"
        self.__client = Client(url, key)
        self.__servers = []

    def health_check(self):
        return self.__client.get('ping')

    def maintenance_status(self):
        return self.__client.get('maintenance')

    def current_api_version(self):
        return self.__client.get('version')


if __name__ == '__main__':
    import json

    def print_json(data: dict):
        print(json.dumps(data, indent=3, sort_keys=True))

    api = NitradoAPI()
    print_json(api.health_check())
    print_json(api.maintenance_status())
    print_json(api.current_api_version())

    # api.restart(9409179, restart_message="lets restart this server!")

