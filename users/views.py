from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Events
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# Create your views here.
#test now

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm (request.POST)
        if form.is_valid ():
            form.save ()
            username = form.cleaned_data.get ('username')
            messages.success (request, f'Your account has been created! You are now able to log in')
            return redirect ('login')
    else:
        form = UserRegisterForm ()
    context = {
        'form': form,
        'title': 'Register'
    }
    return render (request, 'register.html', context)


def login(request):
    context = {
        'title': 'Login'
    }
    return render (request, 'login.html', context)


def profile(request):
    context = {
        'title': 'Profile'
    }
    return render (request, 'profile.html', context)


def img_prof(request):
    img = User.Profile.objects.all ()
    context = {
        'img': img
    }
    return (request, 'base.html', context)


def calendar(request):
    all_events = Events.objects.all ()
    context = {
        "events": all_events,
    }
    return render (request, 'home.html', context)


@login_required
def add_event(request):
    start = request.GET.get ("start", None)
    end = request.GET.get ("end", None)
    title = request.GET.get ("title", None)
    event = Events(name=str (title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get ("start", None)
    end = request.GET.get ("end", None)
    title = request.GET.get ("title", None)
    id = request.GET.get ("id", None)
    event = Events.objects.get (id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save ()
    data = {}

    return JsonResponse (data)


def remove(request):
    id = request.GET.get ("id", None)
    event = Events.objects.get (id=id)
    event.delete ()
    data = {}
    return JsonResponse (data)
