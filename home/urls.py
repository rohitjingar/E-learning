from django.urls import path
from .views import IndexView, LoginView,SignupPage, UserProfileDetailView,LogoutPage,EditProfileView,EditProfileData

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupPage.as_view(), name='signup'),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile-detail'),
    path('logout/', LogoutPage.as_view(),name='logout'),
    path('edit_profile/', EditProfileView.as_view(), name='edit-profile'),
    path('edit_profile_data/', EditProfileData.as_view(), name='edit_profile_data'),
]