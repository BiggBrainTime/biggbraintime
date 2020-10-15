from django import template

register = template.Library()

@register.filter
def forlooptag(value):
    return range(value)