from django.contrib import admin
from .models import Comments
from django.contrib.auth.models import User

# Register your models here.
@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
     list_display = ['comment_content','comment_time','comment_author']
     list_per_page = 20