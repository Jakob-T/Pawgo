from django.shortcuts import render, get_object_or_404,redirect
from .models import Job
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from disputes.views import disputeform as delegate_dispute_job  # Assuming this is your existing disputeform view

@login_required
def jobs_list(request):
    #sort=request.GET.get('sort', 'asc')
    jobs=Job.objects.filter(accepted=False)
    #if sort=="desc":
        #jobs=Job.objects.order_by("-pub_date")
    #else:
        #jobs=Job.objects.order_by("pub_date")

    context = {
        'jobs': jobs,
    }
    return render(request, 'jobs/jobs.html',context)
@login_required
def new_job(request):
    if request.method == "POST":
        title = request.POST.get('title')
        dog_breed = request.POST.get('dog_breed')
        duration = request.POST.get('duration')
        location = request.POST.get('location')
        budget = request.POST.get('budget')
        description = request.POST.get('description')
        
        if title and dog_breed and duration and location and budget and description: 
            try:
                budget = int(budget)
                if budget > 0:
                    if Job.objects.filter(title=title).exists():
                        error_message = 'Molim vas odaberite drugačiji naslov'
                    else:
                        job = Job(
                            user=request.user,
                            title=title,
                            dog_breed=dog_breed,
                            duration=duration,
                            location=location,
                            budget=budget,
                            description=description,
                            
                            pub_date=timezone.now(),
                            accepted=False,
                        )
                        job.save()
                        return redirect('home')
                else:
                    error_message = 'Molim vas upišite pozitivan broj'
            except ValueError:
                error_message = 'Molim vas upišite ispravan broj za budžet'
        else:
            error_message = 'Molim vas popunite sva polja'
            
    return render(request, 'jobs/newjob.html')
@login_required
def job_detail(request, job_id):
    job=get_object_or_404(Job, pk=job_id)
    
    context={
        'job':job,
    }
    return render(request, 'jobs/jobdetail.html',context)
@login_required
def accept_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    if request.user.is_authenticated and not job.accepted and request.user.is_walker:
        if request.method == 'POST':
            job.walked_by = request.user
            job.accepted = True
            job.save()
            return redirect('jobs:job_detail', job_id=job.id)
    
    return redirect('jobs:job_detail', job_id=job.id)
@login_required
def finish_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    if request.user.is_authenticated and request.user == job.walked_by and job.accepted:
        if request.method == 'POST':
            user=job.walked_by
            user.token_balance+=job.duration*job.budget
            user.save()
            job.state = Job.IZVRSEN
            job.save()
            return redirect('jobs:job_detail', job_id=job.id)

    return redirect('jobs:job_detail', job_id=job.id)

@login_required
def return_alljobs(request):
    jobs=Job.objects.filter()
    
    return jobs

@login_required
def dispute_form(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    
    if request.method == "POST":
        return delegate_dispute_job(request)
    else:
        return redirect('jobs:job_detail', job_id=job.id)

    