from django.contrib import admin
from django.urls import path
from courses.views import add_course, list_courses

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-course/', add_course, name='add_course'),
    path('courses/', list_courses, name='list_courses'),
    path('', list_courses),
]