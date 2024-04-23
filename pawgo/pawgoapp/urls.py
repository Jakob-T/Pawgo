from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.login_view, name="login"),
    path('topup/', views.top_up_balance, name="topup"),
    path('nadoplate/', views.nadoplate, name="nadoplate"),
    path("dashboard/",views.user_dashboard, name="dashboard"),
    path("profile/", views.self_profile_view, name="profile"),
    path("<slug:username>/", views.profile_view, name="profile_user"),
]