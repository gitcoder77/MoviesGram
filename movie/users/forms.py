from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50,required=True,help_text="Required")
    last_name = forms.CharField(max_length=50,required=True,help_text="Required")
    email = forms.EmailField(max_length=250,required=True,help_text="Enter a valid email address")
    username = forms.CharField(max_length=50,required=True,help_text="Required")
    class Meta:
        model=User
        fields = ('first_name','last_name','username','email','password1','password2')
        widget ={
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }


class UpdateForm(UserChangeForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    date_joined = forms.EmailField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.EmailField(max_length=250, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # is_superuser = forms.EmailField(max_length=250, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_staff = forms.EmailField(max_length=250, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_active = forms.EmailField(max_length=250, widget=forms.CheckboxInput(attrs={'class':'form-check'}))


    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','date_joined','last_login')



