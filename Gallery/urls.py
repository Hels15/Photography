from django.urls import path

from .views import GalleryView,PhotoDetailsView
urlpatterns = [
    path('', GalleryView.as_view()),
    path('<str:slug>/',PhotoDetailsView.as_view())
]



