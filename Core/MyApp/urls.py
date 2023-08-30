from django.urls import path

from .views import LoginView , RegisterView, ProfileDetailsView, logout_user
# creating the url pattern for this app

urlpatterns = [
  path('' , LoginView.as_view() , name='login' ),
  path('register/' , RegisterView.as_view() , name='register' ),
  path('profile/' , ProfileDetailsView.as_view() , name='profile' ),
  path('logout/' , logout_user , name='logout' ),
]