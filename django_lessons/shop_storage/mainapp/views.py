from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse, reverse_lazy

from .models import StorageItem


class ItemList(ListView):
    model = StorageItem


class ItemCreate(CreateView):
    model = StorageItem
    fields = '__all__'
    success_url = reverse_lazy('index')

