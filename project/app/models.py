from django.db import models

# Create your models here.


class Contact(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=30)
    message = models.TextField(max_length=30, blank=True)

    def __str__(self):
        return  self.email


