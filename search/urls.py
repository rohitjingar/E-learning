from django.urls import path
from .views import CourseSearchView,EnrollCourseView,EnrolledCoursesView,EnrolledCourseDetailView

urlpatterns = [
    path('course/', CourseSearchView.as_view(), name='search-course'),
    path('enroll-course/<int:course_id>/', EnrollCourseView.as_view(), name='enroll_course'),
    
    path('enrolled-courses/', EnrolledCoursesView.as_view(), name='enrolled-courses'),
    path('coursedata/<int:pk>/', EnrolledCourseDetailView.as_view(), name='course-data-detail'),
]