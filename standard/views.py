from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Standard, Book, Chapter, Contact
import os


def home(request):
    return render(request, 'standard/index.html')

class StandardList(ListView):
    model = Standard
    template_name = 'standard/classes.html'

def bookList(request, slug):
    class_item = Standard.objects.get(slug=slug)
    book_list = Book.objects.filter(standard=class_item)
    return render(request, 'standard/book.html', {'book_list':book_list})

def chapterList(request, class_slug, book_slug):
    class_item = Standard.objects.get(slug=class_slug)
    book_item = Book.objects.filter(standard=class_item).get(slug=book_slug)
    chapter_list = Chapter.objects.filter(book=book_item)   
    return render(request,'standard/chapter.html',{'chapter_list':chapter_list})    

# def chapterDetail(request, class_slug, book_slug, chapter_slug):
#     class_item = Standard.objects.get(slug=class_slug)
#     book_item = Book.objects.filter(standard=class_item).get(slug=book_slug)
#     chapter_list = Chapter.objects.filter(book=book_item)
#     chapter_detail = chapter_list.get(slug=chapter_slug)

#     return render(request, 'standard/chapter-details.html',{'chapter_detail':chapter_detail})

def about(request):
    return render(request, 'standard/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        new_contact = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
        new_contact.save()
        return redirect('standard:classes')
    return render(request, 'standard/contact.html')