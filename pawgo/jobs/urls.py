from django.urls import path
from . import views
from pawgoapp import views as pawgoappviews

app_name = 'jobs'

urlpatterns = [
    path("jobs_list/",views.jobs_list,name="jobs_list"),
    path("new_job/",views.new_job,name="new_job"),
    path("<int:job_id>/",views.job_detail,name="job_detail"),
    path('<int:job_id>/accept/', views.accept_job, name='accept_job'),
    path("<int:job_id>/finish/", views.finish_job, name="finish_job"),
    path("<int:job_id>/dispute-form/", views.dispute_form, name="dispute_form"),
]