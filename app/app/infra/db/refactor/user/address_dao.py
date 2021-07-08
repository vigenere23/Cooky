from typing import Optional
from app.infra.db.models.user import AddressModel
from app.infra.db.refactor.mysql_executor import MySQLExecutor


class AddressDao:

    def __init__(self):
        self.__table_name = 'Address'

    def find_by_id(self, executor: MySQLExecutor, address_id: int) -> Optional[AddressModel]:
        result = executor.find_by_id(self.__table_name, address_id)
        return AddressModel(**result) if result else None

    def save(self, executor: MySQLExecutor, address_model: AddressModel) -> int:
        return executor.create(address_model)
