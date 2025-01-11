from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password1= forms.CharField(label='Password', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    profile_picture=forms.ImageField(required=False, label='Profile')
    bio = forms.TextInput ()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_picture']
        
    def clean_password2(self):
        password1= self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields must match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)

        # Hash the password before saving
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user
    
class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
