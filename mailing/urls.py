from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import MailingSettingsListView, MailingSettingsCreateView, MailingSettingsDetailView, \
    MailingSettingsUpdateView, MailingSettingsDeleteView, ClientCreateView, ClientListView, ClientDetailView, \
    ClientUpdateView, ClientDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path('create_mailing/', MailingSettingsCreateView.as_view(), name='create_mailing'),
    path('', MailingSettingsListView.as_view(), name='mailingsettings_list'),
    path('view_mailing/<int:pk>/', MailingSettingsDetailView.as_view(), name='mailing_detail'),
    path('edit_mailing/<int:pk>/', MailingSettingsUpdateView.as_view(), name='update_mailing'),
    path('delete_mailing/<int:pk>/', MailingSettingsDeleteView.as_view(), name='delete_mailing'),
    path('client/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/view/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/edit/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
]