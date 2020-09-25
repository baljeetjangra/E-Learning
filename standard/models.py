from django.db import models
from django.urls import reverse
import os
# Create your models here.

class Subject(models.Model):
    name = models.CharField( max_length=50)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Standard(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("standard:subject-detail", kwargs={"slug": self.slug})


class Chapter(models.Model):
    standard = models.ForeignKey(Standard, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Standard.subject, related_name='subject_key', on_delete=models.CASCADE)
    chapter_no = models.CharField(max_length=100)
    chapter_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.chapter_name}"

    # def get_absolute_url(self):
    #     return reverse("standard:chapter-detail", kwargs={"slug": self.slug})

# class Note(models.Model):
#     standard = models.ForeignKey(Standard, on_delete=models.SET_NULL, null=True)
#     chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)
#     upload_file = models.FileField(upload_to="notes/%Y/%m/%d/")
#     description = models.CharField(max_length=250, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def delete(self, using=None, keep_parents=True):
#         self.upload_file.storage.delete(self.upload_file.name)
#         super().delete()

#     def __str__(self):
#         return f"{self.name}(Notes) of {self.chapter.name}({self.standard.name})"
    
    # def get_absolute_url(self):
    #     return reverse("standard:notes-detail", kwargs={"slug": self.slug})