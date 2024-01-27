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
