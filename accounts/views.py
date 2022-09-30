from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, PasswordChangeView
from accounts.models import Profile
from accounts.forms import UpdateUserForm, UpdateProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import mixins

class Login(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('shop:book_list')

class RegisterUserView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/register.html'

class ProfileUpdateView(mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'accounts/profile/profile.html'
    model  = User
    form_class = UpdateUserForm
    def get_success_url(self):
        return reverse_lazy('accounts:profile', args = [self.kwargs['pk']])

class ProfileUpdatePictureView(mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'accounts/profile/update.html'
    model  = Profile
    form_class = UpdateProfileForm
    def get_success_url(self):
        return reverse_lazy('accounts:profile', args = [self.kwargs['pk']])

class UpdatePassword(mixins.LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/profile/password_change_form.html'
    def get_success_url(self):
        return reverse_lazy('accounts:profile', args = [self.kwargs['pk']])
