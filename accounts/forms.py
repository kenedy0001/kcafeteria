from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()  
        fields = ['phone']

class PayForm(forms.Form):
   
    PhoneNumber = forms.IntegerField(
                     help_text = "Enter your phone number"
                     )
    Amount = forms.IntegerField(
                     help_text = "Enter Amount Payable"
                     )