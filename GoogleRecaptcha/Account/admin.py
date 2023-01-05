from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import ValidationError
from django.contrib import admin
from .models import User
from django import forms


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput({"placeholder": "password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput({"placeholder": "confirm_password"}))

    class Meta:
        model = User
        fields = ('email', 'fullname', 'phone', 'password')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError("passwords didn't match")
        elif len(password and confirm_password) < 8:
            raise ValidationError("")
        return confirm_password

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 11:
            raise ValidationError("please enter a valid phone")
        return phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="to change password <a href=\"../password/\">click here</a>"
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 11:
            raise ValidationError("please enter a valid phone")
        return phone

    class Meta:
        model = User
        fields = ('email', 'fullname', 'phone', 'password', 'bio', 'image', 'is_active', 'is_admin')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'fullname', 'phone', 'is_admin', 'is_active',)
    list_filter = ('is_active', 'is_admin')

    fieldsets = (
        ('information', {'fields': ('email', 'fullname', 'phone', 'image', 'bio', 'password',)}),
        ('permissions', {'fields': (
            'is_active', 'is_admin', 'is_superuser', 'groups', 'user_permissions')}
         ),
    )

    add_fieldsets = (
        (None, {'fields': (
            'email', 'fullname', 'phone', 'password', 'confirm_password')}
         ),
    )

    search_fields = ('phone', 'email', 'fullname')
    ordering = ('-date_joined',)
    filter_horizontal = ('groups', 'user_permissions')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disable = True
        return form


admin.site.register(User, UserAdmin)
