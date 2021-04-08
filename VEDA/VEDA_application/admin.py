from django.contrib import admin
from . import models

# Importing models to admin-panel
admin.site.register(models.Parent)
admin.site.register(models.Client)
admin.site.register(models.Group)
admin.site.register(models.Notification)
admin.site.register(models.Task)
admin.site.register(models.Group_post)
admin.site.register(models.Admin_post)
