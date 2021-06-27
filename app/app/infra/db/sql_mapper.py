from app import db


class SQLMapper:
    def __init__(self, table_name, model_class):
        self.table_name = table_name
        self.column_names = []
        self.model_class = model_class

        column_infos = db.getColumns(self.table_name)
        for column_info in column_infos:
            self.column_names.append(column_info[0])

    def from_tuples(self, sql_tuples):
        models = []
        for sql_tuple in sql_tuples:
            models.append(self.from_tuple(sql_tuple))
        return models

    def from_tuple(self, sql_tuple):
        model = {}
        for (i, value) in enumerate(sql_tuple):
            model[self.column_names[i]] = value
        return self.model_class(**model)

    def to_tuple(self, model):
        if not isinstance(model, self.model_class):
            raise ValueError("model should be of type {}".format(
                type(self.model_class).__name__))
        values = []
        for column_name in self.column_names:
            values.append(getattr(model, column_name))

        return tuple(values)
