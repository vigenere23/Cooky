from app.infra.db.models import BaseModel


class AccountModel(BaseModel):
    def __init__(self, id=None, id_User=None, id_Address=None, firstName=None, lastName=None, email=None, password=None):
        self.id = id
        self.id_User = id_User
        self.id_Address = id_Address
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
