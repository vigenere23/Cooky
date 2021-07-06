from dataclasses import dataclass
from unittest import TestCase, main
from assertpy import assert_that
from app.infra.db.refactor.mysql_model import MysqlModel

@dataclass
class SomeModel(MysqlModel):
    rating: float = 12.4
    name: str = 'somewhat'
    id: int = None

    def table_name(self) -> str:
        return 'SomeTable'

    def get_id(self) -> str:
        return self.id

class MySQLModelTest(TestCase):

    def test_columns(self):
        model = SomeModel()

        columns = model.columns()

        expected = ['rating', 'name', 'id']
        assert_that(columns).contains_only(*expected)

    def test_insert_columns_template(self):
        model = SomeModel()

        template = model.insert_columns_template()

        expected = '(rating, name, id)'
        assert_that(template).is_equal_to(expected)

    def test_insert_values_template(self):
        model = SomeModel()

        template = model.insert_values_template()

        expected = '(%(rating)s, %(name)s, %(id)s)'
        assert_that(template).is_equal_to(expected)

    def test_update_entries_template(self):
        model = SomeModel()

        template = model.update_entries_template()

        expected = 'rating = %(rating)s, name = %(name)s'
        assert_that(template).is_equal_to(expected)

if __name__ == '__main__':
    main()
