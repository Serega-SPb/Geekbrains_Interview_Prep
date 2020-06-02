from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import StorageItem
from .serializers import StorageItemSerializer


class ItemList(ListView):
    model = StorageItem


class ItemCreate(CreateView):
    model = StorageItem
    fields = '__all__'
    success_url = reverse_lazy('index')


# API

class StorageItemView(viewsets.ModelViewSet):
    serializer_class = StorageItemSerializer
    queryset = StorageItem.objects.all()