from django.db import models
from django.urls import reverse
import os

class Standard(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("standard:book-list", kwargs={"slug": self.slug})

class Book(models.Model):
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    subject = models.CharField( max_length=50)
    name = models.CharField( max_length=50)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.subject}-{self.name} of {self.standard.name}"

    
class Chapter(models.Model):
    # standard = models.ForeignKey(Standard, on_delete=models.SET_NULL, null=True)
    # subject = models.ForeignKey(Standard, related_name='subject_key', on_delete=models.CASCADE)
    book = models.ForeignKey("Book",on_delete=models.CASCADE)
    chapter_no = models.CharField(max_length=100)
    chapter_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    upload_file = models.FileField(upload_to="notes/%Y/%m/%d/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.chapter_name}"
    
    def delete(self, using=None, keep_parents=True):
        self.upload_file.storage.delete(self.upload_file.name)
        super().delete()
        
    # def get_absolute_url(self):
    #     return reverse("standard:chapter-detail", kwargs={"slug": self.slug})

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()




# class Note(models.Model):
#     # standard = models.ForeignKey(Standard, on_delete=models.SET_NULL, null=True)
#     # chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True)
#     chapter = models.OneToOneField(Chapter, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)
#     upload_file = models.FileField(upload_to="notes/%Y/%m/%d/")
#     description = models.CharField(max_length=250, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

  

#     def __str__(self):
#         return f"{self.name}(Notes) of {self.chapter.name}({self.standard.name})"
    # def delete(self, using=None, keep_parents=True):
    #     self.upload_file.storage.delete(self.upload_file.name)
    #     super().delete()
    # def get_absolute_url(self):
    #     return reverse("standard:notes-detail", kwargs={"slug": self.slug})