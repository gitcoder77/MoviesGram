from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from users.forms import RegistrationForm, UpdateForm
from users.models import Profile


# Create your views here.


def home(request):
    return render(request,'home.html')


def register(request, username=None):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} registered successfully.')
            return redirect('moviesgram:index')
    else:
        form = RegistrationForm(initial={'username': username}) if username else RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_page(request):
    if request.method =='POST':
        login_form = AuthenticationForm(request=request,data=request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data.get('username')
            password=login_form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, f'Congratulations { username } you are logged in...')
                return redirect('moviesgram:index')
            else:
                pass
    elif request.method == 'GET':
        login_form=AuthenticationForm()
    return render(request,'login.html',{'login_form':login_form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

# def dashboard(request):
#     profile_instance = Profile.objects.first()  # Assuming there's only one profile for now
#     if request.method == 'POST':
#         form = UpdateForm(request.POST, instance=profile_instance)
#         if form.is_valid():
#             form.save()
#     else:
#         form = UpdateForm(instance=profile_instance)
#     return render(request, 'dashboard.html', {'form': form})
#
#     def get_object(self):
#         return self.request.user
#

# class UserEdit(UpdateView):
#     model = Profile
#     template_name = 'dashboard.html'
#     fields = ['first_name','last_name','email']
#     success_url = 'dashboard.html'


class UserEditView(generic.UpdateView):
    form_class = UpdateForm
    template_name = 'dashboard.html'
    success_url = reverse_lazy('UserEditView')

    def get_object(self):
        return self.request.user
class PasswordChangeView(PasswordChangeView):
    from_class = PasswordChangeForm
    success_url = reverse_lazy('dashboard')

