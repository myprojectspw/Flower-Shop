from django.urls import path
from .views import FlowerListView, FlowerDetailView

urlpatterns = [
    path('', FlowerListView.as_view()),
    path('<pk>', FlowerDetailView.as_view()),
]