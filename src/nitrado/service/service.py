from __future__ import annotations
from ..lib import Client
from .details import Details
from .arguments import Arguments
from .task import Task
from .notification import Notification
from .action import Action
from .logs_page import LogsPage
from datetime import datetime


class Service:
    @classmethod
    def find_by_id(cls, service_id: int) -> Service:
        response = Client.get(path=f'/services/{service_id}')
        data: dict = response.json()['data']['service']
        data['details'] = Details(service_id, **data['details'])
        data['arguments'] = Arguments(service_id, **data['arguments'])
        return cls(**data)

    @classmethod
    def all(cls) -> list[Service]:
        response = Client.get(path='/services')
        data: dict = response.json()['data']
        servers = data['services']
        return [Service(**data) for data in servers]

    def __init__(
            self,
            id: int = None,
            location_id: int = None,
            status: str = None,
            status_code: int = None,
            websocket_token: str = None,
            user_id: int = None,
            username: str = None,
            comment: str = None,
            auto_extension: bool = None,
            auto_extension_duration: int = None,
            auto_extension_external: bool = False,
            type: str = None,
            type_human: str = None,
            details: Details = None,
            start_date: str = None,
            suspend_date: str = None,
            delete_date: str = None,
            suspending_in: int = None,
            deleting_in: int = None,
            readonly: bool = False,
            has_benefits: bool = False,
            arguments: Arguments = None,
            roles: list = None,
            is_owner: bool = False,
            servicetype: int = None,
            **kwargs
    ):
        self.id = id
        self.location_id = location_id
        self.status = status
        self.status_code = status_code
        self.websocket_token = websocket_token
        self.user_id = user_id
        self.username = username
        self.comment = comment
        self.auto_extension = auto_extension
        self.auto_extension_duration = auto_extension_duration
        self.auto_extension_external = auto_extension_external
        self.type = type
        self.type_human = type_human
        self.details = details
        self.start_date = None if start_date is None else datetime.fromisoformat(start_date)
        self.suspend_date = None if start_date is None else datetime.fromisoformat(suspend_date)
        self.delete_date = None if start_date is None else datetime.fromisoformat(delete_date)
        self.suspending_in = suspending_in
        self.deleting_in = deleting_in
        self.readonly = readonly
        self.has_benefits = has_benefits
        self.arguments = arguments
        self.roles = roles
        self.is_owner = is_owner
        self.servicetype = servicetype
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def logs(self) -> list:
        first = LogsPage.page(self.id, 1)
        logs = first.logs
        page = 2
        while page <= first.page_count:
            data = LogsPage.page(self.id, page)
            logs += data.logs
            page += 1
        return logs

    def notifications(self) -> list:
        path = f'/services/{self.id}/notifications'
        response = Client.get(path=path)
        items: list = response.json()['data']['notifications']
        notif = []
        for data in items:
            data['actions'] = [Action(self.id, **a) for a in data['actions']]
            notif.append(Notification(**data))
        return notif

    def tasks(self) -> list:
        path = f'/services/{self.id}/tasks'
        response = Client.get(path=path)
        data: dict = response.json()['data']['tasks']
        return [Task(self.id, **kwargs) for kwargs in data]

    def __repr__(self):
        id = f"id={repr(self.id)}"
        status = f"status={repr(self.status)}"
        params = ", ".join([id, status])
        return f"<Service({params}, ...)>"

