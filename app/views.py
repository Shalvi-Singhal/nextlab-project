# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rest_framework import  viewsets, permissions
from .models import App, Profile, TaskCompletion
from .serializer import AppSerializer, UserSerializer, TaskCompletionSerializer
import re
from django.http import JsonResponse

def my_view(request):
    text = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}'

    numbers = re.findall(r'(?<=background-color: orange;">)\d+(?=<)', text)

    return JsonResponse(numbers, safe=False)



class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskCompletionViewSet(viewsets.ModelViewSet):
    queryset = TaskCompletion.objects.all()
    serializer_class = TaskCompletionSerializer
    permission_classes = [permissions.IsAuthenticated]

@login_required(login_url='login_view')
def home(request):
    user = Profile.objects.get(username = request.user)
    if user.is_admin:
        apps = App.objects.all()
        return render(request, 'admin_dashboard.html',{'apps':apps})

    return render(request, 'home.html', {'user': user})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('home')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        profile_picture = request.FILES['profile_picture']
        user = Profile.objects.create_user(username=username, password=password, name=name, profile_picture=profile_picture)
        user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html')

@login_required
def apps_list(request):
    apps = App.objects.all()
    return render(request, 'apps_list.html', {'apps': apps})

@login_required
def app_detail(request, app_id):
    app = App.objects.get(id=app_id)
    return render(request, 'app_detail.html', {'app': app})

@login_required
def add_app(request):
    return render(request, 'add_app.html')

@login_required
def save_app(request):
    if request.method == 'POST':
        app_name = request.POST['name']
        points = request.POST['points']
        app = App.objects.create(name= app_name, points = points)
        app.save()
        return render(request, 'app_saved.html', {'app':app})

@login_required
def task_submit(request, task_id):
    if request.method == 'POST':
        screenshot = request.FILES['screenshot']
        user = Profile.objects.get(username = request.user)
        user_id = request.user.id

        points = App.objects.get(id = task_id).points
        if user.points:
            user_points = user.points + points
        else:
            user_points = points
        user.points = user_points
        user.save()
        task = TaskCompletion.objects.create(user_id = user_id, app_id=task_id, screenshot=screenshot)
        task.save()
       
        return render(request, 'task_submit.html', {'task': task, 'user_points':user_points})