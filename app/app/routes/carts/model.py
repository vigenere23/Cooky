from app.helpers.BaseModel import BaseModel

class CartModel(BaseModel):
  def __init__(self, id=None, id_User=None, totalCost=0):
    self.id = id
    self.id_User = id_User
    self.totalCost = totalCost