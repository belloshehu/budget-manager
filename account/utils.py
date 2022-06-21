from friendship.models import Friendship, FriendshipRequest
from item.models import Item 


def get_dashboard_contents(request):
    friendships = None
    friendship_requests = None
    items = Item.objects.all()
    if request.user.is_authenticated:
        # friendship_requests = Friendship.objects.all().filter(status__iexact='PN')
        friendship_requests = FriendshipRequest.objects.filter(friendship__user=request.user)
        friendships = Friendship.objects.filter(user__id=request.user.id, status__iexact='AC')
    return {
        "items": items, 
        "friendships": friendships, 
        "friendship_requests": friendship_requests,
    }

    
