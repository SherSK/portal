from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'data$',views.data,name='currData'),
    ]
