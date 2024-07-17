
from django.shortcuts import redirect

def customer_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not hasattr(request.user, 'customer'):
            return redirect('customer_login_url')  # Redirect to customer login page
        return view_func(request, *args, **kwargs)
    return wrapped_view