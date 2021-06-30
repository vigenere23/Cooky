# Refactor - Database

The database refactor aims for a more interfaced model, with repository abstractions, abstract transactions handling and logic encapsulation.

## Flow

```
UseCase -> Repository |>
    MysqlRepository ->
        (DbConnection |>) -> MySQLDbConnection ->
            mysql.BaseConnection (cursor, commit, rollback)
            mysql.BaseCursor (close)
        Dao ->
            MySQLExecutor ->
                mysql.BaseCursor (execute)

-> : uses
|> : implements
() : optional
```

## Possible implementation

```py
class RecipeCreationUseCase:
    def create_recipe(self, *args):
        recipe = self.__recipe_factory.create(*args)
        recipe_id = self.__recipe_repository.save(recipe)
        return recipe_id

class MysqlRecipeRepository(RecipeRepository):
    def save(self, recipe: Recipe) -> int:
        try:
            recipe_id = self.__db_connection.execute(lambda executor: self.__start_transaction(executor, recipe))
            return recipe_id
        except Exception as e:
            raise CouldNotSaveRecipeException(e)

    def __save_transaction(self, executor: MysqlExecutor, recipe) -> int:
        # all dao actions here
        recipe_id = self.__recipe_dao.save(executor, recipe)

        for ingredient in recipe.get_ingredients():
            self.__ingredient_dao.save(executor, ingredient)
            self.__recipe_ingredient_dao.save(executor, recipe_id, ingredient)

        for comment in recipe.get_comments():
            self.__comment_dao.save(executor, recipe_id, comment)

        return recipe_id

class RecipeDao:
    def save(self, executor: MysqlExecutor, recipe: Recipe):
        model = self.__recipe_model_assembler.to_dto(recipe)
        query = "INSERT INTO Recipe (id, id_User, title) VALUES (%s, %s, %s)"
        return executor.create(query, data) # returns lastrowid()

class MysqlDBConnection(DBConnection):
    T = TypeVar('T')
    def execute(self, action: Callable[[MysqlExecutor], T]) -> T:
        cursor = self.__connection.cursor()
        executor = self.__connection.create_executor(cursor)
        try:
            result = callable(executor) # -> calls once or multiple times `executor.xxx(query, data)`
            connection.commit()
            return result
        except Exception:
            connection.rollback()
        finally:
            cursor.close()

class MysqlExecutor:
    __cursor: mysql.cursor

    def find(self, query, data=None):
        cursor.execute(...)

    def findAll(self, query, data=None):
        cursor.execute(...)

    def create(self, query, data) -> int:
        cursor.execute(...)
        return cursor.lastrowid()
```
