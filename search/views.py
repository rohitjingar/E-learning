from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.db.models import Q
from course.models import Course,CourseData
from home.models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Enrollment
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.contrib import messages
from urllib.parse import urlencode
from django.views.generic import DetailView
@method_decorator(login_required, name='dispatch')
class CourseSearchView(ListView):
    model = Course
    template_name = 'search_course.html'
    context_object_name = 'courses'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q')
        user_profile = UserProfile.objects.get(user=self.request.user)
        object_list = self.model.objects.exclude(instructor=user_profile)
        if query:
           object_list = object_list.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
           )
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q')
        user_profile = UserProfile.objects.get(user=self.request.user)
        enrolled_courses = Enrollment.objects.filter(user=user_profile).values_list('course_id', flat=True)
        context['enrolled_courses'] = enrolled_courses
        return context
    
class EnrollCourseView(LoginRequiredMixin, CreateView):
    model = Enrollment
    fields = ['enrollment_key']
    template_name = 'search_course.html'
    
    def form_valid(self, form):
        user_profile = UserProfile.objects.get(user= self.request.user)
        form.instance.user = user_profile
        course_id = self.kwargs['course_id']
        form.instance.course_id = course_id
        
        # Check if the enrollment key matches the course's enrollment key
        course = Course.objects.get(pk=course_id)
        if course.enrollment_key:
            # Check if the enrollment key matches the course's enrollment key
            if form.cleaned_data['enrollment_key'] == course.enrollment_key:
                messages.success(self.request, 'Enrollment successful!')
                return super().form_valid(form)
            else:
                return self.form_invalid(form)
        else:
            # Enroll the user directly if the course does not have an enrollment key
            messages.success(self.request, 'Enrollment successful!')
            return super().form_valid(form)
        
    def form_invalid(self, form):
         messages.error(self.request, 'Invalid enrollment key')
         return redirect(reverse('search-course'))
    
    def get_success_url(self):
        return reverse('search-course')
    
class EnrolledCoursesView(LoginRequiredMixin, ListView):
    model = Enrollment
    template_name = 'enrolled_courses.html'
    context_object_name = 'enrollments'

    def get_queryset(self):
        user_profile = UserProfile.objects.get(user= self.request.user)
        return Enrollment.objects.filter(user=user_profile)

class EnrolledCourseDetailView(DetailView):
    model = Course
    template_name = 'enroll_course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course_data'] = CourseData.objects.filter(course=self.object)
        return context