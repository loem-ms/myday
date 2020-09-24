from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel, AssignmentModel, NewsModel
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime



# Create your views here.

def signupview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        try:
            User.objects.create_user(username_data,'',password_data)
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーは既に登録されています。'})
    else:
        return render(request, 'signup.html', {})
    return render(request, 'signup.html', {})

def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data, password=password_data)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('login')

class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

class AssignmentList(ListView):
    template_name = 'assignment.html'
    model = AssignmentModel

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)

class TodoCreate(CreateView):
    template_name = 'createTodo.html'
    model = TodoModel
    fields = ('title','author','content','category')
    success_url = reverse_lazy('home')

class AssignmentCreate(CreateView):
    template_name = 'createAssignment.html'
    model = AssignmentModel
    fields = ('title','content','author','deadline')
    success_url = reverse_lazy('home')

@login_required
def home(request):
    todo = TodoModel.objects.filter(author=request.user)
    assignment = AssignmentModel.objects.filter(author=request.user)
    datetimenow = datetime.date.today()
    return render(request,"home.html",{"TodoModel":todo,"AssignmentModel":assignment,"datetimenow":datetimenow})

class TodoDelete(DeleteView):
    template_name = 'deleteTodo.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'updateTodo.html'
    model = TodoModel
    fields = ('title','content','category')
    success_url = reverse_lazy('list')

class AssignmentDelete(DeleteView):
    template_name = 'deleteAssignment.html'
    model = AssignmentModel
    success_url = reverse_lazy('assignment')

class AssignmentUpdate(UpdateView):
    template_name = 'updateAssignment.html'
    model = AssignmentModel
    fields = ('title','content','deadline')
    success_url = reverse_lazy('assignment')

class NewsList(ListView):
    template_name = 'newslist.html'
    model = NewsModel

class NewsCreate(CreateView):
    template_name = 'createNews.html'
    model = NewsModel
    fields = ('title','author','content')
    success_url = reverse_lazy('news')

class NewsUpdate(UpdateView):
    template_name = 'updateNews.html'
    model = NewsModel
    fields = ('title','content')
    success_url = reverse_lazy('list')

