from django import forms 
from django.contrib.auth.forms import UserCreationForm

from users.models import Worker



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = (
            'username', 'email', 'description_for_profil',
            'image', 'balance', 'telegram_id', 'job',
        )


class ContestForm(forms.Form):
    title = forms.CharField(label='Название', max_length=20)
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea()
    )
    price = forms.IntegerField(
        label='Цена',
        help_text='Рекомендованная розничная цена',
        min_value=10,
        max_value=100,
    )
    comment = forms.CharField(
        label='Комментарий', required=False, help_text='Необязательное поле',
        widget=forms.Textarea()
    )
