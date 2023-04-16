from nitrado.tools import Client
import json


class Service:
    def __init__(self, client: Client, data: dict):
        self.__client = client
        self.__data = data

        self.id = None
        self.location_id = None
        self.status = None
        self.status_code = None
        self.websocket_token = None
        self.user_id = None
        self.username = None
        self.comment = None
        self.auto_extension = None
        self.auto_extension_duration = None
        self.auto_extension_external = None
        self.type = None
        self.type_human = None
        self.details = None
        self.start_date = None
        self.suspend_date = None
        self.delete_date = None
        self.suspending_in = None
        self.deleting_in = None
        for k, v in data.items():
            self.__dict__[k] = v

    def log_page(self, page: int) -> dict:
        assert page > 0, "Page number must be greater than 0"
        path = f'/services/{self.id}/logs'
        response = self.__client.get(path=path, data={'page': page})
        data: dict = response.json()['data']
        return data

    def logs(self) -> list:
        first = self.log_page(1)
        logs = first['logs']
        page = 2
        last_page = first['page_count']
        while page <= last_page:
            data = self.log_page(page)
            logs += data['logs']
            page += 1
        return logs

    def notifications(self) -> list:
        path = f'/services/{self.id}/notifications'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data['notifications']

    def tasks(self) -> list:
        path = f'/services/{self.id}/tasks'
        response = self.__client.get(path=path)
        data: dict = response.json()['data']
        return data['tasks']

    def create_task(self, action_method=None, month="*", day="*", hour="24", minute="0", weekday="*", action_data=None) -> bool:
        path = f'/services/{self.id}/tasks'
        params = {'action_method': action_method, 'action_data': action_data, 'minute': minute,
                  'hour': hour, 'day': day, 'month': month, 'weekday': weekday}
        response = self.__client.post(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def update_task(self, task_id=None, action_method=None, month="*", day="*", hour="*", minute="*", weekday="*", action_data=None) -> bool:
        path = f'/services{self.id}/tasks/task_id'
        params = {'action_method': action_method, 'action_data': action_data, 'minute': minute,
                  'hour': hour, 'day': day, 'month': month, 'weekday': weekday}
        response = self.__client.put(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def delete_task(self, task_id) -> bool:
        path = f'/services/{self.id}/tasks/{task_id}'
        response = self.__client.delete(path=path)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def __contains__(self, item):
        return item in self.__data

    def __getitem__(self, item):
        return self.__data[item]

    def keys(self):
        return self.__data.keys()

    def __iter__(self):
        return iter(self.__data)

    def __repr__(self):
        id = f"id={repr(self.id)}"
        status = f"status={repr(self.status)}"
        type_human = f"type_human={repr(self.type_human)}"
        suspend_date = f"suspend_date={repr(self.suspend_date)}"
        params = ", ".join([id, status, type_human, suspend_date])
        return f"<Service({params})>"

    def __str__(self):
        return json.dumps(self.__data, indent=3)
