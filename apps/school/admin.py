from django.contrib import admin

from .models import Attendance, ClassGroup, Lesson, Student, Teacher

# admin.site.register(Attendance)
admin.site.register(ClassGroup)
admin.site.register(Lesson)
admin.site.register(Student)
admin.site.register(Teacher)
