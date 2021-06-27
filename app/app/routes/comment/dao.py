from app import db
from .model import CommentModel
from app.helpers.BaseDao import BaseDao


class CommentDao(BaseDao):

    def __init__(self):
        super().__init__('Comment', CommentModel)

    def save(self, commentModel):
        if not isinstance(commentModel, CommentModel):
            raise ValueError("commentModel should be of type CommentModel")
        query = 'INSERT INTO Comment (id, id_Recipe, id_User, text) VALUES (%s, %s, %s, %s)'
        newCommandId = db.create(query, self._mapper.to_tuple(commentModel))

        if newCommandId:
            return self.getById(newCommandId)
        else:
            raise Exception("Could not save commend")

    def getRecipeComments(self, id_Recipe):
        query = 'SELECT * FROM Comment WHERE Comment.id_Recipe = %(id_Recipe)s'
        results = db.findAll(query, {'id_Recipe': id_Recipe})
        return self._mapper.from_tuples(results)
