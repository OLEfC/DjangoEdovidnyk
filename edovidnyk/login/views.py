from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        email = request.POST['email']
        # Створення користувача за допомогою create_user
        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponse('User registered')
    else:
        return render(request, 'register.html')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('User logged in')
        else:
            return HttpResponse('Invalid credentials')
    else:
        return render(request, 'login.html')
