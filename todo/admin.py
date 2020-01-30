# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Todo
# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["id","author","iscompleted","date","content"]
    list_display_links = ["content"]
    list_filter = ["iscompleted","id","date"]
    
    class Meta:
        model = Todo
