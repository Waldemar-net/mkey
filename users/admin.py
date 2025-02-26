from django.contrib import admin

# Register your models here.
from carts.admin import CartTabAdmin
from carts.models import Cart
from keys.admin import KeysTabAdmin
from orders.admin import OrderItemTabulareAdmin, OrderTabulareAdmin
from users.models import User

#admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username","first_name", "last_name", "email",]
    search_fields = ["username", "fitst_name", "last_name", "email",]

    inlines = [CartTabAdmin, KeysTabAdmin, OrderTabulareAdmin]