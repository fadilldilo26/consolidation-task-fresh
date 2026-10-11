from django.contrib.auth.forms import UserCreationForm
from news.models import CustomUser

"""
Custom user creation form for handling user registration.
"""
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'password1', 'password2')
