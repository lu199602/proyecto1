from rest_framework import viewsets
from proyecto1.models import Productoo
from proyecto1.apis.serializer import ProductosSerializer

class productosViewSet(viewsets.ModelViewSet):
     queryset = Productoo.objects.all()
     serializer_class = ProductosSerializer