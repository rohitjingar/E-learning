from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course
from .models import CourseData
from .forms import CourseForm
from .forms import CourseDataForm
from home.models import UserProfile
import random
import string
from .course_image_generator import generate_course_image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django.views.generic import ListView
from django.urls import reverse
# Create your views here.
@method_decorator(login_required, name='dispatch')
class CourseCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = CourseForm()
        user_profile = UserProfile.objects.get(user=request.user)
        courses = Course.objects.filter(instructor=user_profile)
        return render(request, 'create_course.html', {'form': form, 'user_courses': courses})

    def post(self, request):
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            user_profile = UserProfile.objects.get(user=request.user)
            course.instructor = user_profile
            if request.POST.get('generate_enrollment_key') == 'on':
                # Generate random enrollment key
                key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
                course.enrollment_key = key
            image = generate_course_image(form.cleaned_data['name'])
            image_io = BytesIO()
            image.save(image_io, format='JPEG')
            image_file = InMemoryUploadedFile(image_io, None, 'course_img.jpg', 'image/jpeg', image_io.tell(), None)
            course.course_image = image_file
            course.save()
            courses = Course.objects.filter(instructor=user_profile)
            return render(request, 'create_course.html', {'form': form, 'user_courses': courses })
        else:
            user_profile = UserProfile.objects.get(user=request.user)
            courses = Course.objects.filter(instructor=user_profile)
            return render(request, 'create_course.html', {'form': form, 'user_courses': courses})

@method_decorator(login_required, name='dispatch')
class CourseDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        course = get_object_or_404(Course, id=pk, instructor__user=request.user)
        if request.method == "POST":
            course.delete()
            return redirect('course-list')

@method_decorator(login_required, name='dispatch')
class CourseListView(LoginRequiredMixin, View):
    def get(self, request):
        return redirect('course-create')

@method_decorator(login_required, name='dispatch')
class CourseDataView(LoginRequiredMixin, View):
     def get(self, request,pk):
        form = CourseDataForm()
        course_key = Course.objects.get(pk=pk)
        course_data = CourseData.objects.filter(course=course_key)
        return render(request, 'course_data.html', {'form': form, 'course_data': course_data, 'course_id': course_key})
     
     def post(self,request,pk):
         form = CourseDataForm(request.POST, request.FILES)
         if form.is_valid():
           course_data = form.save(commit=False)
           course_key = Course.objects.get(pk=pk)
           course_data.course = course_key
           user_profile = UserProfile.objects.get(user=request.user)
           course_data.instructor = user_profile  # set the instructor for the course_data object
           course_data.save()
           course_data = CourseData.objects.filter(course=course_key)
           return render(request, 'course_data.html', {'form': form, 'course_data': course_data})
         else:
             course_key = Course.objects.get(pk=pk)
             course_data = CourseData.objects.filter(course=course_key)
             return render(request, 'course_data.html', {'form': form, 'course_data': course_data})

@method_decorator(login_required, name='dispatch')
class CourseDataDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        course_data = get_object_or_404(CourseData, id=pk, instructor__user=request.user,)
        if request.method == "POST":
            course_data.delete()
            return redirect(reverse('Course-Data', kwargs={'pk':course_data.course.id }))