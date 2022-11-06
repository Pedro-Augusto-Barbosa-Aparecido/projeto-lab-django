from django.db import models

# Create your models here.


class BaseModel(models.Model):
    active = models.BooleanField(default=False)

    class Meta:
        abstract = True
