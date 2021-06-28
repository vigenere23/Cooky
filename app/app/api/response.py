import flask
import traceback
from functools import wraps
from ..domain.exceptions import NotFoundException, ForbiddenException


def __create(data, status):
    mimetype = 'text/plain'

    if not isinstance(data, str):
        data = __json(data)
        mimetype = 'application/json'

    return flask.Response(data, status=status, mimetype=mimetype)


def __json(data):
    if isinstance(data, list):
        try:
            data = [x.serialize() for x in data]
        except Exception:
            pass
    else:
        try:
            data = data.serialize()
        except Exception:
            pass

    return flask.json.dumps(data)


def success(data, status=200):
    return __create(data, status)


def error(error, status=500):
    if not isinstance(error, str):
        error = str(error)

    return __create({
        'error': error
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
            traceback.print_exc()
            return error(e)
    return wrapper


def ensureIdentity(id, identity):
    if id != identity.id:
        raise ForbiddenException()
