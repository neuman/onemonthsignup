from django.shortcuts import render
from django.views.generic.base import TemplateView

class SignupView(TemplateView):
    template_name = 'signup.html'