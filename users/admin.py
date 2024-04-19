from django.contrib import admin

from .models import Special, Worker

# Register your models here.
admin.site.register(Worker)
admin.site.register(Special)