
from enum import Enum
from sanic import response


class ResponseCode(Enum):
    OK = 0
    FAIL = 1


def response_json(code=ResponseCode.OK, message="", status=200, **data):
    return response.json({
        "code": code.value,
        "message": message,
        "data": data
    }, status)
