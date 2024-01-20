from django.db import models
from django.contrib.auth.models import User


class UsersCode(models.Model):

    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name='user_code',
    )

    code = models.CharField(
        max_length=9,
        default=None,
        blank=True
    )

    class Meta:
        verbose_name = "User's code"
        verbose_name_plural = "Users' codes"
