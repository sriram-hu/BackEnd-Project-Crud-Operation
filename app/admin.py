from django.contrib import admin
from .models import  *

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('HallTickectnumber','Student_name','Father_name','Mother_name','Email')


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name','age','emailid','password')

    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'fathername', 'mothername', 'email', 'gender', 'specialization', 'name_course', 'coursecode', 'course_duration')