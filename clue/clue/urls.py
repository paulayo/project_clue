
from django.contrib import admin
from django.urls import path, include
#third_parties
from oscar.app import application
#inner modules
from django.conf import settings


# if settings.DEBUG:
#     import django_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('__debug__/', include(debug_toolbar.urls)),
    # url(r'^search/', include('haystack.urls')),


]
