from django.contrib import admin
from .models import Disease, Symptom, CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomerUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'username','age', 'sex')
admin.site.register(CustomUser, CustomerUserAdmin)
admin.site.register(Disease)
admin.site.register(Symptom)
