from django.shortcuts import render, redirect, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from itertools import chain
from django.utils import timezone

from accounts import views as accountviews
from accounts.models import CustomUser

from jobs import views as jobsviews
from jobs.models import Job

from pawgoapp.models import TopUp



def index(request):
    return HttpResponse("Proseci psa.")

def home(request):
    return render(request,'pawgoapp/home.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    accountviews.user_login(request)
    return redirect('login')

@login_required
def user_dashboard(request):
    user=get_object_or_404(CustomUser, username=request.user.username)
    if request.method == "POST":
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.phone_number = request.POST.get('phone_number')
        user.is_walker = request.POST.get('is_walker', '') == 'on'
        user.save()
        return HttpResponseRedirect(
            reverse('dashboard')
        )
    #jobs=jobsviews.return_alljobs(request)
    
    accepted_jobs=Job.objects.filter(accepted=True,walked_by=request.user, state='U tijeku')
    posted_jobs=Job.objects.filter(user=request.user)
    
    finished_accepted_jobs=Job.objects.filter(walked_by=request.user, state = 'Izvršen')
    finished_posted_jobs=Job.objects.filter(user=request.user,state='Izvršen')
    finished_jobs=list(chain(finished_posted_jobs,finished_accepted_jobs))

    
    context={
        'user':user,
        'accepted_jobs': accepted_jobs,
        'posted_jobs':posted_jobs,
        'finished_jobs':finished_jobs,
    }
    return render(request,'pawgoapp/user_dashboard.html',context)

@login_required
def self_profile_view(request):
    return render(request, 'pawgoapp/userprofile.html')

@login_required
def profile_view(request, username):
    user = get_object_or_404(CustomUser, username = username)
    context={
        'user':user,
    }
    return render(request, 'pawgoapp/userprofile.html', context)

@login_required
def review(request):
    return render(request, 'pawgoapp/recenzija.html')

@login_required
def top_up_balance(request):
    if request.method == "POST":
        code = request.POST.get('code')
        if code:
            try:
                topup = TopUp.objects.get(code=code)
                user = request.user
                if topup.expiration_date < timezone.now():
                    messages.error(request, 'Kod je ISTEKAO.')
                elif not topup.isused:
                    user.token_balance += topup.value
                    topup.isused = True
                    topup.expiration_date=timezone.now()
                    topup.save()

                    user.used_topups.add(topup)

                    user.save()
                    return redirect('home')
                else:
                    messages.error(request, 'Kod je već iskorišten.')
            except TopUp.DoesNotExist:
                messages.error(request, 'Kod nije pronađen.')
        else:
            messages.error(request, 'Kod nije pronađen.')

    return render(request, 'pawgoapp/topup.html')

@login_required
def nadoplate(request):
    nadoplate = request.user.used_topups.all().order_by('-expiration_date')

    context={
        'nadoplate':nadoplate,
    } 

    return render(request, 'pawgoapp/nadoplate.html',context)