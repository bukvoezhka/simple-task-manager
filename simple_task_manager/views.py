from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def sign_in(request):
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
