from django.contrib import admin
from django.db import models
from .models import (Banner,
                    ProjectCategory,
                    Project,
                    ProjectImages,
                    FeaturedImages)


class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class ProjectImagesInline(admin.TabularInline):
    model = ProjectImages
    list_display = ['project', 'image', 'active', 'display_order']
    list_editable = ['display_order']

class ProjectAdmin(admin.ModelAdmin):

    list_filter = ['title', 'category']
    list_display = ['id', 'category', 'title', 'active', 'featured']
    list_editable = ['active', 'featured']
    prepopulated_fields = {'slug': ('title',)}

    # other Inlines
    inlines = [
        ProjectImagesInline,
    ]

class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'useFor', 'active']
    list_editable = ['useFor', 'active']

class FeaturedImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'display_order', 'active']
    list_editable = ['display_order', 'active']


admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(FeaturedImages, FeaturedImagesAdmin)
