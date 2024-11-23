from typing import Any
from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

# user signup view
class UserSignUpView(CreateView):
    model = User
    form_class  = forms.UserSignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('user_login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'User signup successfully created!')
        return response 

#user login view
class UserLoginView(LoginView):
    model = User
    form_class = forms.AuthenticationForm
    template_name = 'login.html'
    next_page = 'user_profile'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'You are already logged in.')
            return redirect('user_profile') 

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your\'e logged in!!')
        return response 

# user profile view
@method_decorator(login_required, name='dispatch')
class UserProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cur_user'] = self.request.user
        context['carts'] = self.request.session.get('carts',[])
        for attr, value in self.request.user.__dict__.items():
            print(f"{attr}: {value}")
        return context


# user logged out view
@method_decorator(login_required, name='dispatch')
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('user_login')
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Your\'e logged out!!.")
        return super().dispatch(request, *args, **kwargs)

# user profile update view

@method_decorator(login_required, name='dispatch')
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = forms.UserUpdateForm
    pk_url_kwarg = 'id'
    template_name = 'edit_profile.html'  # your template name
    success_url = reverse_lazy('user_profile')  # adjust to your success URL


# user password reset
@method_decorator(login_required, name='dispatch')
class UserPasswordUpdateView(LoginRequiredMixin,FormView):
    model = User
    form_class = forms.UserPassChangeForm
    template_name = 'edit_pass.html'  # your template name
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('user_login')  # adjust to your success URL
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the current user to the form
        return kwargs

    def form_valid(self, form):
        form.save()  # Save the new password
        messages.success(self.request, 'Password reset successfull. Please login again!')
        return super().form_valid(form)
