# contacts/models.py
from django.db import models
from django.urls import reverse

class Contact(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact_detail.html', args=[str(self.id)])
