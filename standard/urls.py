from django.urls import path
from .views import home, StandardList, chapterList, noteList, subjectList

app_name = 'standard'

urlpatterns = [
    path('', home, name='home'),
    path('classes/', StandardList.as_view(), name='classes'),
    path('<slug:slug>/', subjectList, name='subject-detail'),
    # path('<slug:slug>/', chapterList, name='standard-detail'),
    # path('<slug:class_slug>/<slug:subject_slug>/',subjectList, name='subject-list'),
    # path('<slug:class_slug>/<slug:chapter_slug>/', noteList, name='chapter-detail'),
]

