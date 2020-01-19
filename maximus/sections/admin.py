from django.contrib import admin

from .models import Section



class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'trainer')
    list_display_links = ('id', 'title')
    list_filter = ('trainer', )
    list_editable = ('is_published', )
    search_fields = ('title', 'description', 'price')
    list_per_page = 25

admin.site.register(Section, SectionAdmin)