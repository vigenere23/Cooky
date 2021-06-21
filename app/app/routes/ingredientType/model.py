from app.helpers.BaseModel import BaseModel

class IngredientTypeModel(BaseModel):
  def __init__(self, id=None, name=None):
    self.id = id
    self.name = name