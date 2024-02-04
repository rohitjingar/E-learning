from django.db import models
from home.models import UserProfile
from django.utils import timezone
from django.contrib.auth.models import User

class Course(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    enrollment_key = models.CharField(max_length=20, unique=True, null=True, blank=True)
    course_image = models.ImageField(upload_to='course_images', blank=True, null=True)
    def __str__(self):
        return self.name

class CourseData(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course,on_delete = models.CASCADE)
    instructor = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    def __str__(self):
        return self.title