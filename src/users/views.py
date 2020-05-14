# users/views.py

from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from users.models import CustomUser, Student, Mentor
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from .forms import StudentSignUpForm, MentorSignUpForm

class ChooseRoleView(TemplateView):
    template_name = 'users/role.html'

    def home(request):
        if request.user.is_authenticated:
            if request.user.is_student:
                return redirect('TeamMap:team-add')
            else:
                return redirect('users:role')
        return render(request, 'home/home.html')


class StudentSignUpView(CreateView):
    model = CustomUser
    form_class = StudentSignUpForm
    template_name = 'users/signup.html'
    # success_url = reverse_lazy('login')

    # success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        user = super(StudentSignUpView, self).get_context_data(**kwargs)
        # user = super(UserCreationForm, self).save(commit=False)
        return user

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home:home')


class MentorSignUpView(CreateView):
    model = CustomUser
    form_class = MentorSignUpForm
    template_name = 'users/signup.html'
    # success_url = reverse_lazy('login')

    # success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'mentor'
        user = super(MentorSignUpView, self).get_context_data(**kwargs)
        return user
        # return super().get_context_data(**kwargs)
        # user = super(UserCreationForm, self).save(commit=False)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home:home')

class LoginView(TemplateView):
    template_name = 'registration/login.html'

class UserProfileView(TemplateView):
    template_name = 'users/user_profile.html'
