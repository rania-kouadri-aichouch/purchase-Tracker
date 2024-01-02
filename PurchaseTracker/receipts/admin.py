from django.contrib import admin
from .models import Receipt

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'store_name', 'date_of_purchase', 'total_amount']
    search_fields = ['user__username', 'store_name']  
    list_filter = ['date_of_purchase'] 
