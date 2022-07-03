from django.contrib import admin
from django.urls import path
from students.views import SubjectView,StudentLearnSubject


urlpatterns = [
    
    path('courses/subject/',SubjectView.as_view()),
    path('courses/subject/<id>/',StudentLearnSubject.as_view())
]