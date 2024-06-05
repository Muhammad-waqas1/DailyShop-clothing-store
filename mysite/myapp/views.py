from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from .models import User

def index(request):
    return render(request, 'index.html')

def account(request):
    return render(request, 'account.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def wishlist(request):
    return render(request, 'wishlist.html')
def error_404(request, exception):
    return render(request, '404.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Process form data and authenticate user
            # Example: user = authenticate(request, username=form.cleaned_data['username_or_email'], password=form.cleaned_data['password'])
            # If authentication is successful, you can redirect user to another page
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save user registration data to the database
            form.save()
            # Redirect user to login page or another page
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})