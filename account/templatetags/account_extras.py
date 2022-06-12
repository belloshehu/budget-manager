from django import template

register = template.Library()

@register.filter
def set_active(context_object, ):
    pass