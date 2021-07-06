from typing import Type, TypeVar
from flask import request
from functools import wraps


T = TypeVar('T')
def parse_body(constructor: Type[T]):
    def decorator(f):
        @wraps(f)

        def wrapper(*args, **kwargs):
            json_string: dict = request.data.decode()
            parsed_request: T = constructor.from_json(json_string)

            return f(parsed_request, *args, **kwargs)

        return wrapper

    return decorator
