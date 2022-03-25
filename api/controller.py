from celery.result import AsyncResult
from flask import jsonify, request

from api.models import db, Advert
from api.schemes import AdvertSchema
from api.validators import is_valid, is_exist

from server import email_task

advert_schema = AdvertSchema()
adverts_schema = AdvertSchema(many=True)


def get_adverts():
    adverts = Advert.query.all()

    return adverts_schema.jsonify(adverts)


@is_exist
def get_advert(advert_id):
    advert = Advert.query.get(advert_id)

    return advert_schema.jsonify(advert)


@is_valid
def create_advert():
    new_advert_attrs = request.get_json()
    new_advert = Advert(**new_advert_attrs)

    db.session.add(new_advert)
    db.session.commit()

    return advert_schema.jsonify(new_advert)


@is_exist
@is_valid
def update_advert(advert_id):
    update_advert_attrs = request.get_json()
    Advert.query.filter_by(id=advert_id).update(update_advert_attrs)

    db.session.commit()
    updated_advert = Advert.query.get(advert_id)

    return advert_schema.jsonify(updated_advert)


@is_exist
def delete_advert(advert_id):
    advert = Advert.query.get(advert_id)

    db.session.delete(advert)
    db.session.commit()

    return jsonify()


def run_task():
    task = email_task(request).delay()

    return jsonify({'task_id': task.id}), 202


def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }

    return jsonify(result), 200
