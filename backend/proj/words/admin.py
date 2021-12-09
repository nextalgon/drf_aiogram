from django.contrib import admin
from . import models


class WordsAmin(admin.ModelAdmin):
    list_display = ['pk', 'gender', 'words']
    list_editable = ['gender', 'words']


admin.site.register(models.Words, WordsAmin)
