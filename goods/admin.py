from django.contrib import admin

# Register your models here.
from goods.models import *
from keys.admin import KeysTabAdmin

class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery
    
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']
    
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ["name", "price", "discount"]
    list_editable = ["discount", "price",]
    search_fields = ["name", "description"]
    list_filter = ['discount',  'category']
    fields = [
        "name",
        "slug",
        "availabilitys",
        "description",
        "image",
        "poster",
        "category",
        "is_displayed",
        ("price", "discount"),
        
        ("languages","region", "services"),
        "genry",
        ("platform", "datas"),
        ("publisher", "developer"),
        "system",
        "processor",
        "rampc",
        "videocard",
        "direx",
        "disk",
        "additional",
        "video"

    ]
    inlines = [GalleryInline, KeysTabAdmin,]
    

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Platforms)
class PlatformsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(OCSystem)
class OCSystemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(ProcessorPC)
class ProccesorsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(RAMPC)
class RAMAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(VideoCard)
class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Direx)
class DirexAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Disk)
class DiskAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
