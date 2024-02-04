from django.views import View
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView as AuthLoginView
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.urls import reverse

class IndexView(View):
    def get(self, request):
        return render(request,'home.html')
    

class LoginView(AuthLoginView):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        uname = request.POST.get('username')
        passw = request.POST.get('password')

        user = authenticate(request, username=uname, password=passw)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(self.request, 'Invalid username or password ')
            return render(request, 'login.html')
   

class SignupPage(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(self.request, 'Your password and confirm password are not the same!')
            return render(request, 'signup.html')
        
        elif UserProfile.objects.filter(user=uname).exists():
            messages.error(self.request, 'Username is already taken!')
            return render(request, 'signup.html') 
        
        else:
            my_auth_user = User.objects.create_user(uname,email,pass1)
            my_auth_user.save()
            my_user = UserProfile(user=uname, email=email, password=pass1)
            my_user.save()
            messages.success(self.request, 'You have successfully registered! Please login to continue.')
            return redirect('login')


class UserProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'userprofile_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = UserProfile.objects.get(user=self.request.user)
        context['user_profile'] = user_profile
        return context
      
class LogoutPage(View):
    def get(self, request):
        logout(request)
        return redirect('home')
    
class EditProfileView(View):
    def post(self, request):
       pic = request.FILES.get('picture')
       user_profile = UserProfile.objects.get(user=request.user)
       user_profile.picture = pic
       user_profile.save()
       return redirect(reverse('userprofile-detail', kwargs={'pk': user_profile.pk}))
    
class EditProfileData(LoginRequiredMixin, TemplateView):
    template_name = 'userprofile_update.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = UserProfile.objects.get(user=self.request.user)
        context['user_profile'] = user_profile
        return context

    def post(self, request):
        phone = request.POST.get('phone')
        skill = request.POST.get('skill')
        Learning_interests = request.POST.get('Learning_interests')
        courses = request.POST.get('courses')
        bio = request.POST.get('bio')
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.phone = phone
        user_profile.skill_set=skill
        user_profile.learning_interests = Learning_interests
        user_profile.completed_courses = courses
        user_profile.bio = bio
        user_profile.save()
        return redirect(reverse('userprofile-detail', kwargs={'pk': user_profile.pk}))