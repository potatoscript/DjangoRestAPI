from django.urls import path
from . import views

urlpatterns = [
    path("potatoposts/", views.PotatoPostListCreate.as_view(),
         name="potatopost-view-create"),
    path("potatoposts/<int:pk>/", views.PotatoPostRetrieveUpdateDestory.as_view(),
         name="potatopost-view-update"),
]
