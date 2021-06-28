from app.infra.db.models.base_model import BaseModel


class UserModel(BaseModel):

    def __init__(self, id=None, username=None):
        self.id = id
        self.username = username
