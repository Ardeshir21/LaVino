from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.utils import translation
from . import models
from apps.blogApp import models as blogAppModels



# Here is the Extra Context ditionary which is used in get_context_data of Views classes
def get_extra_context():
    extraContext = {
        'from_python': _('SOMETHING'),
        'current_language': translation.get_language(),
        }
    return extraContext


# Index View
class IndexView(generic.TemplateView):
    # Select template based on requested language
    def get_template_names(self):
        current_lang = translation.get_language()
        # RTL languages
        if current_lang == 'fa':
            return ["baseApp/layouts/photohub/RTL/index.html"]
        # LTR languages
        else:
            return ["baseApp/layouts/photohub/LTR/index.html"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()
        # Categories based on current language
        context['blog_categories'] = blogAppModels.PostCategories.objects.filter(category_lang=current_lang)

        # Banner
        context['bannerImages'] = models.Banner.objects.filter(useFor__exact='HOME', active__exact=True)
        # Featured images
        context['featuredImages'] = models.FeaturedImages.objects.filter(active__exact=True)
        return context

# About Us View
class AboutUsView(generic.TemplateView):
    # Select template based on requested language
    def get_template_names(self):
        current_lang = translation.get_language()
        # RTL languages
        if current_lang == 'fa':
            return ["baseApp/layouts/photohub/RTL/about_us.html"]
        # LTR languages
        else:
            return ["baseApp/layouts/photohub/LTR/about_us.html"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()
        # Categories based on current language
        context['blog_categories'] = blogAppModels.PostCategories.objects.filter(category_lang=current_lang)

        # Banner
        context['bannerImages'] = models.Banner.objects.filter(useFor__exact='HOME', active__exact=True)
        # Featured images
        context['featuredImages'] = models.FeaturedImages.objects.filter(active__exact=True)
        return context

# Project Portfolio
class ProjectsView(generic.TemplateView):
    def get_template_names(self):
        current_lang = translation.get_language()
        if current_lang == 'fa':
            return ["baseApp/layouts/photohub/RTL/projects.html"]
        else:
            return ["baseApp/layouts/photohub/LTR/projects.html"]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())
        # It must be checked in the method not in attributes
        current_lang = translation.get_language()
        # Categories based on current language
        context['blog_categories'] = blogAppModels.PostCategories.objects.filter(category_lang=current_lang)

        # Projects
        context['Projects'] = models.Project.objects.filter(active__exact=True)
        return context

# Project Detail
class ProjectDetailView(generic.DetailView):
    context_object_name = 'project'
    model = models.Project

    def get_template_names(self):
        current_lang = translation.get_language()
        if current_lang == 'fa':
            return ["baseApp/layouts/photohub/RTL/project_detail.html"]
        else:
            return ["baseApp/layouts/photohub/LTR/project_detail.html"]

    def get_object(self, **kwargs):
        singleResult = self.model.objects.get(slug=self.kwargs['slug'], active=True)
        # To implement save method on the model which adds view count
        singleResult.save()
        return singleResult

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()
        # Categories based on current language
        context['blog_categories'] = blogAppModels.PostCategories.objects.filter(category_lang=current_lang)
        
        # This view have no pageTitle
        # Get the first PostCategories object of the current post
        context['slideContent'] = "AAAA"

        return context
