from django.contrib import admin

from Dashboard.models import Person, Student, Lecturer, Department, Course, Timetable


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('department', 'title', 'code', 'unit')

class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_name', 'first_name')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('person', 'matric_no', 'department')


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('person', 'staff_id', 'department')


class TimetableAdmin(admin.ModelAdmin):
    list_display = ('course', 'day', 'slot')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Timetable, TimetableAdmin)
