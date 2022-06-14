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
    
@register.filter
def share_length(share_set):
    """
    Number of times an item is shared equals the 
    total target users in the share instances.
    """
    length = [ share.target_users.count() for share in share_set.all()]
    return sum(length)