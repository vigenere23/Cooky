from dataclasses import dataclass
from typing import Any

@dataclass
class SQLQuery:
    template: str
    data: Any
