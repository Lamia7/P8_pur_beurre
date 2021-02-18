from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, UserAuthenticationForm  # uses custom form instead of UserCreationForm
#from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def register(request):
    """View for the registration page"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Login automatically
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            #messages.success(request, f"Compte créé pour l'adresse email : {email} !")
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})  # form as a context to be used in template

@login_required  # only allows this page to logged_in users
def account(request):
    """View for the account page when a user is logged in"""
    return render(request, 'account.html')