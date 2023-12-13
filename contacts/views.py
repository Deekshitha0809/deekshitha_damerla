# contacts/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Contact

class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'

class ContactCreateView(CreateView):
    model = Contact
    template_name = 'contact_form.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('contact_list')

class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'contact_form.html'
    fields = ['name', 'email']
    success_url = reverse_lazy('contact_list')

class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'contact_confirm_delete.html'
    success_url = reverse_lazy('contact_list')

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact_detail.html'
