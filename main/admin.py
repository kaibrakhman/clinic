from django.contrib import admin
from . import models

admin.site.register(models.Branch)
admin.site.register(models.Days)
admin.site.register(models.Times)
admin.site.register(models.Doctor)
admin.site.register(models.Statement)