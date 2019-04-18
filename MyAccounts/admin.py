from django.contrib import admin
from AuthByInheritence import settings
from MyAccounts.models import User
# Register your models here.

admin.site.register(User)