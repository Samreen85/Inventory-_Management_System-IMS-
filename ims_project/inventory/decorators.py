# myapp/decorators.py

from django.contrib import messages
from django.shortcuts import redirect

# Ensure that the user is an admin
def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            # Add a message when a non-admin tries to access a restricted view
            messages.error(request, 'Only admin can perform this operation.')
            return redirect('product_list')  # Redirect to product list or any other page
        return view_func(request, *args, **kwargs)
    return _wrapped_view
