from django.contrib import admin

from Dashboard.models import Person, Student, Lecturer, Department, Course


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


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Lecturer, LecturerAdmin)
