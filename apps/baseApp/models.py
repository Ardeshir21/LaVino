from django.db import models
from django.urls import reverse_lazy, reverse
from django.utils import timezone

# Variables
YES_NO_CHOICES = [(True, 'Yes'), (False, 'No')]

PAGE_CHOICES = [('HOME', 'Homepage'),
                ('ABOUT_US', 'About Us'),
                ('BLOG_HOME', 'Blog Homepage'),
                ('BLOG_SEARCH', 'Blog Search'),]


class Banner(models.Model):
    image = models.ImageField(upload_to='baseApp/banners/', blank=True, null=True,
                                help_text='HOME: 1920x850, Breadcrumb: 1920x400')
    # navigator of the slider
    image_thumbnail = models.ImageField(upload_to='baseApp/banners/thumbnail', blank=True, null=True,
                                help_text='HOME: 100x60')
    title = models.CharField(max_length=110, null=True, blank=True)
    sub_title = models.CharField(max_length=110, null=True, blank=True)
    title_fa = models.CharField(max_length=110, null=True, blank=True)
    sub_title_fa = models.CharField(max_length=110, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    display_order = models.PositiveIntegerField(null=True, blank=True)
    useFor = models.CharField(max_length=50, choices=PAGE_CHOICES, null=True, blank=True)
    active = models.BooleanField(choices=YES_NO_CHOICES, default=False)

    def __str__(self):
            return "{}: banner for {}".format(self.id, self.useFor)

    class Meta():
        ordering = ['display_order']

class ProjectCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=300, unique=True, null=True, blank=True)
    name_fa = models.CharField(max_length=150, unique=True, null=True, blank=True)
    description_fa = models.CharField(max_length=300, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, related_name='categories', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, null=True, blank=True)
    title_fa = models.CharField(max_length=100, unique=True, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    description_fa = models.TextField(max_length=500, null=True, blank=True)
    image_thumb = models.ImageField(upload_to='baseApp/projects/', null=True,
                                help_text='Image 600x700')
    image_main = models.ImageField(upload_to='baseApp/projects/', null=True,
                                help_text='Image 1600x900')
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, allow_unicode=True)
    featured = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    active = models.BooleanField(choices=YES_NO_CHOICES, default=True)
    display_order = models.PositiveIntegerField(null=True, blank=True)

    created = models.DateField(editable=False)
    updated = models.DateField(editable=False, null=True)
    view = models.PositiveIntegerField(editable=False, default=0)

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['display_order']

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        # Update Date
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()

        # View count
        self.view += 1
        return super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('baseApp:project_detail', args=(self.slug,))

class ProjectImages(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='baseApp/project/', null=True,
                                help_text='Image 1600x1100')
    display_order = models.PositiveIntegerField(null=True, blank=True)
    active = models.BooleanField(choices=YES_NO_CHOICES, default=True)

    class Meta():
        verbose_name_plural = "Project Images"
        ordering = ['display_order']

# Images for homepage
class FeaturedImages(models.Model):
    image = models.ImageField(upload_to='baseApp/featured_images/', null=True,
                                help_text='Image 1600x1100')
    title = models.CharField(max_length=100, unique=True, null=True, blank=True)
    title_fa = models.CharField(max_length=100, unique=True, null=True, blank=True)
    display_order = models.PositiveIntegerField(null=True, blank=True)
    active = models.BooleanField(choices=YES_NO_CHOICES, default=True)

    class Meta():
        verbose_name_plural = "Featured Images"
        ordering = ['display_order']
