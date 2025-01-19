from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Comment


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_picture']

        def save(self, commit=True):
            user=super().save(commit=False)
            if commit:
                user.save()
                Profile.objects.create(
                    user=user,
                    profile_picture=self.cleaned_data.get('profile_picture')
                )
            return user 

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add a comment...'}),
        }
        labels = {'content': ''}