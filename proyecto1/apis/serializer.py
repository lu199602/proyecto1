from rest_framework import serializers
from proyecto1.models import Productoo

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Productoo
        fields = '__all__'