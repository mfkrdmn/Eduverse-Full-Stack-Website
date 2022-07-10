from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from teachers.models import *
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self) :
        return self.name


class slug_isim(models.CharField):
    def __init__(self, *args , **kwargs):
        super(slug_isim,self).__init__(*args , **kwargs)
    def get_prep_value(self, value) :
        return str(value).lower().replace(" ","_")



class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self) :
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text="Type course name")
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to = "courses/%Y/%m/%d")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    paragraph = models.TextField(blank=True, null=True)
    detail = RichTextUploadingField(default="Type text")
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    teachers = models.ForeignKey(Teachers, null=True, on_delete=models.CASCADE)
    slug = slug_isim(null =True , max_length= 100 )
    
    def __str__(self) :
        return self.name
