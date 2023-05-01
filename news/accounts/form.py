from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomerUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):#to isolate attribute realted to metadata
        model = CustomUser #to generate fields specific to this model, which is in line 9
        fields = UserCreationForm.Meta.fields + ('age',) #field from this use in model 
        
class CustomerUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm): #to understand you can think like meta hold data about form
        models = CustomUser
        fields = UserChangeForm.Meta.fields #holds default fields like fname,lname,email.
