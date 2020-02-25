from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render
from webob import request
from werkzeug.utils import redirect

from users.models import Profile

from .forms import CreatPers
from .models import Pers


# Create your views here.
# hna  ghi bach njiobe  le  nom dyale  lutilisateur 
def base(request):
    user = User.objects.all(username=username)

    context = {
        'user': user
    }
    return render(request, 'base.html', context)

def home(request):
    u = User.objects.get(username=username)
    context = {
        'user': u,
        'title':'Home'
    }
    return render(request, 'home.html', context )

def personel(request):
    pers = Pers.objects.all()
    context = {
    'title' : 'Personel',
    'pers': pers,
    }
    return render(request, 'personel.html', context)
    
 # last work in this  im stoped in file  html creation form & make stayl 
def add_pers(request):
    if request.method == 'POST':
        form = CreatPers(request.POST)
        if form.is_valid :
            form.save()
            messages.success (request, f'New Pers has been created!')
            return redirect('/personel')
    else:
        form = CreatPers(request.POST)

    context = {
        'form':form ,
        'title':'Add_Pers'
    }
    return render(request,'addpers.html',context)






def materiel(request):
    context = {
        'title': 'materiel'
    }
    return render(request, 'materiel.html', context)
