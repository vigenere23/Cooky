from app.helpers import queries

class SQLMapper:
  def __init__(self, table_name, modelClass):
    self.table_name = table_name
    self.column_names = []
    self.modelClass = modelClass

    column_infos = queries.getColumns(self.table_name)
    for column_info in column_infos:
      self.column_names.append(column_info[0])

  def from_tuples(self, SQLtuples):
    models = []
    for SQLtuple in SQLtuples:
      models.append(self.from_tuple(SQLtuple))
    return models

  def from_tuple(self, SQLtuple):
    model = {}
    for (i, value) in enumerate(SQLtuple):
      model[self.column_names[i]] = value
    return self.modelClass(**model)

  def to_tuple(self, model):
    if not isinstance(model, self.modelClass):
      raise ValueError("model should be of type {}".format(type(self.modelClass).__name__))
    values = []
    for column_name in self.column_names:
      values.append(getattr(model, column_name))
    
    return tuple(values)
