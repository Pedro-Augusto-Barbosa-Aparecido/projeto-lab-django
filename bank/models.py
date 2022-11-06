from django.db import models
from bases.models import BaseModel
from users.models import User


class Account(BaseModel):
    number = models.IntegerField(auto_created=True, unique=True)
    balance = models.DecimalField(default=0.0, decimal_places=2, max_digits=10000)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Account {self.number} of {self.user.name}"


class KeyPix(BaseModel):
    EMAIL_KEY = "email"
    RANDOM_KEY = "random"
    PHONE_KEY = "phone"
    CPF_KEY = "cpf"
    CNPJ_KEY = "cnpj"

    TYPE_KEY_CHOICES = (
        (EMAIL_KEY, "E-mail key"),
        (RANDOM_KEY, "Random key"),
        (PHONE_KEY, "Phone Number key"),
        (CPF_KEY, "CPF key"),
        (CNPJ_KEY, "CNPJ key"),
    )

    key = models.CharField(max_length=255, null=False, blank=False)
    type_key = models.CharField(max_length=16, choices=TYPE_KEY_CHOICES, null=False, blank=False)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return f"Pix | type='{self.type_key}' | by {self.account.user.name}"

    def __repr__(self):
        return f"<Pix of {self.account.number}>"


class Agency(BaseModel):
    number = models.IntegerField(auto_created=True, unique=True)
    accounts = models.ManyToManyField(Account, blank=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f"Agência {self.number}"
