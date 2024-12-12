from django.contrib import admin

# Register your models here.
from .models import *
# @admindecorator
admin.site.register([Contributor,Address])
