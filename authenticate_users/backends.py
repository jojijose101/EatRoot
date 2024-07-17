from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class RoleBasedBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, role=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
            if user.check_password(password) and (role is None or user.role == role):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None