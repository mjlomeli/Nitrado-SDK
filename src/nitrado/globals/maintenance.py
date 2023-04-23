
class Maintenance:
    def __init__(
            self,
            cloud_backend: bool = False,
            domain_backend: bool = False,
            pmacct_backend: bool = False,
            dns_backend: bool = False
    ):
        self.cloud_backend = cloud_backend
        self.domain_backend = domain_backend
        self.pmacct_backend = pmacct_backend
        self.dns_backend: bool = dns_backend

    def __repr__(self):
        params = [f'{k}={repr(v)}' for k, v in self.__dict__.items()]
        return f"<{self.__class__.__name__}({', '.join(params)})>"
