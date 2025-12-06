from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import About, Contact

admin.site.register(About)
admin.site.register(Contact)
