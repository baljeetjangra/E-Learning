from django.contrib import admin
from .models import Standard, Chapter,  Subject
# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at')
    search_fields = ['name']
    prepopulated_fields ={'slug':('name',)}
admin.site.register(Subject, SubjectAdmin)


class StandardAdmin(admin.ModelAdmin):
    list_display =('name','created_at','updated_at')
    search_fields =['name']
    date_hierarchy = 'created_at'
    prepopulated_fields ={'slug':('name',)}
admin.site.register(Standard, StandardAdmin)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('chapter_no','standard','created_at','updated_at')
    search_fields = ['chapter_no']
    date_hierarchy = 'created_at'
    list_filter =('standard',)    
    prepopulated_fields ={'slug':('chapter_name',)}
admin.site.register(Chapter, ChapterAdmin)

# class NoteAdmin(admin.ModelAdmin):
#     list_display = ('name','chapter','standard','created_at','updated_at')
#     search_fields = ['name']
#     date_hierarchy = 'created_at'
#     list_filter =('chapter','standard')   
#     prepopulated_fields ={'slug':('name',)}


# admin.site.register(Note, NoteAdmin)