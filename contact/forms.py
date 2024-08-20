from django.db import models


# Create your models here.
class Contact_form(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Subscriber_form(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)