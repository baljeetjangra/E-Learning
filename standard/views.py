from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Standard, Chapter, Note


def home(request):
    return render(request, 'standard/index.html')

class StandardList(ListView):
    model = Standard
    template_name = 'standard/classes.html'


def subjectList(request, slug):
    class_item = Standard.objects.get(slug=slug)
    subject_list = class_item.subject.all()
    return render(request, 'standard/subject.html', {'subject_list':subject_list})


def chapterList(request, slug):
    standard = Standard.objects.get(slug=slug)
    chapter_list = Chapter.objects.filter(standard=standard.id)
    return render(request,'standard/chapter.html',{'chapter_list':chapter_list})    






def noteList(request, class_slug, chapter_slug):
    class_slug = Standard.objects.get(slug=class_slug)
    chapter_slug = Chapter.objects.get(slug=chapter_slug)

    return render(request, 'standard/course-details.html', {'class_slug':class_slug,'chapter_slug':chapter_slug})




