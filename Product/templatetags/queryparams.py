from django import template
from django.utils.http import urlencode

register = template.Library()


@register.simple_tag(takes_context=True)
def add_get_param(context, **kwargs):
    "Used to add/replace query parameters to the current URL."
    params = context["request"].GET.dict()
    params.update(kwargs)
    return "?{}".format(urlencode(params))


@register.simple_tag(takes_context=True)
def remove_get_param(context, *args):
    "Used to remove query parameters from the current URL."
    params = context["request"].GET.dict()
    for key in args:
        params.pop(key, None)
    return "?{}".format(urlencode(params))