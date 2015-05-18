from django.contrib import admin

from .models import Page, Story

class PageInline(admin.TabularInline):
    model = Page
    extra = 1

class StoryAdmin(admin.ModelAdmin):
    inlines = [
        PageInline,
    ]

admin.site.register(Story, StoryAdmin)
