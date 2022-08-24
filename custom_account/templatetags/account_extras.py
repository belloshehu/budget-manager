from django import template

register = template.Library()

@register.filter
def set_active(context_object):
    pass


@register.filter
def get_route(path):
    route = path.split('/')[-2]
    return route    
    

