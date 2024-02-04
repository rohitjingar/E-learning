from django.urls import path
from .views import CourseCreateView, CourseDeleteView,CourseListView,CourseDataView,CourseDataDeleteView

urlpatterns = [
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:pk>/delete/', CourseDeleteView.as_view(), name='delete_course'),
    # add more paths here as needed
    path('', CourseListView.as_view(), name='course-list'),
    path('<int:pk>/CourseData', CourseDataView.as_view(),name = 'Course-Data'),
    path('<int:pk>/delete_Coursedata/', CourseDataDeleteView.as_view(), name='delete_course_data'),
    
]