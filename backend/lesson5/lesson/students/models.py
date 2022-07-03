from dataclasses import dataclass
from re import T
from tabnanny import verbose
from django.db import models

class Subject(models.Model):
    name = models.CharField(verbose_name="Название",
                             max_length=100)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
    
    class Meta:
        verbose_name ="Предмет"
        verbose_name_plural = "Предметы"
    
class StudentGroup(models.Model):
    name = models.CharField(verbose_name="Имя",
                             max_length=100)
    students_number = models.DecimalField(verbose_name="Количество студентов",
                                        max_digits=4,
                                        decimal_places=0,
                                        null=True,
                                        blank=True)
    subject = models.ForeignKey(Subject,verbose_name="Предмет",
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
    
    class Meta:
        verbose_name ="Группа студентов"
        verbose_name_plural = "Группы студентов"

class Student(models.Model):

    SURNAME_CHOICES=(
        ('Petrenko','Петренко'),
        ('Ivanenko','Иваненоко'),
        ('Sidorov','Сидоров'),
        ('Maximenko','Максименко'),
        ('Mykhailenko','Михайленко')
    )
    name = models.CharField(verbose_name="Имя",
                             max_length=100,
                             blank=True,
                             null=True)
    surname= models.CharField(verbose_name="Фамилия",
                            max_length=100,
                            null=True,
                            blank=True,
                            choices=SURNAME_CHOICES)
    birthday = models.DateField(verbose_name="День рождения",
                                null=True,
                                blank=True)
    group = models.ForeignKey(StudentGroup,verbose_name="Группа",
                                on_delete=models.SET_NULL,
                                related_name="students",
                                null=True,
                                blank=True )
    

    def __str__(self) -> str:
        return self.name


    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)
    
    class Meta:
        verbose_name ="Студент"
        verbose_name_plural = "Студеты"