from django.urls import path
from .views import home, StandardList, chapterList,  bookList, about, contact

app_name = 'standard'

urlpatterns = [
    path('', home, name='home'),
    path('classes/', StandardList.as_view(), name='classes'),
    path('about/', about, name='about-page'),
    path('contact/', contact, name='contact-page'),
    path('<slug:slug>/', bookList, name='book-list'),
    path('<slug:class_slug>/<slug:book_slug>/',chapterList, name='chapter-list'),
    # path('<slug:class_slug>/<slug:book_slug>/<slug:chapter_slug>/',chapterDetail, name='chapter-detail'),
]

