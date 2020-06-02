from rest_framework import serializers

from .models import StorageItem


class StorageItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageItem
        fields = '__all__'
