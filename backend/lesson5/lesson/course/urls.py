from django.contrib import admin
from django.urls import path
from students.views import SubjectView,StudentLearnSubject


urlpatterns = [
    
    path('subject/',SubjectView.as_view()),
    path('subject/<id>/',StudentLearnSubject.as_view())
]