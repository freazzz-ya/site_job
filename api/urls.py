from django.urls import path

from .views import (EarningSchemeApiView, ExpensesApiView, JobApiView,
                    NetworkApiView, NeuronetApiView, OtherSource, UsersApiView)

app_name = 'api'

urlpatterns = [
    path('users', UsersApiView.as_view(), name='api_users'),
    path('neuronet', NeuronetApiView.as_view(), name='api_neuronet'),
    path('epxenses', ExpensesApiView.as_view(), name='epxenses'),
    path(
        'earning_scheme', EarningSchemeApiView.as_view(),
        name='earning_scheme',
        ),
    path('job_payment', JobApiView.as_view(), name='job'),
    path('network_payment', NetworkApiView.as_view(), name='network_payment'),
    path('other_payment', OtherSource.as_view(), name='other_payment')
]
