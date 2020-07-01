"""Views for the Info app"""
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.db.models import F

from .models import PointTracker
from .forms import LoginForm

def home(request):
    """Home Page View.

    Shows home page info\n
    If NOT AUTHENTICATED:
        show a login form.\n
    If AUTHENTICATED:
        show a logout button.\n
    If POST and AUTHENTICATED:
        log the user out.\n
    If POST and NOT AUTHENTICATED:
        handle login details
        login/show error
    """
    template = 'info/home.html'
    form = LoginForm()
    context = {'form': form, 'user': request.user}

    if request.method == 'POST' and not request.user.is_authenticated:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('info:home')
            else:
                context['form_error'] = True
    elif request.method == 'POST': # and not authenticated implied
        logout(request)
        return redirect('info:home')
    
    return render(request, template, context)

def gecko_points(request):
    """Gecko Point Page View.
    
    Shows a list of point trackers.\n
    If POST and AUTHENTICATED and NOT CURRENT USER:
        give the specified user a point.\n
    If POST and CURRENT USER:
        add user_error to context\n
    If POST and not AUTHENTICATED:
        add auth_error to context
    """
    point_trackers = PointTracker.objects.order_by('gecko_points')
    template = 'info/points.html'
    context = {'point_trackers': point_trackers}

    if request.method == 'POST' and request.user.is_authenticated:
        username = request.POST['username']
        if username == request.user.username:
            context['user_error'] = True
        else:
            point_getter = get_user_model().objects.get(username=username)
            point_tracker = PointTracker.objects.get(point_haver=point_getter)
            point_tracker.gecko_points = F('gecko_points') + 1
            point_tracker.save()
            return redirect('info:points')
    elif request.method == 'POST': # and not authenticated
        context['auth_error'] = True
        
    return render(request, template, context)