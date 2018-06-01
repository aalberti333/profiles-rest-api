from django.contrib import admin
from . import models

#Register our created models with the Django admin
#This admin.py file is what your admin console is allowed to view
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
