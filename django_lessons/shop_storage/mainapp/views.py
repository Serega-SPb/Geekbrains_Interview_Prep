from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, CreateView
from django.views.generic.edit import BaseCreateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import StorageItem
from .serializers import StorageItemSerializer


class AddItemMixin(BaseCreateView):
    model = StorageItem
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modal_form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        form_cls = self.get_form_class()
        form_ins = form_cls(request.POST, request.FILES)
        if form_ins.is_valid():
            form_ins.save()
            return JsonResponse({'result': 'OK'})
        else:
            return JsonResponse({'result': 'INVALID DATA'})


class ItemList(AddItemMixin, ListView):
    model = StorageItem


class ItemCreate(CreateView):
    model = StorageItem
    fields = '__all__'
    success_url = reverse_lazy('index')


# API


class StorageItemView(viewsets.ModelViewSet):
    serializer_class = StorageItemSerializer
    queryset = StorageItem.objects.all()
