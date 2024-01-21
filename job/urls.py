from django.urls import path

from job import views

app_name = 'job'

urlpatterns = [
    path('', views.job_view, name='job_view'),
    path('neuronet/', views.neiro_view),
    path('finance/', views.finance_view, name='finance_view'),
]
