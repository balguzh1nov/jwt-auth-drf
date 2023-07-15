from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from .forms import UserLoginForm
from .forms import UserRegistrationForm


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'authentication/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('login_success')
            else:
                form.add_error(None, 'Invalid email or password')

        return render(request, 'authentication/login.html', {'form': form})

class UserRegistrationView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'authentication/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('registration_success')
        return render(request, 'authentication/register.html', {'form': form})