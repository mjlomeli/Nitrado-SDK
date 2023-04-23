from __future__ import annotations
from ..lib.client import Client
from .log import Log


class LogsPage:
    @classmethod
    def page(cls, service_id: int, page: int) -> LogsPage:
        assert page > 0, "Page number must be greater than 0"
        path = f'/services/{service_id}/logs'
        response = Client.get(path=path, data={'page': page})
        data: dict = response.json()['data']
        data['logs'] = [Log(service_id, **log) for log in data['logs']]
        return cls(service_id, **data)

    def __init__(
            self,
            service_id: int,
            current_page: int = 1,
            logs_per_page: int = 0,
            page_count: int = 0,
            log_count: int = 0,
            logs: list = None,
            **kwargs
    ):
        self.current_page = current_page
        self.page_count = page_count
        self.log_count = log_count
        self.logs = [] if logs is None else logs
        self.logs_per_page = logs_per_page
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __iter__(self):
        return iter(self.logs)

    def __contains__(self, item):
        return item in self.logs

    def __getitem__(self, item):
        return self.logs[item]

    def __len__(self):
        return len(self.logs)

    def __repr__(self):
        params = [f'{k}={repr(v)}' for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"

