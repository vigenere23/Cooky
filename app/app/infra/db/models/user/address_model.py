from app.infra.db.refactor.mysql_model import MysqlModel
from dataclasses import dataclass


@dataclass
class AddressModel(MysqlModel):
    number: int
    street: str
    city: str
    country: str
    apartment: int = None
    id: int = None

    def table_name(self) -> str:
        return 'Address'
