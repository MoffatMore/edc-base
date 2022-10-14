from datetime import datetime

from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter("date_from_timestamp")
def date_from_timestamp(value):
    return datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f%z').date()
