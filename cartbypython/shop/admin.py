from django.contrib import admin
from .models import Product

class ShopAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'price', 'image', 'quantity')
    search_fields = ['title']

admin.site.register(Product, ShopAdmin)
