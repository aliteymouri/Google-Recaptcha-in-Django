from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput({'class': "form-control form-control-lg", "placeholder": "Email"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput({'class': "form-control form-control-lg", "placeholder": "Password", }),
    )
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, error_messages={"required": 'Recaptcha is required'})
