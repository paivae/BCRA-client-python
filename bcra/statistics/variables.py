from bcra.base import BaseClient
from bcra.config import ConfigClient


class Variables(BaseClient):

    def __init__(self, config: ConfigClient, path_root) -> None:
        self.path = path_root + "principalesvariables"
        super().__init__(config)

    def get(self,
            id_variable: int = None,
            from_: str = None,
            to: str = None):
        path_params = ""

        if (id_variable != None and from_ != None and to != None):
            path_params = f"{self.path}/{id_variable}/{from_}/{to}"

        return self._get(path=self.path, params=path_params)
