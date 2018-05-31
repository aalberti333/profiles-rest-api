from django.contrib import admin
from . import models

#Register our created models with the Django admin
admin.site.register(models.UserProfile)
