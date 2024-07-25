from django.urls import path
from . import views

urlpatterns = [
    path("potatoposts/", views.PotatoPostListCreate.as_view(),
         name="potatopost-view-create"),
    path("potatoposts/<int:pk>/", views.PotatoPostRetrieveUpdateDestory.as_view(),
         name="potatopost-view-update"),

    path('item', views.ItemList.as_view()),
    path('item/<int:pk>', views.ItemDetail.as_view()),
    path('location', views.LocationList.as_view()),
    path('location/<int:pk>', views.LocationDetail.as_view()),

]
