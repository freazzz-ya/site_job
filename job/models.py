from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

from users.models import Worker
from max_site.constants import (
    DjobModelsConstant, UserModelConstant, NeuralNetworkModelConstant
    )


class Neural_network(models.Model):
    """Модель нейросети."""
    title = models.CharField(
        max_length=NeuralNetworkModelConstant.CHAR_FIELD_MAX_LEN,
        verbose_name=_('Название'),
        help_text=_('Max 256'),
        unique=True,
    )
    image = models.ImageField(
        upload_to='images/network/',
        verbose_name=_('Изображение'),
        default='images/network/default.jpg',
    )
    description = models.TextField(
        max_length=NeuralNetworkModelConstant.CHAR_FIELD_MAX_LEN,
        verbose_name=_('Описание'),
        default='Обычное описание для нейросети',
    )
    url = models.URLField(
        verbose_name=_('Url адрес'),
        max_length=NeuralNetworkModelConstant.CHAR_FIELD_MAX_LEN,
    )
    date_joined = models.DateTimeField(
        verbose_name=_("Дата создания"),
        auto_now_add=True,
    )

    class Meta:
        ordering = ('date_joined',)
        verbose_name = _('neural network')
        verbose_name_plural = _('neural networks')

    def __str__(self):
        return f'Neural network {self.title}'


class Job(models.Model):
    """Модель работы"""
    class Busyness(models.TextChoices):
        main = 'Main', 'Main job'
        part_time = 'Part-time', 'Part-time job'

    class Duration(models.TextChoices):
        day = 'Day', 'working time duration - day'
        month = 'Month', 'working time duration - month'

    title = models.CharField(
        max_length=DjobModelsConstant.CHAR_FIELD_MAX_LEN,
        verbose_name=_('Название работы'),
        unique=True,
    )
    duration = models.CharField(
        max_length=DjobModelsConstant.CHAR_FIELD_MAX_LEN,
        verbose_name=_('Оплата за определенный период'),
        choices=Duration.choices,
        default=Duration.day,
    )
    busyness = models.CharField(
        max_length=DjobModelsConstant.CHAR_FIELD_MAX_LEN,
        verbose_name=_('Занятость'),
        choices=Busyness.choices,
        default=Busyness.part_time,
    )
    payment = models.IntegerField(
        verbose_name=_('Оплата'),
        validators=[
            MinValueValidator(
                limit_value=DjobModelsConstant.INT_FIELD_MIN_VALUE,
                message=f'Не может быть меньше '
                        f'{DjobModelsConstant.INT_FIELD_MIN_VALUE}'),
            MaxValueValidator(
                limit_value=DjobModelsConstant.INT_FIELD_MAX_VALUE,
                message=f'Не может быть больше '
                        f'{DjobModelsConstant.INT_FIELD_MAX_VALUE}',
                    )
        ],
    )

    class Meta:
        verbose_name = _('Работа')
        verbose_name_plural = _('Работы')
        ordering = ('id',)

    def __str__(self):
        return f'{self.title}'


class Balance(models.Model):
    """Модель баланса"""
    worker = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE,
        related_name='worker_balance',
        verbose_name=_('Работник'),
    )
    amount_balance = models.DecimalField(
        max_digits=UserModelConstant.BALANCE_MAX_DIGITS,
        decimal_places=UserModelConstant.BALANCE_DECIMAL_PLACES,
        verbose_name=_('balance money'),
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_('last_updated',)
    )

    class Meta:
        ordering = ('id',)
        verbose_name = _('balance',)
        verbose_name_plural = _('balances',)

    def __str__(self) -> str:
        return f'{self.amount_balance} {self.last_updated}'


# class Payment(models.Model):
#     """Модель оплаты"""
#     worker = models.ForeignKey(
#         to=Worker,
#         on_delete=models.CASCADE,
#         related_name='payment',
#         verbose_name=_('Работник'),
#     )
#     neural_network = models.ManyToManyField(
#         to=Neural_network, through='Payment_network',
#         related_name='payments',
#         verbose_name=_('Нейросеть'),
#     )
#     job = models.ManyToManyField(
#         to=Job,
#         related_name='payments',
#         verbose_name=_('Работа'),
#     )
#     balance = models.ManyToManyField(
#         to=Balance,
#         related_name='payments',
#         verbose_name=_('Баланс'),
#     )
#     last_updated = models.DateTimeField(
#         auto_now=True,
#         verbose_name=_('last_updated',)
#     )

#     class Meta:
#         ordering = ('id',)
#         verbose_name = _('Оплата')
#         verbose_name_plural = _('Оплаты')

#     def __str__(self) -> str:
#         return f'Оплата {self.worker}'


# class Payment_network(models.Model):
#     payment = models.ForeignKey(
#         to=Payment,
#         related_name='payment_networks',
#         verbose_name=_('Оплата'),
#         on_delete=models.CASCADE,
#     )
#     network = models.ForeignKey(
#         to=Neural_network,
#         related_name='payment_networks',
#         verbose_name=_('Нейросеть'),
#         on_delete=models.CASCADE,
#     )
#     payment_in_money = models.IntegerField(
#         verbose_name=_('Оплата'),
#         validators=[
#             MinValueValidator(
#                 limit_value=DjobModelsConstant.INT_FIELD_MIN_VALUE,
#                 message=f'Не может быть меньше '
#                         f'{DjobModelsConstant.INT_FIELD_MIN_VALUE}'),
#             MaxValueValidator(
#                 limit_value=DjobModelsConstant.INT_FIELD_MAX_VALUE,
#                 message=f'Не может быть больше '
#                         f'{DjobModelsConstant.INT_FIELD_MAX_VALUE}',
#                     )
#         ],
#     )

#     class Meta:
#         ordering = ('id',)
#         verbose_name = _('Нейросеть в оплате')
#         verbose_name_plural = _('Нейросети в оплате')

#     def __str__(self):
#         return f'{self.payment} {self.network}'


class Job_Payment(models.Model):
    job = models.ManyToManyField(
        to=Job,
        related_name='payments',
        verbose_name=_('Работа'),
    )
    payment_in_money = models.IntegerField(
        verbose_name=_('Оплата'),
        validators=[
            MinValueValidator(
                limit_value=DjobModelsConstant.INT_FIELD_MIN_VALUE,
                message=f'Не может быть меньше '
                        f'{DjobModelsConstant.INT_FIELD_MIN_VALUE}'),
            MaxValueValidator(
                limit_value=DjobModelsConstant.INT_FIELD_MAX_VALUE,
                message=f'Не может быть больше '
                        f'{DjobModelsConstant.INT_FIELD_MAX_VALUE}',
                    )
        ],
    )