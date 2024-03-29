import base64

from django.core.files.base import ContentFile
from PIL import Image
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from max_site.constants import UserModelConstant
from users.models import Worker, Special
from job.models import (
    Neural_network, Job_Payment, Job,
    Network_Payment, Other_Source, Other_Source_model,
    Earning_scheme, Maling_model, Сontacts_model,
    )


class Base64ImageField(forms.ImageField):
    """
    Сериализатор для обработки изображений, представленных в кодировке
    base64, которые могут быть отправлены клиентом при создании или обновлении
    объекта.
    """
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        required=True,
        help_text='Это поле обязательное',
        error_messages={
                'required': 'Это поле обязательное'
            },
        )
    email = forms.EmailField(
        required=True,
        label='email',
        error_messages={
            'required': 'Это поле обязательное',
            'unique': 'Такая почта уже существует',
        },
        help_text='Это поле обязательное',
    )
    description_for_profil = forms.CharField(
        label='Описание профиля',
        help_text='Это поле необязательное',
        required=False,
        empty_value=UserModelConstant.DEFAULT_TEXT_FOR_DESCRIPTION,
    )
    image = forms.ImageField(
        label='Фото профиля',
        help_text='Это поле необязательное',
        required=False,
    )
    telegram_id = forms.IntegerField(
        required=False,
        help_text='Это числовое поле и оно необязательное',
    )
    first_name = forms.CharField(
        label='Имя',
        help_text='Это поле необязательное',
        required=False,
    )
    last_name = forms.CharField(
        label='Фамилия',
        help_text='Это поле необязательное',
        required=False,
    )

    class Meta:
        model = Worker
        fields = (
            'username', 'email', 'description_for_profil',
            'image', 'telegram_id', 'first_name', 'last_name',
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Проверяем, загружено ли изображение
        if self.cleaned_data.get('image'):
            img = Image.open(self.cleaned_data['image'])
            img.thumbnail((300, 200))  # Изменяем размер до 300x200
            # Перезаписываем изображение в поле image
            instance.image.save(
                self.cleaned_data['image'].name,
                self.cleaned_data['image'], save=False
            )
        if commit:
            instance.save()
        return instance


class NeuralNetworkForm(forms.ModelForm):
    """Форма для модели нейросеть."""
    title = forms.CharField(
        required=True,
        error_messages={
            'unique': 'должно быть уникальным',
        },
        label='Название',
        help_text='Поле должно быть уникальным',
    )

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


class NetworkForm(forms.ModelForm):
    class Meta:
        model = Network_Payment
        fields = [
            'network', 'payment_in_money',
            'duration', 'busyness', 'comment',
        ]


class Other_Source_Form(forms.ModelForm):
    class Meta:
        model = Other_Source
        fields = [
            'other_source', 'payment_in_money',
            'duration', 'busyness', 'comment',
        ]


class Job_Reg_Form(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


class Other_Source_Reg_Form(forms.ModelForm):
    class Meta:
        model = Other_Source_model
        fields = '__all__'


class JobForm(forms.ModelForm):
    class Meta:
        model = Job_Payment
        fields = [
            'job', 'payment_in_money',
            'duration', 'busyness',
            'comment',
        ]


class SpecialForm(forms.ModelForm):
    class Meta:
        model = Special
        fields = [
            'user', 'text',
        ]


class Earning_schemeForm(forms.ModelForm):
    title = forms.CharField(
        label='Название',
        required=True,
        error_messages={
            'required': 'Это поле должно быть обязательным',
        }
    )
    discription = forms.CharField(
        label='Описание',
        required=False,
        help_text='Максимальная длинна - 10000 символов',
        widget=forms.Textarea(attrs={'class': 'form-control'}),
    )
    url = forms.URLField(
        label='Url площадки для заработка',
        required=True,
        error_messages={
            'required': 'Это поле должно быть обязательным',
        }
    )

    class Meta:
        model = Earning_scheme
        fields = [
            'title', 'network', 'other_source',
            'url', 'discription', 'image',
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Проверяем, загружено ли изображение
        if self.cleaned_data.get('image'):
            img = Image.open(self.cleaned_data['image'])
            img.thumbnail((300, 200))  # Изменяем размер до 300x200
            # Перезаписываем изображение в поле image
            instance.image.save(
                self.cleaned_data['image'].name,
                self.cleaned_data['image'], save=False
            )
        if commit:
            instance.save()
        return instance


class Maling_model_form(forms.ModelForm):
    class Meta:
        model = Maling_model
        fields = [
            'email'
        ]


class Сontacts_model_form(forms.ModelForm):
    class Meta:
        model = Сontacts_model
        fields = '__all__'
