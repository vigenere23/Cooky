from app.infra.db.refactor.mysql_model import MysqlModel
from dataclasses import dataclass


@dataclass
class AccountModel(MysqlModel):
    firstName: str
    lastName: str
    email: str
    password: bytes
    id_User: int = None
    id_Address: int = None
    id: int = None

    def table_name(self) -> str:
        return 'Account'
