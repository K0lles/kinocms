from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseForbidden


def login_admin_required(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())

        if not request.user.is_superuser:
            return HttpResponseForbidden()

        return function(request, *args, **kwargs)

    wrapper.__doc__ = function.__doc__
    wrapper.__name__ = function.__name__
    return wrapper
