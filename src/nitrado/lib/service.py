from nitrado.tools import Client


def assert_success(response):
    if not response:
        return
    if 'status' not in response or response['status'] != 'success':
        raise AssertionError(f"API returned: {response}")


class Service:

    def __init__(self, client: Client, data: dict):
        self.__client = client

        assert type(data) == dict, f"constructor only accepts type dict: Service({data})"
        self.id = data['id'] if 'id' in data else None
        self.location_id = data['location_id'] if 'location_id' in data else None
        self.status = data['status'] if 'status' in data else None
        self.status_code = data['status_code'] if 'status_code' in data else None
        self.websocket_token = data['websocket_token'] if 'websocket_token' in data else None
        self.user_id = data['user_id'] if 'user_id' in data else None
        self.username = data['username'] if 'username' in data else None
        self.comment = data['comment'] if 'comment' in data else None
        self.auto_extension = data['auto_extension'] if 'auto_extension' in data else None
        self.auto_extension_duration = data['auto_extension_duration'] if 'auto_extension_duration' in data else None
        self.auto_extension_external = data['auto_extension_external'] if 'auto_extension_external' in data else None
        self.type = data['type'] if 'type' in data else None
        self.type_human = data['type_human'] if 'type_human' in data else None
        self.details = data['details'] if 'details' in data else None
        self.start_date = data['start_date'] if 'start_date' in data else None
        self.suspend_date = data['suspend_date'] if 'suspend_date' in data else None
        self.delete_date = data['delete_date'] if 'delete_date' in data else None
        self.suspending_in = data['suspending_in'] if 'suspending_in' in data else None
        self.deleting_in = data['deleting_in'] if 'deleting_in' in data else None

    def __get_log_page(self, page: int) -> dict:
        log = self.__client.get(path=['services', self.id, 'logs'], data={'page': page})
        assert 'status' in log, "Failed to communicate to server."
        assert log['status'] == 'success', "Failed to get logs."
        return log['data']

    def logs(self, page: int = None):
        if page:
            return self.__get_log_page(page)['logs']
        data = self.__get_log_page(1)
        logs = data['logs']
        current_page_num = 2
        while current_page_num <= data['page_count']:
            data = self.__get_log_page(current_page_num)
            logs += data['data']['logs']
            current_page_num += 1
        return logs

    def notifications(self):
        notify = self.__client.get(path=['services', self.id, 'notifications'])
        assert_success(notify)
        return notify['data']['notifications']

    def tasks(self):
        path = ['services', self.id, 'tasks']
        tasks = self.__client.get(path=path)
        assert_success(tasks)
        return tasks['data']['tasks']

    def create_task(self, action_method=None, month="*", day="*", hour="24", minute="0", weekday="*", action_data=None):
        path = ['services', self.id, 'tasks']
        params = {'action_method': action_method, 'action_data': action_data, 'minute': minute,
                  'hour': hour, 'day': day, 'month': month, 'weekday': weekday}
        try:
            self.__client.post(path=path, params=params)
            return True
        except Exception as e:
            print(e)
            return False

    def update_task(self, task_id=None, action_method=None, month="*", day="*", hour="*", minute="*", weekday="*", action_data=None):
        path = ['services', self.id, 'tasks', task_id]
        params = {'action_method': action_method, 'action_data': action_data, 'minute': minute,
                  'hour': hour, 'day': day, 'month': month, 'weekday': weekday}
        try:
            self.__client.put(path=path, params=params)
            return True
        except Exception as e:
            print(e)
            return False

    def delete_task(self, task_id):
        path = ['services', self.id, 'tasks', task_id]
        try:
            self.__client.delete(path=path)
            return True
        except Exception as e:
            print(e)
            return False

    def __repr__(self):
        return f"<Service(id={self.id}, username='{self.username}', details={self.details})>"

    def __str__(self):
        return f"""
        id = {self.id}
        location_id = {self.location_id}
        status = '{self.status}'
        status_code = {self.status_code}
        websocket_token = '{self.websocket_token}'
        user_id = {self.user_id}
        username = '{self.username}'
        comment = {self.comment}
        auto_extension = {self.auto_extension}
        auto_extension_duration = {self.auto_extension_duration}
        auto_extension_external = {self.auto_extension_external}
        type = '{self.type}'
        type_human = '{self.type_human}'
        details = {self.details}
        start_date = '{self.start_date}'
        suspend_date = '{self.suspend_date}'
        delete_date = '{self.delete_date}'
        suspending_in = {self.suspending_in}
        deleting_in = {self.deleting_in}
        """
