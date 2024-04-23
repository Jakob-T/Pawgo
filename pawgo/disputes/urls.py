from django.urls import path
from . import views


urlpatterns = [
    path("dispute/",views.disputeform,name="dispute"),
]