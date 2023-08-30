from django.shortcuts import render , redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .models import Profile

from MyApp.forms import ProfileImageForm
# Create your views here.

class LoginView(View):
    def get(self, request):
      return render(request, 'myapp/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username doesn't exist!")
            return redirect(reverse('login'))

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('profile')) 
        else:
            messages.error(request, "Invalid Password")
            return redirect(reverse('login'))  
          
       
  
class RegisterView(View):
  def get(self, request):
      return render(request, 'myapp/registration.html')
    
  def post(self, request ):
    data = request.POST
    
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if User.objects.filter(username = username).exists():
        messages.error(request, 'Username already taken !!')
        return redirect('register')
        
    user = User.objects.create(first_name = first_name , last_name = last_name , username = username , email= email)
    user.set_password(password)
    user.save()
    messages.success(request,'successfully created account !!')
    
    return redirect('login')
  
  

class ProfileDetailsView(LoginRequiredMixin, View):
    def get(self, request):
      
        # profile = request.user.profile
        return render(request, 'myapp/profile.html', {})

    def post(self, request):
        image = request.FILES.get('profile_pic')  
        profile = Profile.objects.filter(user = request.user).first()    
        if not profile: 
            profile = Profile.objects.create(user = request.user , image = image)
        else:
            profile.image = image
            profile.save()
            
        messages.success(request, "Profile picture updated!")
        return redirect(reverse('profile'))  
    

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')
           
    
