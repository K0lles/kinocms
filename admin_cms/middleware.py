from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseForbidden


class LoginRequiredAccess:
    """All urls starting with the given prefix require the user to be logged in"""

    APP_NAME = 'admin_cms'

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not hasattr(request, 'user'):
            raise ImproperlyConfigured(
                "Requires the django's authentication middleware"
                " to be installed.")

        user = request.user
        if self.APP_NAME in request.path:  # match app_name defined in myapp.urls.py
            if not user.is_authenticated:
                path = request.get_full_path()
                return redirect_to_login(path)

            if not request.user.is_superuser:
                return HttpResponseForbidden()

        return self.get_response(request)
