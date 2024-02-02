from django.db import models
from django.core.validators import (
    MinValueValidator, MaxValueValidator,
    )
from django.utils.translation import gettext_lazy as _

from users.models import Worker
from max_site.constants import (
    DjobModelsConstant, UserModelConstant, NeuralNetworkModelConstant,
    )


class Neural_network(models.Model):
    """Модель нейросети."""
    title = models.CharField(
        max_length=NeuralNetworkModelConstant.CHAR_FIELD_MAX_LEN,
        verbose_name=_('Название'),
        help_text=_('Max 256'),
        unique=True,
        error_messages={
            'unique': 'Название уже существует такое',
        }
    )
    image = models.ImageField(
        upload_to='images/network/',
        verbose_name=_('Изображение'),
        default='images/network/default_Uf.jpg',
    )
    description = models.TextField(
        max_length=NeuralNetworkModelConstant.TEXT_FIELD_MAX_LEN,
        verbose_name=_('Описание'),
        default=DjobModelsConstant.DEFAULT_TEXT_FOR_DESCRIPTION,
        help_text='Максимальная длинна - 1000 символов',
    )
    url = models.URLField(
        verbose_name=_('Url адрес'),
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


class Job(models.Model):
    """Модель работы"""
    title = models.CharField(
        max_length=DjobModelsConstant.CHAR_FIELD_MAX_LEN,
        verbose_name='Работа',
        unique=True,
    )
    discription = models.TextField(
        max_length=DjobModelsConstant.TEXT_FIELD_MAX_LEN,
        default=DjobModelsConstant.DEFAULT_TEXT_FOR_DESCRIPTION,
        verbose_name=_('Описание')
    )

    class Meta:
        verbose_name = _('Основная мод работы')
        verbose_name_plural = _('Основные мод работы')
        db_table = 'Job'
        ordering = ('id',)

    def __str__(self):
        return f'Работа {self.title}'


class Other_Source_model(models.Model):
    """Модель других источников"""
    title = models.CharField(
        max_length=DjobModelsConstant.CHAR_FIELD_MAX_LEN,
        verbose_name='Подработка',
        unique=True,
    )
    discription = models.TextField(
        max_length=DjobModelsConstant.TEXT_FIELD_MAX_LEN,
        default=DjobModelsConstant.DEFAULT_TEXT_FOR_DESCRIPTION,
        verbose_name=_('Описание')
    )

    class Meta:
        verbose_name = _('Другой ист дохода')
        verbose_name_plural = _('Другие ист дохода')
        db_table = 'Other_Source'
        ordering = ('id',)

    def __str__(self):
        return f'{self.title}'


class Job_Payment(models.Model):
    class Busyness(models.TextChoices):
        main = 'Основная', 'Основная работа'
        part_time = 'Подработка', 'Частичная занятость'

    worker = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE,
        related_name='job',
        verbose_name='Работник',
    )
    job = models.ForeignKey(
        to=Job,
        on_delete=models.CASCADE,
        verbose_name=_('работы'),
        related_name='jobs',
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
        default=0,
    )
    duration = models.IntegerField(
        verbose_name=_('сумма дней'),
        validators=[
            MinValueValidator(
                limit_value=DjobModelsConstant.INT_FIELD_MIN_VALUE_DURATION,
                message=f'Не может быть меньше '
                        f'{DjobModelsConstant.INT_FIELD_MIN_VALUE_DURATION}'),
            MaxValueValidator(
                limit_value=DjobModelsConstant.INT_FIELD_DAY_MAX_VALUE,
                message=f'Не может быть больше '
                        f'{DjobModelsConstant.INT_FIELD_MAX_VALUE}',
                    )
        ],
        default=0,
    )
    busyness = models.CharField(
        max_length=DjobModelsConstant.CHAR_FIELD_MAX_LEN,
        verbose_name=_('Занятость'),
        choices=Busyness.choices,
        default=Busyness.part_time,
    )
    total_amount = models.IntegerField(
        verbose_name=_('Общая сумма'),
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
        default=0,
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Последнее обновление',)
    )
    comment = models.TextField(
        max_length=DjobModelsConstant.TEXT_FIELD_MAX_LEN,
        default=UserModelConstant.DEFAULT_TEXT_FOR_COMMENT,
        verbose_name=_('Комментарий')
    )

    class Meta:
        db_table = 'job_payment'
        ordering = ('id',)
        verbose_name = _('Работа',)
        verbose_name_plural = _('Работы',)

    def __str__(self) -> str:
        return f'{self.job} {self.worker}'


