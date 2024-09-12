from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from moviesgram.models import Movie
from users.forms import RegistrationForm, UpdateForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request, username=None):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User {username} registered successfully.')
            return redirect('users:login')
    else:
        form = RegistrationForm(initial={'username': username}) if username else RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Congratulations {username} you are logged in...')
                request.session['username'] = username
                return redirect('moviesgram:index')
            else:
                pass
    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})


@login_required
def logout_view(request):
    # Clear the session data
    request.session.flush()

    # Logout the user
    logout(request)

    # Redirect to the home page or login page
    return redirect('home')  # Replace 'home' with your desired redirect URL name


@login_required
def DashBoard(request):
    user_name = request.session.get('username', '')
    print('USERNAME:', user_name)
    
    try:
        user = User.objects.get(username=user_name)
    except User.DoesNotExist:
        # Handle case where the user does not exist
        user = None

    if user:
        form = UpdateForm(request.POST or None, instance=user)
        user_movies = Movie.objects.filter(added_by=user_name)
        print("USER MOVIES", user_movies)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('users:dashboard')  # Ensure this is the correct URL name

        context = {'form': form, 'user_movies': user_movies, 'user': user}
    else:
        print("Please Register on our website")

    return render(request, 'dashboard.html', context)

class PasswordChangeView(PasswordChangeView):
    from_class = PasswordChangeForm
    success_url = reverse_lazy('dashboard')
