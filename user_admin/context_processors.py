from django.db.models import Sum
from users.models import UserWallet  # Import UserWallet from the user app
from app.models import Notification


def total_balance_admin(request):
    """Returns the total balance of all users for the admin panel"""
    total = UserWallet.objects.aggregate(Sum("balance"))["balance__sum"] or 0
    return {"total_balance_admin": total}


def unread_notification_count(request):
    """
    Returns the number of unread Notification objects
    for the currently logged-in user.
    """
    if request.user.is_authenticated:
        count = Notification.objects.filter(user=request.user, read=False).count()
    else:
        count = 0
    return {"notification_count": count}