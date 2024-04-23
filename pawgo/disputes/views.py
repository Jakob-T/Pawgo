from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from disputes.models import Dispute
from jobs.models import Job
from django.contrib import messages


@login_required
def disputeform(request):
    
    if request.method=="POST":
        user=request.user
        title=request.POST.get('title')
        description=request.POST.get('description')
        
        job=get_object_or_404(Job, title=title)
        if job.walked_by is not None and job.state==Job.IZVRSEN:
            dispute=Dispute(user=user,walker=job.walked_by,description=description)
            dispute.save()
            return render(request,'disputes/disputeform.html', context={'dispute':dispute})
        else:
            messages.error(request, 'Invalid job or job state for dispute.')
            
    
    return render(request,'disputes/disputeform.html')
