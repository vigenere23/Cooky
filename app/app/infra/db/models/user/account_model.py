from app.infra.db.refactor.mysql_model import MysqlModel
from dataclasses import dataclass


@dataclass
class AccountModel(MysqlModel):
    id_User: int
    id_Address: int
    firstName: str
    lastName: str
    email: str
    password: bytes
    id: int = None

    def table_name(self) -> str:
        return 'Account'
