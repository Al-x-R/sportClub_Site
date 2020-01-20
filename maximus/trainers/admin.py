from django.contrib import admin

from .models import Trainer

class TrainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'birthday_date')
    list_display_links = ('id', 'first_name', 'last_name',)
    search_fields = ('name', )
    list_per_page = 25


admin.site.register(Trainer, TrainerAdmin)