from rest_framework.generics import ListAPIView, RetrieveAPIView

from flowers.models import Flower
from .serializers import FlowerSerializer

class FlowerListView(ListAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer

class FlowerDetailView(RetrieveAPIView):
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer