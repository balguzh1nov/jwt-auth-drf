from django.urls import path
from django.views.generic import TemplateView
from .views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration-success/', TemplateView.as_view(template_name='authentication/registration_success.html'), name='registration_success'),
    path('login-success/', TemplateView.as_view(template_name='authentication/login_success.html'), name='login_success'),
]
