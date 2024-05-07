from django.contrib import admin

from .models import (Balance, Job, Job_Payment, Network_Payment,
                     Neural_network, Other_Source, Other_Source_model,
                     Crypto_model,)

admin.site.register(Network_Payment)
admin.site.register(Neural_network)
admin.site.register(Balance)
admin.site.register(Job_Payment)
admin.site.register(Other_Source)
admin.site.register(Job)
admin.site.register(Other_Source_model)
admin.site.register(Crypto_model)