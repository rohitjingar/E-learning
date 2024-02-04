from django.contrib import admin
from .models import Course
from .models import CourseData
# Register your models here.

admin.site.register(Course)
admin.site.register(CourseData)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'instructor', 'enrollment_key')

