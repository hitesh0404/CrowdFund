from django.contrib import admin
from .models import Motive

@admin.register(Motive)
class MotiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'motive_type', 'created_at')
    list_filter = ('motive_type',) 
    search_fields = ('name',) 
 


# admin.site.register(Motive, MotiveAdmin)