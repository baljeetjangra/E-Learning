from django.contrib import admin
from .models import Standard, Chapter, Note
# Register your models here.

admin.site.register(Standard)

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name','standard','created_at','updated_at')
    search_fields = ['name']
    date_hierarchy = 'created_at'
    list_filter =('standard',)    

admin.site.register(Chapter, ChapterAdmin)

class NoteAdmin(admin.ModelAdmin):
    list_display = ('name','chapter','standard','created_at','updated_at')
    search_fields = ['name']
    date_hierarchy = 'created_at'
    list_filter =('chapter','standard')    

admin.site.register(Note, NoteAdmin)