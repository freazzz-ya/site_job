from django.contrib import admin

from .models import (
    Job, Neural_network, Balance, Job_Payment

    )

admin.site.register(Job)
admin.site.register(Neural_network)
admin.site.register(Balance)
admin.site.register(Job_Payment)
