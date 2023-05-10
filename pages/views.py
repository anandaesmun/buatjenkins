from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from pages.forms import create_user_form
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('count')
        else:
            messages.info(request, 'Username or Password is Incorrect!')
            return render(request,'index.html', {})

    return render(request,'index.html', {})

def log_out(request):
    logout(request)
    return redirect('home')

def sign_up(request):
    form = create_user_form()

    if request.method == 'POST':
        form = create_user_form(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form, 'username': username}
    return render(request, 'sign_up.html', context)

def count(request):
    if request.method == 'POST':
        a = request.POST['a']
        b = request.POST['b']
        if 'add' in request.POST:
            result = tambah(a,b)
            return render(request,'count.html',{'result':result})
    return render(request,'count.html')

# functions
def tambah(a, b):
    return int(a) + int(b)
