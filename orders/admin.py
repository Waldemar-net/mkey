from django.contrib import admin

from orders.models import Order, OrderItem


#admin.site.register(Order)
#admin.site.register(OrderItem)

class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", "price"
    search_fields = (
        "product",
        "name",
    )
    extra = 0

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "name", "price"
    search_fields = (
        "order",
        "product",
        "name",
    )


class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = (
              "id", 
              "is_paid", 
              "status",
              "created_timestamp",
              )
    search_fields = (
        "id", 
        "is_paid", 
        "status",
        "created_timestamp",
    )
    readonly_fields = ("created_timestamp",)
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "email_delivery_adress",
        "is_paid",
        "status",
        "created_timestamp",
    )
    search_fields = (
        "id",
        "user",
        "email_delivery_adress",
        "created_timestamp",
        "is_paid",
    )
    readonly_fields = ("created_timestamp",)
    list_filter = (
        "email_delivery_adress",
        "created_timestamp",
        "user",
    )
    inlines = (OrderItemTabulareAdmin,)
