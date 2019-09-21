from django.contrib import admin
from Quiz.models import *



class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('category',)

class SubCategoryAdmin(admin.ModelAdmin):
    search_fields = ('sub_category',)
    list_display = ('sub_category','category',)
    list_filter = ('category',)


# Register your models here.

admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)