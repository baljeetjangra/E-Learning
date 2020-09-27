from django.contrib import admin
from .models import Standard, Chapter,  Book, Contact
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('name','standard','created_at','updated_at')
    list_filter = ('standard',)
    search_fields = ['name']
    prepopulated_fields ={'slug':('name',)}
admin.site.register(Book, BookAdmin)


class StandardAdmin(admin.ModelAdmin):
    list_display =('name','created_at','updated_at')
    search_fields =['name']
    date_hierarchy = 'created_at'
    prepopulated_fields ={'slug':('name',)}
admin.site.register(Standard, StandardAdmin)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('chapter_name','book','created_at','updated_at')
    search_fields = ['chapter_name']
    date_hierarchy = 'created_at'
    list_filter =('book',)    
    prepopulated_fields ={'slug':('chapter_name',)}
admin.site.register(Chapter, ChapterAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone')
    list_filter = ('email',)
    search_fields = ['name']
admin.site.register(Contact, ContactAdmin)


# class NoteAdmin(admin.ModelAdmin):
#     list_display = ('name','chapter','created_at','updated_at')
#     search_fields = ['name']
#     date_hierarchy = 'created_at'
#     list_filter =('chapter',)   
#     prepopulated_fields ={'slug':('name',)}


# admin.site.register(Note, NoteAdmin)