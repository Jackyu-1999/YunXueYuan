# users/forms.py

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    '''登录验证表单'''

    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):
    '''注册验证表单'''

    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    # 验证码
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})

