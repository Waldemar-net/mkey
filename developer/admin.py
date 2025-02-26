from django.contrib import admin


from developer.models import Developers
# Register your models here.
@admin.register(Developers)
class DeveloperAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}