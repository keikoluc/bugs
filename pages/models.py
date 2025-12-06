from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    telegram = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.phone
