from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.CharField(max_length=122,blank=True)
    email = models.EmailField(max_length=122,blank=True)
    phone = models.CharField(max_length=13,blank=True)
    password = models.CharField(max_length=122,blank=True)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to='profile_pics', blank=True)
    skill_set = models.CharField(max_length=200,blank=True)
    learning_interests = models.CharField(max_length=200,blank=True)
    completed_courses = models.CharField(max_length=200,blank=True)
    certifications = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.user