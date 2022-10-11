import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FullNameValidator:

    def __init__(self, regex=None):
        self.regex = regex or re.compile('^[A-Za-z]{1,50}\, [A-Za-z]{1,50}$')  # NOQA

    def __call__(self, value):
        if not re.match(self.regex, value):
            raise ValidationError(
                'Invalid format. Format is \'Lastname, Firstname\'. '
                'All uppercase separated by a comma. Note the space '
                'following the comma.')

    def __eq__(self, other):
        return self.regex == other.regex
