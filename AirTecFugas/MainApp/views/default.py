"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'MainApp/Home/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def dashboard(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'MainApp/Dashboard/dashboard.html',
        {
            'title':'Dashboard',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'MainApp/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'MainApp/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def mapafugas(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'MainApp/Fuga/mapa-fugas.html',
        {
            'title':'mapa fugas',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
