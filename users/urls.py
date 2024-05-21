from django.urls import include, path, reverse_lazy
from django.views.generic.edit import CreateView

from job.forms import CustomUserCreationForm

app_name = 'users'

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=CustomUserCreationForm,
            success_url=reverse_lazy('job:job_view'),
        ),
        name='registration',
    ),
]
