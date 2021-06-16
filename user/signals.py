from django.db.models.signals import post_save, pre_save 
from django.core.mail import send_mail
from django.dispatch import receiver
from django.conf import settings
from .models import User
from .tasks import email_send
import string
import random
import crypt


# Хэширование пароля
@receiver(pre_save, sender = User)
def hash_password(sender,  **kwargs):
    letters_and_digits = string.ascii_letters + string.digits
    crypt_rand_string = ''.join(random.choice(letters_and_digits) for _ in range(16))
    kwargs['instance'].code_activate = crypt_rand_string
    kwargs['instance'].password = crypt.crypt(str(kwargs['instance'].password), settings.SECRET_KEY)
    
    
# Код для активации почты
@receiver(post_save, sender = User)
def code_activation(sender,  **kwargs):
    subject = "Письмо для активации почтового сервера"
    message = kwargs['instance'].code_activate
    email_send.delay(subject, message, kwargs['instance'].email)
