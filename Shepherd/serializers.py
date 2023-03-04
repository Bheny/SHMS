from rest_framework import serializers
from .models import Shepherd

class ShepherdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shepherd
        fields = '__all__'
