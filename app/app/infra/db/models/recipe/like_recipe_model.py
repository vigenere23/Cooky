from app.infra.db.models import BaseModel


class LikeRecipeModel(BaseModel):
    def __init__(self, id=None, id_Recipe=None, id_User=None,):
        self.id = id
        self.id_Recipe = id_Recipe
        self.id_User = id_User
