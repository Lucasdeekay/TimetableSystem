from rest_framework import viewsets

from Dashboard.models import Department, Course, Person, Student, Lecturer
from Dashboard.serializers import DepartmentSerializer, CourseSerializer, PersonSerializer, StudentSerializer, \
    LecturerSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class LecturerViewSet(viewsets.ModelViewSet):
    serializer_class = LecturerSerializer
    queryset = Lecturer.objects.all()
