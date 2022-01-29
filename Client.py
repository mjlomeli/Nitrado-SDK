import requests
import json


def _get_key():
    from pathlib import Path
    import os
    key_file = Path(os.environ.get("KEY")) / Path("keys.json")
    if key_file.exists():
        with open(key_file, "r") as r:
            data = json.load(r)
            return data['api']['https://server.nitrado.net/']['accounts'][0]['key']


def pretty_json(data: dict):
    return json.dumps(data, indent=3, sort_keys=True)


class Client:
    def __init__(self, api_url, access_token):
        assert type(api_url) == str
        assert len(api_url) > 1, "Api URL's should include 'http://' or 'https://'"
        self.__headers = {'Authorization': access_token} if access_token else None
        self.__api_url = api_url if api_url[-1] == '/' else f"{api_url}/"

    def __make_path(self, path=None):
        if isinstance(path, str):
            return "{}{}".format(self.__api_url, path)
        elif isinstance(path, list):
            path_list = [str(dir) for dir in path]
            return "{}{}".format(self.__api_url, '/'.join(path_list))
        else:
            return self.__api_url

    @staticmethod
    def __ark_request_filter(response):
        text = response.text
        if response.status_code != 200:
            raise Exception("[APIErrorStatus: {}] Returned: {}".format(response.status_code,
                                                                       'None' if text == '' else '\n{}'.format(text)))
        data = json.loads(response.text)
        if 'status' in data:
            if 'blueprints' in data:
                return data['blueprints']
            elif data['status'] == 'success':
                return data
            else:
                return False
        else:
            raise Exception("[APIError] Returned: \n{}".format(pretty_json(data)))

    def get(self, path=None, data=None, params=None):
        response = requests.get(self.__make_path(path), headers=self.__headers, data=data, params=params)
        return self.__ark_request_filter(response)

    def post(self, path=None, data=None, params=None):
        response = requests.post(self.__make_path(path), headers=self.__headers, data=data, params=params)
        return self.__ark_request_filter(response)

    def delete(self, path=None, data=None, params=None):
        response = requests.delete(self.__make_path(path), headers=self.__headers, data=data, params=params)
        return self.__ark_request_filter(response)

    def put(self, path=None, data=None, params=None):
        response = requests.put(self.__make_path(path), headers=self.__headers, data=data, params=params)
        return self.__ark_request_filter(response)


def test():
    NITRAPI_LIVE_URL = "https://api.nitrado.net/"
    api = Client(NITRAPI_LIVE_URL)
    print('Get Nitrado Ping')
    print(pretty_json(api.get('ping')))
    print("\n")

    print('Get Nitrado Maintenance Status')
    print(pretty_json(api.get('maintenance')))
    print("\n")

    print('Get Nitrado Version')
    print(pretty_json(api.get('version')))
    print("\n")


if __name__ == '__main__':
    test()
