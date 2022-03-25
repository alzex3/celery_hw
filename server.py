import smtplib
from email.message import EmailMessage

from flask import request, jsonify

from settings import EMAIL_SENDER
from tasks import make_celery
from app import flask_app

celery = make_celery(flask_app)


@celery.task()
def email_task():
    email = request.get_json()
    msg = EmailMessage()
    msg['From'] = EMAIL_SENDER
    msg['To'] = 'arsenalnn1@gmail.com'
    msg['Subject'] = email.get("subject")
    msg.set_content(email.get("msg"))

    with smtplib.SMTP('localhost') as smtp:
        smtp.send_message(msg)
        return jsonify()
