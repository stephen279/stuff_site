from django.contrib import admin

# Register your models here.

from .models import Thing,Step

admin.site.register(Thing)
admin.site.register(Step)