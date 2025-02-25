from django.contrib import admin

from comments.models import Comments, CommentsResponse

# Register your models here.
admin.site.register(Comments)
admin.site.register(CommentsResponse)