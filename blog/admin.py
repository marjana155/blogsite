from django.contrib import admin
from .models import Blogs, Category
# Register your models here.


class BlogsAdmin(admin.ModelAdmin):
    exclude = ['pub_date']
    list_display = ('title', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Category, CategoryAdmin)
