from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from decorator_include import decorator_include
from .decorators import login_admin_required
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_cms/', decorator_include(login_admin_required, 'admin_cms.urls')),
    # path('', include('cinema.urls')),
    # path('event/', include('event.urls')),
    # path('page/', include('page.urls')),
    # path('movie/', include('movie.urls')),
    # path('banner/', include('banner.urls')),
    path('user/', include('user.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
