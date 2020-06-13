from django import forms
from .models import Profile
from django.contrib.auth.models import User

# To accept the input from users we used forms which enables us to input 
# This Form is used to update the user profile and user informations 
class userupdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','email']


class profielupdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']
