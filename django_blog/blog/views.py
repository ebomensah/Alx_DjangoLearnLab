from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm, PostForm, CommentForm
from .models import Profile, Post, Comment, Tag


from .models import Post, Comment
from .forms import CommentForm

@login_required
def CommentCreateView(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post.id)
        else:
            return render(request, 'blog/post_detail.html',  {'post': post, 'form': form, 'comments': post.comments.all()})
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'comments': post.comments.all()})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


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
    context_object_name = 'user'

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

from django.db.models import Q

def search_posts(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
    ).distinct()
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})


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

class PostsByTagListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        tag= get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags=tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_slug'] = self.kwargs.get('tag_slug')
        context['tag_slug'] = Tag.objects.get(slug=self.kwargs.get('tag_slug')).name
        return context
