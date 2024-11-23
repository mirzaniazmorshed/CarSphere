from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, SetPasswordForm
from django import forms


class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    def __str__(self) -> str:
        return self.username
    
   

class UserLoginForm(AuthenticationForm):
    class Meta: 
        model = User
        fields = '__all__'


class UserUpdateForm(UserChangeForm):
    password1 = None
    password2 = None
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UserPassChangeForm(SetPasswordForm):
    class Meta:
        model = User
        fields = '__all__'