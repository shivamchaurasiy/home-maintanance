from django.shortcuts import render


def home(req):
    return render(req, 'index.html')
def about(req):
    return render(req, 'about.html')
def contact(req):
    return render(req, 'contact.html')
def services(req):
    return render(req, 'services.html')
def login(req):
    return render(req, 'login.html')
def signup(req):
    return render(req, 'signup.html')
