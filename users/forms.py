
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm

from mailing.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin,UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password',
                  'phone', 'country')

    def __init__(self, *args, **kwards):
        super().__init__(*args, **kwards)

        self.fields['password'].widget = forms.HiddenInput()


class UserForgotPasswordForm(StyleFormMixin, PasswordResetForm):
    """Запрос на восстановление пароля"""

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class UserSetNewPasswordForm(StyleFormMixin, SetPasswordForm):
    """Изменение пароля пользователя после подтверждения"""

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })
