from flask.views import MethodView

from api.controller import get_advert, get_adverts, delete_advert, create_advert, update_advert, run_task, get_status


class AdvertsView(MethodView):
    @staticmethod
    def get():
        return get_adverts()

    @staticmethod
    def post():
        return create_advert()


class AdvertView(MethodView):
    @staticmethod
    def get(advert_id):
        return get_advert(advert_id)

    @staticmethod
    def put(advert_id):
        return update_advert(advert_id)

    @staticmethod
    def delete(advert_id):
        return delete_advert(advert_id)


class TaskView(MethodView):
    @staticmethod
    def post():
        return run_task()

    @staticmethod
    def get(task_id):
        return get_status(task_id)
