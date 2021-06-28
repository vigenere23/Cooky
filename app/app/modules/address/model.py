from app.infra.db.models.base_model import BaseModel


class AddressModel(BaseModel):
    def __init__(self, id=None, number=None, apartment=None, street=None, city=None, country=None):
        self.id = id
        self.number = number
        self.apartment = apartment
        self.street = street
        self.city = city
        self.country = country
