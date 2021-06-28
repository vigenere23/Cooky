from .model import QuantityTypeModel
from app.infra.db.base_dao import BaseDao


class QuantityTypeDao(BaseDao):

    def __init__(self):
        super().__init__('QuantityType', QuantityTypeModel)

    def save(self, quantityTypeModel):
        if not isinstance(quantityTypeModel, QuantityTypeModel):
            raise ValueError(
                "quantityTypeModel should be of type QuantityTypeModel")
