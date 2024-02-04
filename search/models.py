from django.db import models
from home.models import UserProfile
from django.utils import timezone
from course.models import Course
# Create your models here.

class Enrollment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(default=timezone.now)
    enrollment_key = models.CharField(max_length=20,blank=True)
    def __str__(self):
        return f"{self.user.user} enrolled in {self.course.name}"