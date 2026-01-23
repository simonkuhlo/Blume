from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render


def login_page(request):
    match request.method:
        case 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                return
        case 'GET':
            return render(request, "user/login_page.html")
        case _:
            return 404

def logout_page(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def register_page(request):
    match request.method:
        case 'POST':
            pass

@login_required
def own_entry(request):
    pass

@login_required
def account_page(request):
    pass