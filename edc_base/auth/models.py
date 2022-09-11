from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import PROTECT


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=PROTECT)

    site = models.CharField(
        max_length=100,
        blank=True,
        null=True)

    occupation = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='user\'s occupation')

    department = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='user\'s organisation department')
