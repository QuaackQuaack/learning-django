from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [ #just to show which fields are listed
            'email','username','age','is_staff' ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields":("age",)}),) #actual edit garni
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields":("age",)}),)
#add_fieldssets are fields used when creating a user like in signup


admin.site.register(CustomUser, CustomUserAdmin)


