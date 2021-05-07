from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext as _
from django.utils import translation
from django.conf import settings
from apps.baseApp import models as baseAppModels
from . import models



# Here is the Extra Context ditionary which is used in get_context_data of Views classes
def get_extra_context():
    extraContext = {
        'DEBUG_VALUE': settings.DEBUG,
        'from_python': _('SOMETHING'),
        'current_language': translation.get_language(),
        }
    return extraContext



class PostList(generic.ListView):
    context_object_name = 'allPosts'
    model = models.Post
    paginate_by = 3

    # Select template based on requested language
    def get_template_names(self):
        # It must be checked in the method not in attributes
        current_lang = translation.get_language()

        # RTL languages
        if current_lang == 'fa':
            return ["blogApp/layouts/photohub/RTL/blog.html"]
        # LTR languages
        else:
            return ["blogApp/layouts/photohub/LTR/blog.html"]

    def get_queryset(self, **kwargs):
        result = super(PostList, self).get_queryset()

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()
        result= result.filter(language=current_lang, status=True).order_by('-created')

        return result

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()
        # Categories based on current language
        context['blog_categories'] = models.PostCategories.objects.filter(category_lang=current_lang)
        # Banner Image
        context['breadcumb'] = baseAppModels.Banner.objects.get(useFor__exact='BLOG_HOME', active__exact=True)

        return context

class CategoryListView(generic.ListView):
    context_object_name = 'allPosts'
    model = models.Post
    paginate_by = 6

    # Select template based on requested language
    def get_template_names(self):
        # It must be checked in the method not in attributes
        current_lang = translation.get_language()

        # RTL languages
        if current_lang == 'fa':
            return ["blogApp/layouts/photohub/RTL/blog-category.html"]
        # LTR languages
        else:
            return ["blogApp/layouts/photohub/LTR/blog-category.html"]


    def get_queryset(self, **kwargs):
        result = super(CategoryListView, self).get_queryset()

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()
        # Categories -- For filtering based on the categories
        result= result.filter(language=current_lang, categories__slug=self.kwargs['category'], status=True).order_by('-created')

        return result

    # If the user change the url manually, this get method will handle the issues and redirect her to Blog page
    def get(self, request, *args, **kwargs):
        current_lang = translation.get_language()
        current_category_lang = models.PostCategories.objects.get(slug=self.kwargs['category']).category_lang

        # It redirects to blog page if the selected language is not match with article language
        if current_category_lang != current_lang:
            return HttpResponseRedirect(reverse("blogApp:all_posts"))
        else:
            return super().get(self.request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Append shared extraContext
        context.update(get_extra_context())

        # It must be checked in the method not in attributes
        current_lang = translation.get_language()
        # Categories based on current language Navbar
        context['blog_categories'] = models.PostCategories.objects.filter(category_lang=current_lang)

        # The category object itself
        context['categoryObject'] = models.PostCategories.objects.get(slug=self.kwargs['category'])

        # result counte
        context['resultCount'] = len(self.get_queryset())
        return context

class PostDetail(generic.DetailView):
    context_object_name = 'post'
    model = models.Post

    # Select template based on requested language
    def get_template_names(self):
        # It must be checked in the method not in attributes
        current_lang = translation.get_language()

        # RTL languages
        if current_lang == 'fa':
            return ["blogApp/layouts/photohub/RTL/single-blog.html"]
        # LTR languages
        else:
            return ["blogApp/layouts/photohub/LTR/single-blog.html"]

    # If the user change the url manually, this get method will handle the issues and redirect her to Blog page
    def get(self, request, *args, **kwargs):
        current_lang = translation.get_language()
        current_post = self.get_object()

        # It redirects to blog page if the selected language is not match with article language
        if current_post.language != current_lang:
            return HttpResponseRedirect(reverse("blogApp:all_posts"))
        else:
            return super().get(self.request, *args, **kwargs)

    def get_object(self, **kwargs):
        singleResult = self.model.objects.get(slug=self.kwargs['slug'], status=True)
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
        context['blog_categories'] = models.PostCategories.objects.filter(category_lang=current_lang)

        # Get the first PostCategories object of the current post
        context['categoryObject'] = self.get_object().categories.first()

        return context

# class PostSearch(generic.ListView):
#     context_object_name = 'allPosts'
#     template_name = 'blogApp/search_result.html'
#     model = models.Post
#     paginate_by = 8
#
#     def get_queryset(self, **kwargs):
#         result = super(PostSearch, self).get_queryset()
#
#         # Get the GET content >>> name='s'
#         keyword = self.request.GET.get('s')
#         if not(keyword==None or keyword==''):
#             # Content Search -- For filtering based on the Text Search
#             result= result.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword), language='EN', status=True).order_by('-created_on')
#
#         return result
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Append shared extraContext
#         context.update(get_extra_context())
#
#         # This title is different for this view
#         context['slideContent'] = baseAppModel.Slide.objects.get(useFor__exact='BLOG_SEARCH', active__exact=True)
#         context['pageTitle'] = 'SEARCH'
#         # result counte
#         context['resultCount'] = len(self.get_queryset())
#         return context
