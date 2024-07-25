from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import PotatoPost, Item, Location
from .serializers import PotatoPostSerializer, ItemSerializer, LocationSerializer
from rest_framework.views import APIView


class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(itemLocation=location)
        return queryset


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class PotatoPostListCreate(generics.ListCreateAPIView):
    # getting all of the different PotatoPosts objects that exist
    queryset = PotatoPost.objects.all()
    # to return this data we use serializer_class
    serializer_class = PotatoPostSerializer

    def delete(self, request, *args, **kwargs):
        PotatoPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PotatoPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = PotatoPost.objects.all()
    serializer_class = PotatoPostSerializer
    lookup_field = "pk"


class PotatoPostList(APIView):
    def get(self, request, format=None):
        # Get the title from the query parameters (if none, default to empty string)
        title = request.query_params.get("title", "")

        if title:
            # Filter the queryset based on the title
            potato_posts = PotatoPost.objects.filter(title_icontains=title)
        else:
            # If no title is provided, return all potato posts
            potato_posts = PotatoPost.objects.all()

        serializer = PotatoPostSerializer(potato_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
