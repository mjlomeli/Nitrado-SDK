class _User:
    def __init__(self):
        self.__id = None
        self.__username = None

    def id(self):
        return self.__id

    def username(self):
        return self.__username


class AccessToken:
    def __init__(self):
        self.__user = None
        self.__expires_at = None
        self.__valid_until = None
        self.__scopes = []
        self.__employee = False

    def user(self):
        return self.__user

    def expires_at(self):
        return self.__expires_at

    def valid_until(self):
        return self.__valid_until

    def scopes(self):
        return self.__scopes

    def is_employee(self):
        return self.__employee


