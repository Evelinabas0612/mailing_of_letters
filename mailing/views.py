from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import MailingSettingsForm, ClientForm
from mailing.models import MailingSettings, Client
from mailing.services.services import get_cached_blog


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        new_user = form.save()
        new_user.save()
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')

    def form_valid(self, form):
        new_user = form.save()
        new_user.save()
        form.instance.user = self.request.user
        return super().form_valid(form)


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


class MailingSettingsListView(ListView):
    model = MailingSettings

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        count_active_mailing = MailingSettings.objects.filter(status=MailingSettings.STATUS_STARTED).count()
        clients_count = Client.objects.values('email').distinct().count()
        context['blog_list'] = get_cached_blog()
        context['count_active_mailing'] = count_active_mailing
        context['clients_count'] = clients_count
        return context


class MailingSettingsDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = MailingSettings

    def test_func(self):
        return self.request.user

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            self.object.user = self.request.user
            self.object.save()

        return super().form_valid(form)


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:mailingsettings_list')

    def test_func(self):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super(MailingSettingsCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MailingSettingsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:mailingsettings_list')

    def test_func(self):
        return self.request.user.is_staff or self.get_object().user == self.request.user


class MailingSettingsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailing:mailingsettings_list')

    def test_func(self):
        return self.request.user.is_superuser or self.get_object().user == self.request.user
