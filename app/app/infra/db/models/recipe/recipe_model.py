from dataclasses import dataclass
from app.infra.db.refactor.mysql_model import MysqlModel


# see usage for `frozen` attribute
@dataclass
class RecipeModel(MysqlModel):
    id_User: int
    name: str
    directives: str
    description: str
    id: int = None
    rating: float = 0

    def table_name(self) -> str:
        return 'Recipe'
