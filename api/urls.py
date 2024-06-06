from django.urls import path

from .views import (EarningSchemeApiView, ExpensesApiView, NeuronetApiView,
                    UsersApiView)

app_name = 'api'

urlpatterns = [
    path('users', UsersApiView.as_view(), name='api_users'),
    path('neuronet', NeuronetApiView.as_view(), name='api_neuronet'),
    path('epxenses', ExpensesApiView.as_view(), name='epxenses'),
    path(
        'earning_scheme', EarningSchemeApiView.as_view(),
        name='earning_scheme',
        ),
]
