from django.contrib import admin
from .models import *
from django.contrib.admin import site
from django.conf import settings


admin.site.site_header=settings.ADMIN_SITE_HEADER
admin.site.index_title='Администрирование'
admin.site.side_title='Test'

admin.site.register(Category)
admin.site.register(Product)
