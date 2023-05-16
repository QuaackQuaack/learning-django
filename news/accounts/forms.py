from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

#class CustomUserCreationForm(UserCreationForm):
#    class Meta(UserCreationForm): #to override the default fields by setting model
#        model = CustomUser
#        fields = UserCreationForm.Meta.fields + ("age",) #creating own fields for signup


#class CustomUserChangeForm(UserChangeForm):
#    class Meta:
#        model = CustomUser
#        fields = UserChangeForm.Meta.fields

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ( 'username', 'email', 'age')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email', 'age')
