from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from job.models import Job, Balance
from max_site.constants import UserModelConstant


class Worker(AbstractUser):
    job = models.ManyToManyField(
        to=Job,
        related_name='job',
    )
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
    balance = models.ForeignKey(
        to=Balance,
        related_name='balance',
        on_delete=models.CASCADE,
        verbose_name=_('balance'),
    )
