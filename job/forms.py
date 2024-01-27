from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from users.models import Worker
from job.models import Neural_network, Balance, Job_Payment, Job
from max_site.constants import MoneyFormConstant


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = (
            'username', 'email', 'description_for_profil',
            'image', 'telegram_id', 'first_name', 'last_name',
        )


class NeuralNetworkForm(forms.ModelForm):
    """Форма для модели нейросеть."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].empty_label = 'Напишите описание поля'

    class Meta:
        model = Neural_network
        fields = [
            'title', 'description', 'image', 'url'
        ]

    def clean_descripption(self):
        description = self.cleaned_data['description']
        if description[0] != description[0].upper():
            ValidationError('Описание должно начинаться с большой буквы')
        return description

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0] != title[0].upper():
            ValidationError('Описание должно начинаться с большой буквы')
        return title


class JobForm(forms.Form):
    job = forms.CharField(
        max_length=256,
        min_length=1,
        required=True,
        label='работа',
        strip=True,
        initial='Работенка',
        localize=True,
    )
    payment = forms.IntegerField(
        max_value=100000,
        min_value=1,
        required=True,
        label='Оплата',
    )

    class Meta:
        fields = [
            'job', 'payment',
        ]


class NetworkForm(forms.Form):
    neuralnetwork = forms.CharField(
        max_length=256,
        min_length=1,
        label='Нейросеть',
        required=True,
        strip=True,
        initial='Нейро',
        localize=True,
    )
    payment = forms.IntegerField(
        max_value=100000,
        min_value=1,
        required=True,
        label='Оплата',
    )

    class Meta:
        fields = [
            'neuralnetwork', 'payment',
        ]


class Other_Source_Form(forms.Form):
    other_source = forms.CharField(
        max_length=256,
        min_length=1,
        required=True,
        label='Другой источник дохода',
        strip=True,
        initial='иное',
        localize=True,
    )
    payment = forms.IntegerField(
        max_value=100000,
        min_value=1,
        required=True,
        label='Оплата',
    )

    class Meta:
        fields = [
            'other_source', 'payment',
        ]
