from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'date_of_birth']
