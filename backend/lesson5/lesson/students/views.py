from socket import gaierror
from sqlite3 import DatabaseError
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from students.models import Subject,StudentGroup,Student
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
class SubjectView(View):
    def get(self,request):
        subjects=Subject.objects.all()
        
        return HttpResponse(subjects)


class StudentLearnSubject(View):#Решить вопрос с id
    def get(self, request,id):
        
        try:
            
            
            subjects=Subject.objects.get(id=id)
            group_name=StudentGroup.objects.filter(subject=subjects)
            student_names=[] 
            for groups in group_name:
                stud=Student.objects.filter(group=groups)
                
                for student in stud:
                    student_names.append(student)
                
            return HttpResponse(student_names)
        
            
        except ObjectDoesNotExist:
            return HttpResponse("Такой id не существует")
        