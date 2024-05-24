from django.urls import path

from job import views

app_name = 'job'

urlpatterns = [
    path('', views.job_view, name='job_view'),
    path('neuronet/', views.neiro_view, name='neiro_view'),
    path('scheme/', views.earning_scheme, name='scheme_view'),
    path('finance/', views.finance_view, name='finance_view'),
    path('finance/add_work/', views.finance_add_work, name='finance_add_view'),
    path(
        'finance/add_other_work/', views.finance_other_add,
        name='finance_other_add_view'
        ),
    path(
        'finance/list/', views.finance_list,
        name='finance_list_view'
        ),
    path(
        'finance/special/', views.special,
        name='special_view',
    ),
    path('crypto/', views.CryptoListView.as_view(), name='crypto'),
    path('finance/calculation/', views.finance_calculation_view,
         name='finance_calculation'),
    path(
        'finance/list/expenses', views.finance_list_expenses,
        name='finance_list_expenses_view'
        ),
    path(
        'worker/edit/', views.ProfileUpdateView.as_view(),
        name='profile_edit'
        ),
]
