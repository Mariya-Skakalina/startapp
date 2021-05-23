import os

from celery import Celery

# установить модуль настроек Django по умолчанию для программы 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'startapp.settings')

app = Celery('startapp')

# Использование строки здесь означает, что работнику не нужно сериализовать объект конфигурации для дочерних процессов.
# namespace = 'CELERY' означает все ключи конфигурации, связанные с сельдереем  должен иметь префикс CELERY_.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загружать модули задач из всех зарегистрированных конфигураций приложений Django.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')