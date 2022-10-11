
from django.db import models
from edc_base.model_fields import CellPhoneField
from ..choices import PREFERRED_CONTACT, PREFERRED_INVOICE


class ContactMixin(models.Model):

    physical_address = models.CharField(
        verbose_name='Physical address',
        max_length=100,
    )

    postal_address = models.CharField(
        verbose_name='Postal address',
        max_length=100,
    )

    cell = CellPhoneField()

    email = models.EmailField(
        verbose_name='Email',

    )

    preferred_email = models.CharField(
        verbose_name='Preferred email',
        max_length=100,
        blank=True,
        null=True
    )

    preferred_contact = models.CharField(
        verbose_name='Preferred method of contact',
        max_length=100,
        null=True,
        choices=PREFERRED_CONTACT,
    )

    preferred_invoice = models.CharField(
        verbose_name='Preferred method of receiving invoice',
        max_length=100,
        null=True,
        choices=PREFERRED_INVOICE,
    )

    class Meta:
        abstract = True
