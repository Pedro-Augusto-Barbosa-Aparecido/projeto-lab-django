from django.db import models

# Create your models here.


class BaseModel(models.Model):
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
