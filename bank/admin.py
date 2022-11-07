from django.contrib import admin
from .models import *


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(KeyPix)
class KeyPixAdmin(admin.ModelAdmin):
    pass


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    pass
