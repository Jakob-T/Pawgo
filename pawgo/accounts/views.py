from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .models import CustomUser 
from pawgoapp import urls


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('telephone_number')
        is_walker = request.POST.get('is_walker', '') == 'on'
        
        if username and email and password and phone_number: 
            user = CustomUser.objects.create_user(username=username, email=email, password=password, phone_number=phone_number, is_walker=is_walker)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/register.html', {'error_message': 'Molim te popuni sva polja'})

    return render(request, 'accounts/register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
                
            else:
                return render(request, 'accounts/login.html', {'error_message': 'Netočno korisničko ime ili lozinka'})
        else:
            return render(request, 'accounts/login.html', {'error_message': 'Ispunite sva polja'})
    
    return render(request, 'accounts/login.html')


