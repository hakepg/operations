from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Sample
from .serializers import sampleSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class sampleView(ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = sampleSerializer

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World..! I love Python'}
        return Response(content)