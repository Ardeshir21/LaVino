from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.utils import translation
from . import models, forms
from django.conf import settings
from apps.blogApp import models as blogAppModels
from django.contrib import messages


# Here is the Extra Context ditionary which is used in get_context_data of Views classes
def get_extra_context():
    extraContext = {
        'DEBUG_VALUE': settings.DEBUG,
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
        # Categories based on current language Navbar
        context['blog_categories'] = blogAppModels.PostCategories.objects.filter(category_lang=current_lang)
        # Current language
        context['current_lang'] = current_lang
        # Banner
        context['bannerImages'] = models.Banner.objects.filter(useFor__exact='HOME', active__exact=True)
        # Featured images
        context['featuredImages'] = models.FeaturedImages.objects.filter(active__exact=True)
        return context

# About Us View
class AboutUsView(generic.edit.FormView):

    success_url = reverse_lazy('baseApp:about_us')

    # Select template based on requested language
    def get_template_names(self):
        current_lang = translation.get_language()
        # RTL languages
        if current_lang == 'fa':
            return ["baseApp/layouts/photohub/RTL/about_us.html"]
        # LTR languages
        else:
            return ["baseApp/layouts/photohub/LTR/about_us.html"]

    # Select the form_class based on requested language
    def get_form_class(self):
        current_lang = translation.get_language()
        # RTL languages
        if current_lang == 'fa':
            return forms.ContactForm_fa
        # LTR languages
        else:
            return forms.ContactForm

    def form_valid(self, form):
        # Success Message
        current_lang = translation.get_language()
        # RTL languages
        if current_lang == 'fa':
            messages.add_message(self.request, messages.SUCCESS, 'پیام شما با موفقیت ارسال شد.')
        # LTR languages
        else:
            messages.add_message(self.request, messages.SUCCESS, 'Your message has been successfully sent.')

        # This method is called when valid form data has been POSTed.
        # current_url = resolve(request.path_info).url_name
        form.send_email(current_url=self.request.build_absolute_uri())
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()
        # Categories based on current language Navbar
        context['blog_categories'] = blogAppModels.PostCategories.objects.filter(category_lang=current_lang)

        # Banner Image
        context['breadcumb'] = models.Banner.objects.get(useFor__exact='ABOUT_US', active__exact=True)
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
        # Categories based on current language Navbar
        context['blog_categories'] = blogAppModels.PostCategories.objects.filter(category_lang=current_lang)
        # Current language
        context['current_lang'] = current_lang
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
        # Current language
        context['current_lang'] = current_lang
        # Categories based on current language Navbar
        context['blog_categories'] = blogAppModels.PostCategories.objects.filter(category_lang=current_lang)
        return context
