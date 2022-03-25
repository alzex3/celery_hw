from flask import Blueprint

from api.view import AdvertsView, AdvertView, TaskView


main_blueprint = Blueprint('main', __name__)


main_blueprint.add_url_rule(
    '/api/adverts',
    view_func=AdvertsView.as_view('adverts'),
    methods=['POST', 'GET'],
)

main_blueprint.add_url_rule(
    '/api/advert/<int:advert_id>',
    view_func=AdvertView.as_view('advert'),
    methods=['GET', 'PUT', 'DELETE'],
)

main_blueprint.add_url_rule(
    '/api/tasks',
    view_func=TaskView.as_view('run_task'),
    methods=['POST'],
)

main_blueprint.add_url_rule(
    '/api/tasks/<task_id>',
    view_func=TaskView.as_view('get_status'),
    methods=['GET'],
)
