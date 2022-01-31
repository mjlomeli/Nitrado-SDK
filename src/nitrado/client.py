import requests
import json


class Client:
    CLIENT = None

    def __init__(self, api_url, key):
        assert type(api_url) == str, "A string key.txt must be provided in Client(api_url, key.txt)"
        assert len(api_url) > 1, "Api URL's should include 'http://' or 'https://'"
        self.__headers = {'Authorization': key} if key else None
        self.__api_url = api_url if api_url[-1] == '/' else f"{api_url}/"

    def __make_path(self, path=None):
        if isinstance(path, str):
            return "{}{}".format(self.__api_url, path)
        elif isinstance(path, list):
            path_list = [str(directory) for directory in path]
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
