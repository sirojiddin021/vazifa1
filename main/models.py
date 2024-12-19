from django.db import models

# Create your models here.
class Info(models.Model):
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    instagram = models.URLField()
    facebook = models.URLField()
    youtube = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return self.phone


class Inance(models.Model):
    image = models.ImageField(upload_to='media/inance')
    title = models.CharField(max_length=200)
    text = models.TextField()


class About(models.Model):
    image = models.ImageField(upload_to='media/about')
    title = models.CharField(max_length=200)
    text = models.TextField()


class Services(models.Model):
    image = models.ImageField(upload_to='media/services', null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()


class Clients(models.Model):
    image = models.ImageField(upload_to='media/clients')
    name = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name