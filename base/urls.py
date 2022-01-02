from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from base import views
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
    path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('edit_profile_page/<int:pk>/',EditProfilePageView.as_view(), name='edit_user_profile'),
    path('create_profile_page/',CreateProfilePageView.as_view(), name='create_user_profile'),
    path('notion/', NotionList.as_view(), name ='notions'),
    path('notion/<int:pk>/', NotionDetail.as_view(), name ='notion_detail'),
    path('notion-create/', NotionCreate.as_view(), name ='notion-create'),
    path('notion/update/<int:pk>/', NotionUpdate.as_view(), name ='notion-update'),
    path('notion/<int:pk>/', NotionDetail.as_view(), name ='notion'),
    path('notion/<int:pk>/delete', DeleteNotiontView.as_view(), name ='notion-delete'),
    path('contact/', views.contact, name="contact")
]
