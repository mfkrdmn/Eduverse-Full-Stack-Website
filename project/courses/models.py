from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=200, unique=True, help_text="Type course name")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to = "courses/%Y/%m/%d")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self) :
        return self.name