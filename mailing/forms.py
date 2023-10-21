from django import forms

from mailing.models import Client, MailingSettings


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    class Meta:
        model = Client
        fields = ('name', 'email', 'comment',)


class MailingSettingsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MailingSettingsForm, self).__init__(*args, **kwargs)


        self.fields['clients'].queryset = Client.objects.filter(user=user)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    class Meta:
        model = MailingSettings
        fields = ('topic_mail', 'body_mail', 'clients',
                  'period', 'time', 'day', 'status',)
