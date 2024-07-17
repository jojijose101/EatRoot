
from functools import wraps
from django.shortcuts import redirect
from authenticate_users.models import User

def customer_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            return redirect('auth_app:signin')  # Redirect to the sign-in page if not authenticated

        # Check if the user's role is "customer"
        if request.user.role.lower() != "customer":
            return redirect('auth_app:signin')  # Redirect to the sign-in page if the user is not a customer

        return view_func(request, *args, **kwargs)
    
    return wrapped_view



def hotel_user_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            return redirect('auth_app:h_signin')  # Redirect to the sign-in page if not authenticated

        # Check if the user's role is "customer"
        if request.user.role.lower() != "hotel":
            return redirect('auth_app:h_signin')  # Redirect to the sign-in page if the user is not a customer

        return view_func(request, *args, **kwargs)
    
    return wrapped_view

def delivery_user_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            return redirect('auth_app:d_signin')  # Redirect to the sign-in page if not authenticated

        # Check if the user's role is "customer"
        if request.user.role.lower() != "delivery":
            return redirect('auth_app:d_signin')  # Redirect to the sign-in page if the user is not a customer

        return view_func(request, *args, **kwargs)
    
    return wrapped_view