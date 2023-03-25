from requests import get, post, put, delete, RequestException
import json


def pretty_json(data: dict):
    return json.dumps(data, indent=3, sort_keys=True)


def assert_response(response):
    if not response.ok:
        code = response.status_code
        reason = response.reason
        raise RequestException(f"Url error => {code} {reason} for:", response.url)


def get_content(response):
    content_type = response.headers['content-type'].split("; ")
    if 'application/json' in content_type:
        return response.json()
    return response.text


class Client:
    CLIENT = None

    def __init__(self, api_url, key=None):
        assert type(api_url) == str, "A string url must be provided in Client(api_url, key)"
        assert len(api_url) > 1, "Api URL's should include 'http://' or 'https://'"
        self.__headers = {'Authorization': key}
        self.__api_url = api_url if api_url[-1] == '/' else f"{api_url}/"
        Client.CLIENT = self

    def __make_path(self, path=None):
        if isinstance(path, str):
            return "{}{}".format(self.__api_url, path)
        elif isinstance(path, list):
            path_list = [str(directory) for directory in path]
            return "{}{}".format(self.__api_url, '/'.join(path_list))
        else:
            return self.__api_url

    def get(self, path=None, data=None, params=None):
        response = get(self.__make_path(path), headers=self.__headers, data=data, params=params)
        assert_response(response)
        return get_content(response)

    def post(self, path=None, data=None, params=None):
        response = post(self.__make_path(path), headers=self.__headers, data=data, params=params)
        assert_response(response)
        return get_content(response)

    def delete(self, path=None, data=None, params=None):
        response = delete(self.__make_path(path), headers=self.__headers, data=data, params=params)
        assert_response(response)
        return get_content(response)

    def put(self, path=None, data=None, params=None):
        response = put(self.__make_path(path), headers=self.__headers, data=data, params=params)
        assert_response(response)
        return get_content(response)
