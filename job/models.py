from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

from max_site.constants import DjobModelsConstant, UserModelConstant


class Job(models.Model):
    """Модель работы"""
    class Busyness(models.TextChoices):
        main = 'Main', 'Main job'
        part_time = 'Part-time', 'Part-time job'

    class Duration(models.TextChoices):
        day = 'Day', 'working time duration - day'
        month = 'Month', 'working time duration - month'

    name = models.CharField(
        max_length=DjobModelsConstant.CHAR_FIELD_MAX_LEN,
        verbose_name=_('name djob'),
        unique=True,
    )
    busyness = models.CharField(
        max_length=DjobModelsConstant.CHAR_FIELD_MAX_LEN,
        verbose_name=_('busyness'),
        choices=Busyness.choices,
        default=Busyness.part_time,
    )
    payment = models.IntegerField(
        verbose_name=_('payment'),
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
    duration = models.CharField(
        max_length=DjobModelsConstant.CHAR_FIELD_MAX_LEN,
        verbose_name=_('duration'),
        choices=Duration.choices,
        default=Duration.day,
    )

    class Meta:
        ordering = ('name',)
        verbose_name = _('job')
        verbose_name_plural = _('jobs')

    def __str__(self) -> str:
        return f'{self.name}'


class Balance(models.Model):
    """Модель баланса"""
    amount_balance = models.DecimalField(
        max_digits=UserModelConstant.BALANCE_MAX_DIGITS,
        decimal_places=UserModelConstant.BALANCE_DECIMAL_PLACES,
        verbose_name=_('balance money'),
        default=0,
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
