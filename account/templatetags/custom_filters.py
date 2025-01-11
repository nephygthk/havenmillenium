# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def split(value, separator=","):
    """Splits the string by the given separator."""
    return value.split(separator)
