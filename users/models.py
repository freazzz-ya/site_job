from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from max_site.constants import UserModelConstant


class Worker(AbstractUser):
    """Кастомный юзер"""
    class Role(models.TextChoices):
        Admin = 'Admin', 'Admin role',
        special = 'Special', 'Special role'
        custom = 'Custom', 'Custom role'
        superuser = 'SuperUser', 'SuperUser role',

    email = models.EmailField(
        unique=True,
        verbose_name=_('email address'),
        error_messages={
            "unique": _('A user with that email already exists.'),
        },
    )
    telegram_id = models.PositiveBigIntegerField(
        blank=True,
        null=True,
        unique=True,
        verbose_name=_('telegram id'),
        error_messages={
            "unique": _('A user with that telegram id already exists.'),
        },
    )
    description_for_profil = models.TextField(
        verbose_name=_('description'),
        max_length=UserModelConstant.TEXT_FIELD_MAX_LEN,
        default=UserModelConstant.DEFAULT_TEXT_FOR_DESCRIPTION,
    )
    image = models.ImageField(
        upload_to='images/',
        verbose_name=_('image'),
        default='images/nou.jpg',
    )
    role = models.CharField(
        max_length=UserModelConstant.CHAR_FIELD_MAX_LEN,
        choices=Role.choices,
        default=Role.custom,
    )

    class Meta:
        verbose_name = _('worker')
        verbose_name_plural = _('workers')


class Special(models.Model):
    class We(models.TextChoices):
        Karina = 'Карина', 'КАРИНА'
        Max = 'Максим', 'МАКСИМ'
        we = 'Мы', 'МЫ'
    user = models.CharField(
        max_length=UserModelConstant.CHAR_FIELD_MAX_LEN,
        choices=We.choices,
        verbose_name=_('Имя пользователя')
    )
    text = models.TextField(
        max_length=UserModelConstant.CHAR_FIELD_MAX_LEN,
        verbose_name=_('Договоренность'),
        default=UserModelConstant.DEFAULT_TEXT_FOR_DESCRIPTION,
    )
    date_joined = models.DateTimeField(
        _("date joined"), default=timezone.now
    )

    class Meta:
        verbose_name = _('Специальная модель')
        verbose_name_plural = _('Специальные модели')
        db_table = 'Special'

    def __str__(self):
        return 'Договоренности'
