from rest_framework import generics
from .models import IntegerPair
from .serializers import IntegerPairSerializer

class IntegerPairList(generics.ListCreateAPIView):
    queryset = IntegerPair.objects.all()
    serializer_class = IntegerPairSerializer