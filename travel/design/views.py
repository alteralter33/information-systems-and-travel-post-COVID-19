from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from design.models import Comments
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class CustomBackend(ModelBackend):
    """email can also login"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=User.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                error_msg = "Username already exists :("
                return render(request, 'register.html', {'error_msg': error_msg})
            elif User.objects.filter(email = email).exists():
                error_msg = "Email already exists :("
                return render(request, 'register.html', {'error_msg': error_msg})
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                return redirect('login')
        else:
            error_msg = "Confirm password failed :("
            return render(request, 'register.html', {'error_msg': error_msg})
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request,user)         #If the authentication is successful, the login status will be maintained
            return redirect('index')
        else:
            error_msg = "Wrong user name or password :("
            return render(request,'login.html',{'error_msg':error_msg})
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('index')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'tasmanian_devil.html')

def travel_system(request):
    if request.user.is_authenticated:
        return render(request, 'travel_system.html')
    else:
        return redirect('login')

def travel_system1(request):
    if request.user.is_authenticated:
        return render(request, 'travel_system1.html')
    else:
        return redirect('login')

def travel_system2(request):
    if request.user.is_authenticated:
        return render(request, 'travel_system2.html')
    else:
        return redirect('login')

def travel_modes(request):
    if request.user.is_authenticated:
        return render(request, 'travel_modes.html')
    else:
        return redirect('login')

def travel_modes1(request):
    if request.user.is_authenticated:
        return render(request, 'travel_modes1.html')
    else:
        return redirect('login')

def travel_modes2(request):
    if request.user.is_authenticated:
        return render(request, 'travel_modes2.html')
    else:
        return redirect('login')

def safety(request):
    if request.user.is_authenticated:
        return render(request, 'safety.html')
    else:
        return redirect('login')

def safety1(request):
    if request.user.is_authenticated:
        return render(request, 'safety1.html')
    else:
        return redirect('login')

def safety2(request):
    if request.user.is_authenticated:
        return render(request, 'safety2.html')
    else:
        return redirect('login')

def contact(request):
    comments = Comments.objects.all().order_by('-id')
    return render(request, 'contact.html',{'comments': comments})

def comment(request):
    if request.method == 'POST':
        user = request.user
        text = request.POST.get('text', '').strip()
        comment = Comments()
        comment.comment_author = user
        comment.comment_content = text
        comment.save()
        comments = Comments.objects.all().order_by('-id')
        return render(request, 'contact.html',{'comments': comments})
    else:
        return render(request, 'login.html')

