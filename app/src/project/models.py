from django.db import models

class BaseModel(models.Model):
    maked = models.DateTimeField('Создано',auto_now_add = True)
    updated = models.DateTimeField('Обновлено',auto_now=True)
    class Meta:
        abstract = True