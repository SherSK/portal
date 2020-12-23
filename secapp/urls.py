from django.urls import path,include
from django.conf.urls import url
from . import views
from django.contrib import admin



urlpatterns = [
    url(r'^$',views.index,name='secindex')
    ]
