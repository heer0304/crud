from django.contrib import admin
from .models import Customer,Product,Order

# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','contact_no','pincode']
    list_display_links = ['id','first_name']
    list_per_page = 10

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','unit_price']
    list_display_links = ['id','name']
    list_per_page = 10

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id','customer_id','product_id','unit_price','qty','total_price']
    list_display_links = ['id','customer_id']
    list_per_page = 10
