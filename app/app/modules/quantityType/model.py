from app.domain.base_model import BaseModel


class QuantityTypeModel(BaseModel):
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
