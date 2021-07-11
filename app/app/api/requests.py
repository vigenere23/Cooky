from typing import Type, TypeVar
from flask import request
from functools import wraps


T = TypeVar('T')
def parse_body(constructor: Type[T]):
    def decorator(f):
        @wraps(f)

        def wrapper(*args, **kwargs):
            json_string: dict = request.data.decode()
            try:
                parsed_request: T = constructor.from_json(json_string)
                return f(parsed_request, *args, **kwargs)
            except KeyError as e:
                raise Exception(f"Error parsing request: '{e.args[0]}' cannot be empty")

        return wrapper

    return decorator
