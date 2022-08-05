from friendship.models import Friendship, FriendshipRequest
from item.models import Item 
from budget.models import Budget


def get_dashboard_contents(request):
    friendships = None
    friendship_requests = None
    items = Item.objects.all()
    if request.user.is_authenticated:
        # friendship_requests = Friendship.objects.all().filter(status__iexact='PN')
        sent_friendship_requests = FriendshipRequest.objects.filter(friendship__user=request.user)
        received_friendship_requests = FriendshipRequest.objects.filter(friendship__friend=request.user)
        friendships = Friendship.objects.filter(user__id=request.user.id, status__iexact='AC')
        budgets = Budget.objects.filter(owner__id=request.user.id)
    return {
        "items": items, 
        "friendships": friendships, 
        "sent_friendship_requests": sent_friendship_requests,
        "received_friendship_requests": received_friendship_requests,
        "budgets": budgets
    }

    
