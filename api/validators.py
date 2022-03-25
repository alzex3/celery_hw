from marshmallow import ValidationError
from flask import jsonify, request, helpers

from api.models import Advert
from api.schemes import AdvertSchema


def is_valid(func):
    def wrapper(*args, **kwargs):

        try:
            AdvertSchema().load(request.get_json())

        except ValidationError as err:
            return helpers.make_response(
                jsonify(error=err.messages),
                400
            )

        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper


def is_exist(func):
    def wrapper(*args, **kwargs):

        try:
            advert_id = request.view_args.get('advert_id')
            if not Advert.query.get(advert_id):
                raise AssertionError

        except AssertionError:
            return helpers.make_response(
                jsonify(error='Advert not found!'),
                404
            )

        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper
