from django.db import models
import os
# Create your models here.

class Standard(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    


class Chapter(models.Model):
    standard = models.ForeignKey(Standard, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"

class Note(models.Model):
    standard = models.ForeignKey(Standard, on_delete=models.SET_NULL, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    upload_file = models.FileField(upload_to="notes/%Y/%m/%d/")
    description = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete(self, using=None, keep_parents=True):
        self.upload_file.storage.delete(self.upload_file.name)
        super().delete()

    def __str__(self):
        return f"{self.name}(Notes) of {self.chapter.name}({self.standard.name})"
    
    