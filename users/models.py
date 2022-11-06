from django.db import models

# Create your models here.
from bases.models import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False, unique=True)
    password = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return f"User {self.name}"

    def __repr__(self):
        return f"<User {self.name} - {self.email}>"
