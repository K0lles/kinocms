from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseForbidden


def login_admin_required(function):
    def wrapper(request, *args, **kwargs):
        # decorated_view_func = login_required(request)
        # if not decorated_view_func.user.is_authenticated:
        #     return decorated_view_func(request)  # return redirect to signin
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())

        if not request.user.is_superuser:  # if not coach redirect to home page
            # return HttpResponseRedirect(reverse('home', args=(), kwargs={}))
            return HttpResponseForbidden()

        return function(request, *args, **kwargs)

    wrapper.__doc__ = function.__doc__
    wrapper.__name__ = function.__name__
    return wrapper
