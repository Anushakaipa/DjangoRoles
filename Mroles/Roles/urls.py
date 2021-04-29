from django.urls import path
from Roles import views
from django.contrib.auth import views as d

urlpatterns = [
    path('',views.home,name="hm"),
    path('lg/',d.LoginView.as_view(template_name="html/login.html"),name="lgo"),
    path('lgn/',d.LogoutView.as_view(template_name="html/logout.html"),name="lgon"),
    path('ins/',views.index,name="ind"),
]
