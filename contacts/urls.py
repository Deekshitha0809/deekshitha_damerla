# contacts/urls.py
from django.urls import path
from .views import ContactListView, ContactCreateView, ContactUpdateView, ContactDeleteView, ContactDetailView

urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    path('create/', ContactCreateView.as_view(), name='contact_create'),
    path('<int:pk>/update/', ContactUpdateView.as_view(), name='contact_update'),
    path('<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),
    path('<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
]
