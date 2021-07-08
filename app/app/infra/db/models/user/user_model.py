from dataclasses import dataclass
from app.infra.db.refactor.mysql_model import MysqlModel


@dataclass
class UserModel(MysqlModel):
    username: str
    id: int = None

    def table_name(self) -> str:
        return 'User'
