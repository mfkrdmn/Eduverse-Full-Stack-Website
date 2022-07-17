from email.policy import default
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe

# Create your models here.


class Teachers(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = RichTextUploadingField(blank=True)
    image = models.ImageField(upload_to = "courses/%Y/%m/%d")
    facebook = models.URLField(max_length=100, blank=True)
    twitter = models.URLField(max_length=100, blank=True)
    linkedin = models.URLField(max_length=100, blank=True)
    youtube = models.URLField(max_length=100, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self) :
        return self.name

