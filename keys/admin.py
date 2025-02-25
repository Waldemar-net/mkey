from django.contrib import admin

from keys.models import Keys


class KeysTabAdmin(admin.TabularInline):
    model = Keys
    fields = "product", "keys", "user", "created_timestamp", "datas"
    search_fields = "product", "keys", "user", "created_timestamp", "datas"
    readonly_fields = ("created_timestamp",)
    extra = 1

@admin.register(Keys)
class KeysAdmin(admin.ModelAdmin):
    list_display = ["product", "keys", "activated_key", "user", "created_timestamp", 'datas',]
    search_fields = ["product", "keys", "activated_key", "user", "created_timestamp", 'datas', ]

    