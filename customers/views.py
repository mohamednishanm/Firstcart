from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Customer
from django.contrib import messages


def sign_out(request):
    logout(request)
    return redirect('home')
# Create your views here.
def show_account(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            # Create a new user account
            user = User.objects.create_user(username=username, password=password, email=email)
            # create a customer account
            customer = Customer.objects.create(name=username ,user=user, address=address, phone=phone)
            messages.success(request, 'Account created successfully')
        except Exception as e:
            error_message = 'duplicate username or invalid credentials'
            messages.error(request, error_message)


    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')


    return render(request, 'account.html',context)