from friendship.models import Friendship
from item.models import Item 


def get_dashboard_contents(request):
    items = Item.objects.all()[:10]
    friendships = None
    friendship_requests = None
    if request.user.is_authenticated:
        friendship_requests = Friendship.objects.all().filter(status__iexact='PN')
        friendships = Friendship.objects.filter(user__id=request.user.id, status__iexact='AC')
    print(friendships, friendship_requests)
    return {"items": items, "friendships": friendships, "requests": friendship_requests}

    
