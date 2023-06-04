from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'expiry_date_time', 'status')

    def status(self, obj):
        return obj.status()
    status.short_description = 'Status'
