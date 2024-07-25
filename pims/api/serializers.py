from rest_framework import serializers
from .models import PotatoPost, Item, Location


class PotatoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotatoPost
        # any field you want to be returned from your API
        # id will be automatically been added and return in the API so we do not have to specify it in the model
        fields = ["id", "title", "content", "published_date"]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')
