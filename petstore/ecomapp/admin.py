from django.contrib import admin
from ecomapp.models import Product, contactenquiry

# Register your models here.
#admin.site.register(product)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','age','cat','pdetail','is_active']
    list_filter=['cat','is_active']

admin.site.register(Product,ProductAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','message']

admin.site.register(contactenquiry,ContactAdmin)