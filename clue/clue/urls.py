
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
#third_parties
from oscar.app import application
#inner modules
from django.conf import settings


if settings.DEBUG:
    import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    # url(r'^search/', include('haystack.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
