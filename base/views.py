import operator

from django.http.response import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login
from django.db.models import Count, Q
from datetime import datetime
from .models import Task, Profile, Notion
from .forms import EditProfileForm, SignUpForm, TaskForm, NotionForm, ProfileForm


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = SignUpForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
        if User.objects.filter(username = request.POST['username']).exists():
              print('Already taken')


    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        context['k'] = context['tasks'].filter(complete=True).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        context['search_input'] = search_input

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

    def dispatch(self, request, *args, **kwargs):
        task=self.get_object()
        if task.user != self.request.user:
            raise Http404("You don't have permission to view this Task")
        return super().dispatch(request, *args, **kwargs)


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')

    def dispatch(self, request, *args, **kwargs):
        task=self.get_object()
        if task.user != self.request.user:
            raise Http404("You don't have permission to edit this Task")
        return super().dispatch(request, *args, **kwargs)


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


class About(ListView):
    model= Task
    template_name = 'base/about.html'


class TopUsersView(View):
    def get(self, request):
        template = 'base/top-users.html'
        context = {'top_users': self.get_top_users()}
        return render(request, template, context)

    def get_top_users(self):
        top_users = User.objects.annotate(task_completed=Count(
            'tasks', filter=Q(tasks__complete=True))).order_by('-task_completed')
        return top_users



class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'base/edit_profile.html'
    success_url = reverse_lazy('tasks')
    
    def get_object(self):
        return self.request.user


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'base/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'base/edit_profile_page.html'
    form_class=ProfileForm
    
    success_url = reverse_lazy('tasks')

class NotionList(ListView):
    model = Notion
    context_object_name = 'notions'
    template_name = 'base/notion.html'
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notions'] = context['notions'].filter(user=self.request.user)
      

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['notions'] = context['notions'].filter(title__icontains=search_input)
        context['search_input'] = search_input

        return context

class NotionDetail(DetailView):
    model = Notion
    context_object_name = 'notion'
    
    template_name = 'base/notion_detail.html'

class NotionCreate(LoginRequiredMixin, CreateView):
    model = Notion
    form_class = NotionForm
    success_url = reverse_lazy('notions')

class NotionUpdate(LoginRequiredMixin, UpdateView):
    model = Notion
    template_name = 'base/notion_update.html'
    fields = ['title', 'body']

class DeleteNotiontView(DeleteView, LoginRequiredMixin):
     model = Notion
     template_name = 'base/notion_confirm_delete.html'
     success_url = reverse_lazy('notions')

class CreateProfilePageView(CreateView):
    model = Profile
    
    template_name = 'base/create_profile.html'
    fields = ['profile_pic', 'bio', 'facebook', 'twitter', 'instagram']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('tasks')