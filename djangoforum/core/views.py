import datetime

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from story.models import Story

def index(request):
    today = datetime.date.today()

    stories = Story.objects.all()[0:50]

    return render(request, 'core/index.html', {
        'stories': stories
    })

def new(request):
    today = datetime.date.today()

    stories = Story.objects.filter(created_at__gte=today).order_by('-created_at')

    return render(request, 'core/new.html', {
        'stories': stories
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:    
        form = UserCreationForm()

    return render(request, 'core/signup.html',
        {'form' : form}              
    )

