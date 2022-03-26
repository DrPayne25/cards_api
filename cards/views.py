from django.shortcuts import render
from rest_framework import generics
from .models import Card
from .serializer import CardSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class CardList(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Card.objects.all()
  serializer_class = CardSerializer

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsAuthenticated,)
  queryset = Card.objects.all()
  serializer_class = CardSerializer
