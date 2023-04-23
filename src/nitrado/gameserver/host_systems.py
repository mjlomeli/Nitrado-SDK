from .operating_system import OperatingSystem


class HostSystem:
    def __init__(
            self,
            service_id: int,
            linux: OperatingSystem = None,
            windows: OperatingSystem = None,
            macos: OperatingSystem = None,
            **kwargs
    ):
        self.linux = linux
        self.windows = windows
        self.macos = macos
        self.service_id = service_id
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __repr__(self):
        linux = f"linux={'<OperatingSystem>' if self.linux else 'None'}"
        windows = f"windows={'<OperatingSystem>' if self.windows else 'None'}"
        macos = f"macos={'<OperatingSystem>' if self.macos else 'None'}"
        params = [s for s in [linux, windows, macos]]
        return f"<{self.__class__.__name__}({', '.join(params)})>"
