from django.urls import path, include
from rest_framework import routers, viewsets, serializers
from .models import productModels

class productserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=productModels
        fields=['tittle', 'price', 'description']

class product(viewsets.ModelViewSet):
    queryset=productModels.objects.all()
    serializer_class=productserializer

router=routers.DefaultRouter()
router.register(r'product',product)

urlpatterns = [
              path('',include(router.urls)),
              path('api/',include('rest_framework.urls',namespace='rest_framework'))     
             ]