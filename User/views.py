from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserCreationForm
from django.urls import reverse_lazy


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
