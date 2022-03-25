from flask import Flask

from api.models import db
from api.schemes import ma
from router import main_blueprint
from settings import PG_DSN, CELERY_RESULT_BACKEND, CELERY_BROKER_URL


flask_app = Flask(__name__)

flask_app.config.update(
    SQLALCHEMY_DATABASE_URI=PG_DSN,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    CELERY_RESULT_BACKEND=CELERY_RESULT_BACKEND,
    CELERY_BROKER_URL=CELERY_BROKER_URL,
)

flask_app.register_blueprint(main_blueprint)

db.init_app(flask_app)
ma.init_app(flask_app)
