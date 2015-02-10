from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


    def save(self, commit=True):
        user = super(RegisterForm, self).save(False)
        if user:
            user.is_active = True
            user.save()


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        # fields = ("username", "password")