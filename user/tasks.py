from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail



@shared_task
def email_send(subject, message,  **kwargs):
    send_mail(subject, message, kwargs['instance'].email, [settings.EMAIL_HOST_USER])