class Network_Payment(models.Model):
    class Busyness(models.TextChoices):
        main = 'Основная', 'Основная работа'
        part_time = 'Подработка', 'Частичная занятость'

    worker = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE,
        related_name='network',
        verbose_name='Работник',
    )
    network = models.ForeignKey(
        to=Neural_network,
        on_delete=models.CASCADE,
        verbose_name=_('нейросети'),
        related_name='networks',
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
        default=0,
    )
    duration = models.IntegerField(
        verbose_name=_('сумма дней'),
        validators=[
            MinValueValidator(
                limit_value=DjobModelsConstant.INT_FIELD_MIN_VALUE_DURATION,
                message=f'Не может быть меньше '
                        f'{DjobModelsConstant.INT_FIELD_MIN_VALUE_DURATION}'),
            MaxValueValidator(
                limit_value=DjobModelsConstant.INT_FIELD_DAY_MAX_VALUE,
                message=f'Не может быть больше '
                        f'{DjobModelsConstant.INT_FIELD_MAX_VALUE}',
                    )
        ],
        default=0,
    )
    comment = models.TextField(
        max_length=DjobModelsConstant.TEXT_FIELD_MAX_LEN,
        default=UserModelConstant.DEFAULT_TEXT_FOR_COMMENT,
        verbose_name=_('Комментарий')
    )
    busyness = models.CharField(
        max_length=DjobModelsConstant.CHAR_FIELD_MAX_LEN,
        verbose_name=_('Занятость'),
        choices=Busyness.choices,
        default=Busyness.part_time,
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Последнее обновление',)
    )

    class Meta:
        ordering = ('id',)
        verbose_name = _('Нейросеть оплаты',)
        verbose_name_plural = _('Нейросети оплаты',)

    def __str__(self) -> str:
        return f'{self.network} {self.worker}'


class Other_Source(models.Model):
    class Busyness(models.TextChoices):
        main = 'Основная', 'Основная работа'
        part_time = 'Подработка', 'Частичная занятость'

    worker = models.ForeignKey(
        to=Worker,
        on_delete=models.CASCADE,
        related_name='other_sources',
        verbose_name='Работник',
    )
    other_source = models.ForeignKey(
        to=Other_Source_model,
        on_delete=models.CASCADE,
        verbose_name=_('другие источники'),
        related_name='other_sources',
    )
    payment_in_money = models.IntegerField(
        verbose_name=_('Оплата'),
        validators=[
            MinValueValidator(
                limit_value=DjobModelsConstant.INT_FIELD_MIN_VALUE_DURATION,
                message=f'Не может быть меньше '
                        f'{DjobModelsConstant.INT_FIELD_MIN_VALUE_DURATION}'),
            MaxValueValidator(
                limit_value=DjobModelsConstant.INT_FIELD_MAX_VALUE,
                message=f'Не может быть больше '
                        f'{DjobModelsConstant.INT_FIELD_MAX_VALUE}',
                    )
        ],
        default=0,
    )
    duration = models.IntegerField(
        verbose_name=_('сумма дней'),
        validators=[
            MinValueValidator(
                limit_value=DjobModelsConstant.INT_FIELD_MIN_VALUE,
                message=f'Не может быть меньше '
                        f'{DjobModelsConstant.INT_FIELD_MIN_VALUE}'),
            MaxValueValidator(
                limit_value=DjobModelsConstant.INT_FIELD_DAY_MAX_VALUE,
                message=f'Не может быть больше '
                        f'{DjobModelsConstant.INT_FIELD_MAX_VALUE}',
                    )
        ],
        default=0,
    )
    comment = models.TextField(
        max_length=DjobModelsConstant.TEXT_FIELD_MAX_LEN,
        default=UserModelConstant.DEFAULT_TEXT_FOR_COMMENT,
        verbose_name=_('Комментарий')
    )
    busyness = models.CharField(
        max_length=DjobModelsConstant.CHAR_FIELD_MAX_LEN,
        verbose_name=_('Занятость'),
        choices=Busyness.choices,
        default=Busyness.part_time,
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Последнее обновление',)
    )

    class Meta:
        ordering = ('id',)
        verbose_name = _('Другой источник оплаты',)
        verbose_name_plural = _('Другие источники оплаты',)

    def __str__(self) -> str:
        return f'{self.other_source} {self.worker}'
