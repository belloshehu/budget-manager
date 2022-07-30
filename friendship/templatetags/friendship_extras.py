from django import template
from django.utils.html import format_html

register = template.Library()

@register.simple_tag(takes_context=True)
def request_status_action_tag(context, friendship):
    """
    Returns simple tag to show friendship request status and actions.

    If requests is outgoing, status and delete action are shown. 
    If request is incoming and pending, 'accept' and 'reject' actions are shown.
    """
    request = context['request']
    accept_url = f"/friendship/accept/{friendship.user.id}/"
    reject_url = '#'
    delete_url = '#'
    
    if friendship.friend == request.user:
        accept_reject_actions = format_html(
            """
            <a href={} class='btn-gray'>
                <i class='fa-solid fa-check'></i> Accept
            </a>
            <a href={} class='btn-gray'>
                <i class='fa-solid fa-arrow-reverse'></i> Reject
            </a>
            """,
            accept_url, 
            reject_url
        )
        return format_html(accept_reject_actions)
    else:
        accept_reject_actions = format_html(
            """
            <small class='primary'>{}</small>
            <a href={} class='btn-gray'>
                <i class="fa-solid fa-trash fa-xl"></i> Delete
            </a>
            """,
            friendship.get_status_display(), 
            delete_url
        )
        return format_html(accept_reject_actions)



