from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm, PostForm
from .models import Profile, Post


class LoginView(LoginView):
    template_name = 'blog/login.html'

class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')
    form_class = RegistrationForm
    success_message = "Your profile was created successfully"

from django.views import View
from django.contrib.auth import logout

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

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
        return self.request.user

class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = "blog/profile_update.html"
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        # Check if the request method is POST
        if self.request.method == 'POST':
            profile = form.save()
            user_form = UserUpdateForm(self.request.POST, instance=self.request.user)
            if user_form.is_valid():
                user_form.save()

            return redirect(self.success_url)
        else:
            # You can return some other response here if it's not a POST request
            return super().form_invalid(form)


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name='posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user