from django.db import models
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from tinymce.models import HTMLField
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.
GENRE_CHOICES = [
    ('Adventure','Adventure'),
    ('Biography','Biography'),
    ('Culinary',"Culinary"),
    ('Fiction','Fiction'),
    ('Mythology','Mythology'),
    ('Non-Fiction','Non-Fiction'),
    ('Technology','Technology'),
    ]

def upload_image(instance,filename):
    return f'{instance.title}/{filename}'

class Blog_page(models.Model):

    title = models.CharField(_("Title"), max_length=250, blank=True, null=True)
    author = models.CharField(_("Author"), max_length=100,blank=True, null=True)
    #content = models.TextField(_("Content"), blank=True, null=True)
    published_on = models.DateTimeField(_("Published On"), default=timezone.now)
    genre = models.CharField(_("Genre"), max_length=20,choices=GENRE_CHOICES, blank=True, null=True)
    modified_on = models.DateTimeField(_("Modified On"), auto_now=True, blank=True, null=True)
    title_image = models.ImageField(_("Image"), upload_to=upload_image, blank=True, null=True)
    body = HTMLField(_("Content"), blank=True, null=True)
    keyword = TaggableManager(verbose_name='keyword')
    slug = models.SlugField(_("slug"), blank=True, unique=True)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.writer}')
        super(Blog_page, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("each_article", kwargs={"slug":self.slug})