from django.shortcuts import render, redirect
from .forms import LoginForm
from .forms import UserForm
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
def Error_404(request):
    return render(request, '404.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']

            # Check if the input is an email
            if '@' in username_or_email:
                try:
                    user = User.objects.get(email=username_or_email)
                except User.DoesNotExist:
                    messages.error(request, 'Email not found. Please try again or Register.')
                    return redirect('account')
            else:
                user = authenticate(request, username=username_or_email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have been logged in successfully.')
                return redirect('index')
            else:
                messages.error(request, 'Invalid Email or Password. Please try again.')
        else:
            messages.error(request, 'Form is invalid. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'account.html', {'form': form})



def Sign_in_FormSubmit(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully registered.')
            return redirect('index')
        else:
            # Form is invalid, display errors
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserForm()
    return render(request, 'account.html')