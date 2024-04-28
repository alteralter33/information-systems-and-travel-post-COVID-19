"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from design import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('travel_system/',views.travel_system, name='travel_system'),
    path('travel_system1/',views.travel_system1, name='travel_system1'),
    path('travel_system2/',views.travel_system2, name='travel_system2'),
    path('travel_modes/', views.travel_modes, name='travel_modes'),
    path('travel_modes1/', views.travel_modes1, name='travel_modes1'),
    path('travel_modes2/', views.travel_modes2, name='travel_modes2'),
    path('safety/', views.safety, name='safety'),
    path('safety1/', views.safety1, name='safety1'),
    path('safety2/', views.safety2, name='safety2'),
    path('contact/', views.contact, name='contact'),
    path('comment/', views.comment, name='comment'),

]
