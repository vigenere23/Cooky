from app import db
from .model import LikeRecipeModel
from app.helpers.BaseDao import BaseDao

class LikeRecipeDao(BaseDao):

    def __init__(self):
        super().__init__('LikeRecipe', LikeRecipeModel)

    def getLikeRecipeByUser(self, id_User):
        query = 'SELECT * FROM LikeRecipe WHERE id_User = %(id_User)s'
        results = db.select(query, {'id_User': id_User})
        return self._mapper.from_tuples(results)

    def save(self, likeRecipeModel):
        if not isinstance(likeRecipeModel, LikeRecipeModel):
            raise ValueError("likeRecipeModel should be of type LikeRecipeModel")
        query = 'INSERT INTO LikeRecipe (id, id_Recipe, id_User) VALUES (%s, %s, %s)'
        newLikeRecipe = db.insert(query, self._mapper.to_tuple(likeRecipeModel))

        if newLikeRecipe:
            return self.getById(newLikeRecipe)
        else:
            raise Exception("Could not like this recipe")

    def delete(self, likeRecipeModel):
        if not isinstance(likeRecipeModel, LikeRecipeModel):
            raise ValueError("likeRecipeModel should be of type LikeRecipeModel")
        query = 'DELETE FROM LikeRecipe WHERE LikeRecipe.id_Recipe = %(id_Recipe)s AND LikeRecipe.id_User = %(id_User)s'
        db.delete(query, { 'id_Recipe': likeRecipeModel.id_Recipe, 'id_User': likeRecipeModel.id_User })
