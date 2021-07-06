DEBUG = True


# Работа с почтой
EMAIL_HOST_USER = 'scka.maria@gmail.com'
if not DEBUG:
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_PASSWORD = 'Zombi@1997'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
else:
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = './email.log'
