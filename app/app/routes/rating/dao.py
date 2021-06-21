from app import db
from .model import RatingModel
from app.helpers.BaseDao import BaseDao

class RatingDao(BaseDao):

    def __init__(self):
        super().__init__('Rating', RatingModel)
    
    def save(self, ratingModel):
        if not isinstance(ratingModel, RatingModel):
            raise ValueError("ratingModel should be of type RatingModel")

        query = 'INSERT INTO Rating (id, id_Recipe, id_User, value) VALUES (%s, %s, %s, %s)'
        newItemId = db.insert(query, self._mapper.to_tuple(ratingModel))
        return self.getById(newItemId)

    def replace(self, ratingModel):
        if not isinstance(ratingModel, RatingModel):
            raise ValueError("ratingModel should be of type RatingModel")

        query = 'UPDATE Rating SET value = %(value)s WHERE id_User = %(id_User)s AND id_Recipe = %(id_Recipe)s'
        db.replace(query, { 'value': ratingModel.value, 'id_Recipe': ratingModel.id_Recipe, 'id_User': ratingModel.id_User })
        return self.getUserRecipeRating(ratingModel.id_User, ratingModel.id_Recipe)

    def getRatingsByUser(self, id_User):
        query = 'SELECT * FROM Rating WHERE Rating.id_User = %(id_User)s'
        results = db.select(query, { 'id_User': id_User })
        return self._mapper.from_tuples(results)

    def getUserRecipeRating(self, id_User, id_Recipe):
        query = 'SELECT * FROM Rating WHERE Rating.id_User = %(id_User)s AND Rating.id_Recipe = %(id_Recipe)s'
        results = db.select(query, { 'id_User': id_User, 'id_Recipe': id_Recipe })
        return self._mapper.from_tuples(results)
