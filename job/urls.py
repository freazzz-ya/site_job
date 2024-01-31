from django.urls import path

from job import views

app_name = 'job'

urlpatterns = [
    path('', views.job_view, name='job_view'),
    path('neuronet/', views.neiro_view, name='neiro_view'),
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
]
