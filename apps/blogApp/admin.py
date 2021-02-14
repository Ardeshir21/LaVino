from django.contrib import admin
from .models import Post, PostCategories
from django import forms
from django.db import models



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    # Using Widgets
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple(attrs={'multiple': True})},
    }

class PostCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category",)}

admin.site.register(Post, PostAdmin)
admin.site.register(PostCategories, PostCategoriesAdmin)
