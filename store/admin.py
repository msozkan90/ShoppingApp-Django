from django.contrib import admin

# Register your models herea
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
#admin.site.register(Category)
admin.site.register(MainCategory)
admin.site.register(Brand)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category"]
    list_display_links = ["name", "category"]

    class Meta:
        model = Category