from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=125, choices=[
                ('COMPUTER SCIENCES', 'COMPUTER SCIENCES'),
                ('BIOLOGICAL SCIENCES', 'BIOLOGICAL SCIENCES'),
                ('CHEMICAL SCIENCES', 'CHEMICAL SCIENCES'),
                ('MANAGEMENT SCIENCES', 'MANAGEMENT SCIENCES'),
                ('MASS COMMUNICATION', 'MASS COMMUNICATION'),
                ('CRIMINOLOGY', 'CRIMINOLOGY'),
                ('GENERAL STUDIES', 'GENERAL STUDIES'),
            ])

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    code = models.CharField(max_length=10)
    unit = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)

    def __str__(self):
        return self.user


class Student(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    matric_no = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.matric_no


class Lecturer(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.staff_id
