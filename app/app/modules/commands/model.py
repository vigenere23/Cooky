from app.infra.db.models.base_model import BaseModel


class CommandModel(BaseModel):
    def __init__(self, id=None, id_Cart=None, creationDate=None, arrivalDate=None):
        self.id = id
        self.id_Cart = id_Cart
        self.creationDate = creationDate
        self.arrivalDate = arrivalDate
