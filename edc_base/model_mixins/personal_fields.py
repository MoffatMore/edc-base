from django.core.validators import RegexValidator
from django.db import models
from django_crypto_fields.fields import (
    FirstnameField, LastnameField, EncryptedCharField)
from django_crypto_fields.models import CryptoMixin
from edc_base.model_fields import IsDateEstimatedField
from ..choices import GENDER, TITLE


class PersonalFieldsMixin(CryptoMixin, models.Model):

    title = models.CharField(
        verbose_name="Title",
        choices=TITLE,
        max_length=5,
        null=True,
        blank=False)

    first_name = FirstnameField(
        null=True, blank=False)

    last_name = LastnameField(
        verbose_name="Last name",
        null=True, blank=False)

    initials = EncryptedCharField(
        validators=[RegexValidator(
            regex=r'^[A-Z]{2,3}$',
            message=('Ensure initials consist of letters '
                     'only in upper case, no spaces.'))],
        null=True, blank=False)

    dob = models.DateField(
        verbose_name="Date of birth",
        null=True,
        blank=False)

    is_dob_estimated = IsDateEstimatedField(
        verbose_name="Is date of birth estimated?",
        null=True,
        blank=False)

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER,
        max_length=6,
        null=True,
        blank=False)

    class Meta:
        abstract = True
