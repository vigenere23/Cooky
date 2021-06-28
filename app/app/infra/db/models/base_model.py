class BaseModel:
    def serialize(self):
        return self.__dict__
