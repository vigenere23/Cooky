import unittest
from app.infra.db.refactor.condition import Condition
from unittest import TestCase

class ConditionTest(TestCase):

    def test_query(self):
        condition = Condition().where(
            ['Comment.id = %(id_Comment)s', 'Recipe.name LIKE %(name)s'], data={'id_Comment': 123, 'name': 'lolo'}
        ).where(
            ['Recipe.type = ITALIAN'], data={'rating': 0}
        ).where([])

        query = condition.query()
        data = condition.data()

        expected_query = 'WHERE (Comment.id = %(id_Comment)s AND Recipe.name LIKE %(name)s) OR (Recipe.type = ITALIAN)'
        expected_data = {'id_Comment': 123, 'name': 'lolo', 'rating': 0}

        self.assertEqual(query, expected_query)
        self.assertEqual(data, expected_data)

if __name__ == '__main__':
    unittest.main()
