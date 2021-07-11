from dataclasses import asdict, is_dataclass
import flask
from functools import wraps
from app.domain.exceptions import NotFoundException, ForbiddenException


def __create(data, status):
    mimetype = 'text/plain'

    if not isinstance(data, str):
        data = __json(data)
        mimetype = 'application/json'

    return flask.Response(data, status=status, mimetype=mimetype)


def __json(data):
    if is_dataclass(data):
        data = asdict(data)
    elif isinstance(data, list) and len(data) > 0 and is_dataclass(data[0]):
        data = [asdict(item) for item in data]

    return flask.json.dumps(data)


def success(data, status=200):
    return __create(data, status)


def error(exception, status=500):
    if not isinstance(exception, str):
        exception = str(exception)

    return __create({
        'error': exception
    }, status)


def empty():
    return success('', status=204)


def handleExceptions(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except NotFoundException as e:
            return error(e, 404)
        except ForbiddenException as e:
            return error(e, 403)
        except Exception as e:
            print(e)
            return error(e)
    return wrapper
