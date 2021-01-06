from django.contrib import admin

from .models import Bills


class BillsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'count', 'state')


admin.site.register(Bills, BillsAdmin)
