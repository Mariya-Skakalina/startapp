from startapp.celery import app
from django.conf import settings
from django.core.mail import send_mail



@app.task(bind=True)
def email_send(self, subject, message,  email):
    send_mail(subject, message, email, [settings.EMAIL_HOST_USER])
