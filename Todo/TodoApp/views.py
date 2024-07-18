from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Todo


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        return redirect('login')
    return render(request, 'register.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        validate_user = authenticate(username=username, password=password)

        if validate_user is not None:
            login(request, validate_user)
            return redirect('home')
    return render(request, 'login.html')


def home(request):
    todos = Todo.objects.order_by('-id')
    return render(request, 'home.html', {'todo': todos})


def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('desc')
        Todo.objects.create(title=title, description=description)

    return redirect('home')


def complete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.completed = True
    todo.save()
    return redirect('home')


def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('home')





def user_logout(request):
    logout(request)
    return redirect('login')





