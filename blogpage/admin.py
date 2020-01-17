from django.contrib import admin
from .models import Blog_page

# Register your models here.
@admin.register(Blog_page)
class Blog_pageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','slug']
