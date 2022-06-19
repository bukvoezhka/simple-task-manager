from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, message='There was an error logging in. Check credentials and try again.')
            return redirect('sign_in')
    else:
        return render(request, 'sign_in.html')


def logout_view(request):
    logout(request)
    return redirect('sign_in')
