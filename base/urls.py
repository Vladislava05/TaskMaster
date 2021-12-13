from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

from .views import *

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name ='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name ='task'),
    path('task-create/', TaskCreate.as_view(), name ='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name ='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name ='task-delete'),
    path('top-users/', TopUsersView.as_view(), name='top-users'),
    path('about/', About.as_view(), name='about'),
     #path('password/', auth_views.PasswordChangeView.as_view(template_name='base/change-password.html')),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='base/change-password.html')),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    
]
