from rest_framework import serializers
from .models import PotatoPost, Item, Location
from rest_framework import generics


class PotatoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotatoPost
        # any field you want to be returned from your API
        # id will be automatically been added and return in the API so we do not have to specify it in the model
        fields = ["id", "title", "content", "published_date"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')

# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = ('__all__')


# class ItemSerializer(serializers.ModelSerializer):
#     # Use LocationSerializer to nest the object
#     itemLocation = LocationSerializer(required=False)

#     class Meta:
#         model = Item
#         fields = ['itemName', 'date_added', 'itemLocation']


class ItemSerializer(serializers.ModelSerializer):
    itemLocation = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all())

    class Meta:
        model = Item
        fields = ['id', 'itemName', 'date_added', 'itemLocation']


class ItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
