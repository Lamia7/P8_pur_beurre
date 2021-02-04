from django.shortcuts import render


def register(request):
    return render(request, 'register.html')

def auth(request):
    return render(request, 'auth.html')
