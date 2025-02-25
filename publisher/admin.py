from django.contrib import admin


from publisher.models import Publishers
# Register your models here.
@admin.register(Publishers)
class PublishersAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}