from django.utils import timezone
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.baseApp.models import Project
from apps.blogApp.models import PostCategories, Post
from django.db.models import F

class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'https'
    i18n = True

    def items(self):
        return ['baseApp:index', 'baseApp:about_us',]

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        # This part check between created and updated date of lastest Project and use the latest date
        latest_updated_item = Project.objects.all().order_by(F('updated').desc(nulls_last=True))[0]
        latest_created_item = Project.objects.all().order_by(F('created').desc(nulls_last=True))[0]
        if latest_updated_item.updated:
            if latest_updated_item.updated >= latest_created_item.created:
                latest_item = latest_updated_item
                return latest_item.updated
            else:
                # Use the last created of Asset for each page
                latest_item = latest_created_item
                return latest_item.created
        else:
            latest_item = latest_created_item
            return latest_item.created


# Projects sitemap
class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    protocol = 'https'
    i18n = True

    def items(self):
        return Project.objects.all()

    def lastmod(self, item):
        if item.updated:
            return item.updated
        else: return item.created


# All Post Page
class AllPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'
    i18n = True

    def items(self):
        return ['blogApp:all_posts',]

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        # This part check between created and updated date of lastest Asset and use the latest date
        latest_updated_item = Post.objects.all().order_by(F('updated').desc(nulls_last=True))[0]
        latest_created_item = Post.objects.all().order_by(F('created').desc(nulls_last=True))[0]
        if latest_updated_item.updated:
            if latest_updated_item.updated >= latest_created_item.created:
                latest_item = latest_updated_item
                return latest_item.updated
            else:
                # Use the last created of Asset for each page
                latest_item = latest_created_item
                return latest_item.created
        else:
            latest_item = latest_created_item
            return latest_item.created

# Since Post are in different languages, the sitemaps need i18n = True and languages=???
# Post Categories sitemap EN
class PostCategoriesSitemap_en(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'
    i18n = True
    languages = ['en',]

    def items(self):
        return PostCategories.objects.filter(category_lang='en')

    def lastmod(self, item):
        # This part check between created and updated date of lastest Asset and use the latest date
        latest_updated_item = Post.objects.filter(language='en').order_by(F('updated').desc(nulls_last=True))[0]
        latest_created_item = Post.objects.filter(language='en').order_by(F('created').desc(nulls_last=True))[0]
        if latest_updated_item.updated:
            if latest_updated_item.updated >= latest_created_item.created:
                latest_item = latest_updated_item
                return latest_item.updated
            else:
                # Use the last created of Asset for each page
                latest_item = latest_created_item
                return latest_item.created
        else:
            latest_item = latest_created_item
            return latest_item.created

# Since Post are in different languages, the sitemaps need i18n = True and languages=???
# Posts EN
class PostSitemap_en(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'
    i18n = True
    languages = ['en',]

    def items(self):
        return Post.objects.filter(language='en')

    def lastmod(self, item):
        if item.updated:
            return item.updated
        else: return item.created

# Since Post are in different languages, the sitemaps need i18n = True and languages=???
# Post Categories sitemap TR
class PostCategoriesSitemap_en(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'
    i18n = True
    languages = ['tr',]

    def items(self):
        return PostCategories.objects.filter(category_lang='tr')

    def lastmod(self, item):
        # This part check between created and updated date of lastest Asset and use the latest date
        latest_updated_item = Post.objects.filter(language='tr').order_by(F('updated').desc(nulls_last=True))[0]
        latest_created_item = Post.objects.filter(language='tr').order_by(F('created').desc(nulls_last=True))[0]
        if latest_updated_item.updated:
            if latest_updated_item.updated >= latest_created_item.created:
                latest_item = latest_updated_item
                return latest_item.updated
            else:
                # Use the last created of Asset for each page
                latest_item = latest_created_item
                return latest_item.created
        else:
            latest_item = latest_created_item
            return latest_item.created

# Since Post are in different languages, the sitemaps need i18n = True and languages=???
# Posts TR
class PostSitemap_en(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'
    i18n = True
    languages = ['tr',]

    def items(self):
        return Post.objects.filter(language='tr')

    def lastmod(self, item):
        if item.updated:
            return item.updated
        else: return item.created

# Since Post are in different languages, the sitemaps need i18n = True and languages=???
# Post Categories sitemap FA
class PostCategoriesSitemap_en(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    protocol = 'https'
    i18n = True
    languages = ['fa',]

    def items(self):
        return PostCategories.objects.filter(category_lang='fa')

    def lastmod(self, item):
        # This part check between created and updated date of lastest Asset and use the latest date
        latest_updated_item = Post.objects.filter(language='fa').order_by(F('updated').desc(nulls_last=True))[0]
        latest_created_item = Post.objects.filter(language='fa').order_by(F('created').desc(nulls_last=True))[0]
        if latest_updated_item.updated:
            if latest_updated_item.updated >= latest_created_item.created:
                latest_item = latest_updated_item
                return latest_item.updated
            else:
                # Use the last created of Asset for each page
                latest_item = latest_created_item
                return latest_item.created
        else:
            latest_item = latest_created_item
            return latest_item.created

# Since Post are in different languages, the sitemaps need i18n = True and languages=???
# Posts FA
class PostSitemap_en(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'
    i18n = True
    languages = ['fa',]

    def items(self):
        return Post.objects.filter(language='fa')

    def lastmod(self, item):
        if item.updated:
            return item.updated
        else: return item.created
