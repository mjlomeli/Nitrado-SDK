from __future__ import annotations
from datetime import datetime
from ..lib.client import Client


class Task:
    @classmethod
    def create_task(
            cls,
            service_id: int,
            action_method=None,
            month="*",
            day="*",
            hour="24",
            minute="0",
            weekday="*",
            action_data=None
    ) -> Task:
        path = f'/services/{service_id}/tasks'
        params = {'action_method': action_method, 'action_data': action_data, 'minute': minute,
                  'hour': hour, 'day': day, 'month': month, 'weekday': weekday}
        response = Client.post(path=path, params=params)
        data: dict = response.json()
        if not response.ok and data['status'] == 'success':
            raise Exception(response.text)
        return cls(service_id=service_id, **params)

    def __init__(
            self,
            service_id: int,
            id: int = None,
            status: str = None,
            minute: str = None,
            hour: str = None,
            day: str = None,
            month: str = None,
            weekday: str = None,
            next_run: str = None,
            last_run: str = None,
            timezone: str = None,
            action_method: str = None,
            action_data: str = None,
            **kwargs
    ):
        self.id = id
        self.status = status
        self.minute = minute
        self.hour = hour
        self.day = day
        self.month = month
        self.weekday = weekday
        self.next_run = None if next_run is None else datetime.fromisoformat(next_run)
        self.last_run = None if last_run is None else datetime.fromisoformat(last_run)
        self.timezone = timezone
        self.action_method = action_method
        self.action_data = action_data
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def update_task(self) -> bool:
        path = f'/services{self.service_id}/tasks/{self.id}'
        params = {
            'action_method': self.action_method, 'action_data': self.action_data, 'minute': self.minute,
            'hour': self.hour, 'day': self.day, 'month': self.month, 'weekday': self.weekday}
        response = Client.put(path=path, params=params)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def delete_task(self) -> bool:
        path = f'/services/{self.service_id}/tasks/{self.id}'
        response = Client.delete(path=path)
        data: dict = response.json()
        return response.ok and data['status'] == 'success'

    def __repr__(self):
        params = [f'{k}={repr(v)}' for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"
