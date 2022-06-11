from django import template

register = template.Library()

@register.filter
def get_class(item):
    class_name = ""
    if item.done:
        class_name = "done"
    return class_name


@register.filter
def get_acceptance(item):
    accepted = "no"
    if item.accepted:
        accepted = "yes"
    return accepted
    