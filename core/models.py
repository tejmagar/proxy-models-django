from django.db import models


# Create your models here.


class Person(models.Model):
    class TYPES(models.TextChoices):
        TEACHER = 'teacher', 'Teacher'
        STUDENT = 'student', 'Student'

    name = models.CharField(max_length=60)
    type = models.CharField(max_length=60, choices=TYPES.choices)

    def __str__(self):
        return self.name


class TeacherManager(models.Manager):
    def get_queryset(self):
        return super(TeacherManager, self).get_queryset().filter(type=Teacher.TYPES.TEACHER)


class Teacher(Person):
    objects = TeacherManager()

    class Meta:
        proxy = True


class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(type=Person.TYPES.STUDENT)


class Student(Person):
    objects = StudentManager()

    class Meta:
        proxy = True
