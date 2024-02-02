from django.contrib import admin

from .models import (
    Neural_network, Balance, Job_Payment,
    Network_Payment, Other_Source, Job, Other_Source_model
    )

admin.site.register(Network_Payment)
admin.site.register(Neural_network)
admin.site.register(Balance)
admin.site.register(Job_Payment)
admin.site.register(Other_Source)
admin.site.register(Job)
admin.site.register(Other_Source_model)

