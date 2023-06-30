from django.contrib import admin
from .models import *

admin.site.register(Kitob)

# class BuyAdmin(admin.ModelAdmin):
#     list_display = ('kitob', 'name', 'phone', 'yetkazish', 'hudud')
    # list_filter = ('site',)
    # search_fields = ('kitob__name')


admin.site.register(Buy)
