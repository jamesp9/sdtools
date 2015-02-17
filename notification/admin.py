from django.contrib import admin

from . import models

admin.site.register(models.Email)
admin.site.register(models.Client)
admin.site.register(models.NotificationType)
admin.site.register(models.Notification)
admin.site.register(models.Update)
