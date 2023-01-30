from rest_framework import serializers
from .models import IntegerPair

class IntegerPairSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntegerPair
        fields = '__all__'