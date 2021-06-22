# Contributing

## Adding new route modules

Create a new folder under `/routes` with the name of the module you want to add (generally, the name should match the route prefix associated, ex: `users` for the route prefix `/users`). Inside the new folder, create the following files:
1. `__init__.py`
2. `controller.py`
3. `dao.py`
4. `model.py` (only if you need one)

### `__init__.py`

```python
from app import app
from .controller import routes

app.register_blueprint(routes, url_prefix='/<WANTED_PREFIX>')
```

### `controller.py`

A controller is responsible for defining the available routes of the API and calling the right functions to get and format the needed data. 

```python
from flask import Blueprint
# import only helpers you need
from app.helpers import response, exceptions, queries
from .dao import SomeDao

routes = Blueprint('<MODULE_NAME>', __name__)
theUsedDao = SomeDao # should define an instance of the needed DAO

@routes.route('/<URL_SUFFIX>')
def some_name_related_to_this_route():
  return "some text or use the response helper"

# other routes below
```

> See the section below to learn more about the different helpers

### `dao.py`

A DAO is responsible for querying the database for the controllers. It should always inherit the BaseDao to ensure uniformity of methods. It should also define a `SQLMapper` instance to map the returned tuples from a table to the correct model. 

```python
from app import db
from .model import UserModel
from app.herlpers.SQLMapper import SQLMapper
from app.helpers.BaseDao import BaseDao
from app.helpers.exceptions import NotFoundException

class UserDao(BaseDao):
  def __init__(self):
    self.mapper = SQLMapper('User', UserModel)

  def getById(self, id):
    query = 'SELECT * FROM User WHERE id = %(id)s'
    result = db.select(query, { 'id': id }, 1)
    if result:
      return self.mapper.from_tuple(result)
    else:
      raise NotFoundException(str.format("No user found with id '%d'", id))
```

> Any DAO is responsible for raising the correct exception(s) from `app.helpers.exceptions`.
> You can always define new methods that are specific to that DAO (like `findByName` or `groupedByCategory`)

### `model.py` (only if needed)

Models are used to reiceive and return correctly formatted data to the user. **They should be able to receive any arbitrairy decomposed dict**. Normally, the class name should be suffixed by `Model`. Any model should inherit the `BaseModel` class from `app.helpers` for automatic serialization (and maybe deserialization in the future). 

```python
from app.helpers.BaseModel import BaseModel

class ModuleNameModel(BaseModel):
  def __init__(self, id=None, other_attribute=None):
    self.id = id
    self.other_attribute = other_attribute
```

## Understanding the helpers

A list for usefull helpers can be found in the `app.helpers` module. They offer simplicity and abstraction to help better code and standarize the flow of information. Here are some of the most usefull ones: 

### `DB`

Simple class wrapping the `MySQL-connector` driver. It automatically opens connections, calls the cursor, fetch results, commit changes, etc.

> YOu should NEVER create your own instance of the DB class. Instead, use the one defined in the app by using `from app import db`.

#### `DB.select(query, data=None, limit=0)`

Used for selecting data in the database. You can limit the number of results (0 = no-limit) with `limit`. `data` can be used if your query needs to be formatted with some values, ex: `SELECT * FROM User WHERE id = %s`.

> IMPORTANT : The `data` argument **must** be a `tuple` or a `map`. To know more about the correct syntax, please check the MySQL Python driver doc. 

#### `DB.insert(query, data)`

Used for inserting a *single* row. The `query` and `data` arguments remain the same. 

#### `DB.insertMany(query, data)`

Used for inserting `more than one` row. The `data` argument **must** be a list of tuple or map. The function will call the cursor to iterate over the data and re-execute the same `query` for each data. 

### `exceptions`

The `exceptions` helper contains all the exceptions that a controller or dao (or model) could raise. It helps specify the type of error that occured and will be parsed and mapped to the correct error code with the helper `response.handleExceptions`. 

### `response`

The `response` helper contains the functions used for returning a response to the client. It helps adding the correct `content-type` header and parsing the data to an understandable way for the browser (`json` or `text`). 

#### `response.success(data, status=200)`

Returns the data parsed as json (or text) with the status specified. By default, the returned status is `200 OK`.

> A success status will normally be between 100 and 399, since 4xx and 5xx are reserved for errors.

#### `response.error(error, status=500`

Returns a json object containing the field `error` containing the specified error message. By default, the status code `500 INTERNAL SERVER ERROR` will be returned, although it should more often be a user error (in the 4xx range). 

#### `@response.handleErrors`

A decorator to be used around Flask routing functions to handle the automatic parsing of errors. 

Example:

```python
@routes.route('/<int:id>')
@response.handleExceptions
def getOne(id):
  data = dao.getById(id)
  return response.success(data)
```

Here, `dao.getById()` could raise a `NotFOundException`. To catch it and return it to the client with the correct format (`{ error: "error message" }`), we simply put the decorator right under the route specification. 

### `BaseModel`

The `BaseModel` class is only meant to be inherited by model classes, and **not** used directly. It is configured to automatically serialize data to return to the user. Any model can override the `serialize` method to remove any unwanted fileds. 

### `queries`

This one should not be usefull. It is used by the `SQLMapper` class. 

It may contains in the future other usefull and often used queries. 
