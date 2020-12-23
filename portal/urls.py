"""portal URL Configuration"""

from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainapp.urls')),
    url(r'^mainapp/',include('mainapp.urls')),
    url(r'^secapp/',include('secapp.urls'))
]
