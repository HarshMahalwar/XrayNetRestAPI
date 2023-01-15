from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Books)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
