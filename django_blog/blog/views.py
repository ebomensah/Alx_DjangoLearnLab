from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile 

class LoginView(LoginView):
    template_name = 'blog/login.html'

class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')
    form_class = RegistrationForm
    success_message = "Your profile was created successfully"

class LogoutView(LogoutView):
    next_page = 'login'

class ProfileView(DetailView):
    model = User
    template_name = 'blog/profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "blog/user_update.html"  
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        user = self.request.user
        return user

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['user_form'] = self.get_form()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        user_form = self.get_form()

        if user_form.is_valid():
            user_form.save()
            return redirect(self.success_url)

        context = self.get_context_data()
        context['user_form'] = user_form
        return self.render_to_response(context)


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = "blog/profile_update.html"
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()
        context['user_form'] = UserUpdateForm(instance=request.user)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        profile_form = self.get_form()

        if profile_form.is_valid():
            self.object = profile_form.save()
            
            user_form = UserUpdateForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()

            return redirect(self.success_url)

        context = self.get_context_data()
        context['user_form'] = UserUpdateForm(instance=request.user)
        context['profile_form'] = profile_form
        return self.render_to_response(context)
   

# Create your views here.
