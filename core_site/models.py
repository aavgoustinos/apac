from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=50)
    slider_description = models.CharField(max_length=100)
    slider_image = models.FileField(null=True, blank=True, upload_to="slider_images/")
    order = models.CharField(max_length=10)
    slug = models.CharField(max_length=100)
    slider_online = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# News model.
class New(models.Model):
    news_title = models.CharField(null=True, blank=True, max_length=200)
    news_image = models.FileField(null=True, blank=True, upload_to="news_images/")
    news_description = RichTextField(config_name='default', blank=True)
    date = models.DateField(default=datetime.now)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return  self.news_title

class Page(models.Model):
    page_title = models.CharField(null=True, blank=True, max_length=100)
    page_image = models.FileField(null=True, blank=True, upload_to="page_images/")
    page_description = RichTextField(config_name='default', blank=True)
    date = models.DateField(default=datetime.now)
    slug = models.SlugField(max_length=200, unique=True)
    page_online = models.BooleanField("Online Click Yes ",default=True)

    def __str__(self):
        return  self.page_title