from .models import DelUser


def links(request):
    try:
       user_link = DelUser.objects.get(user=request.user)
    except:
        user_link = None
    return dict(user_link=user_link)
