from django.shortcuts import render
from rest_framework import generics
from .models import Card
from .serializer import CardSerializer
from .permissions import IsOwnerOrReadOnly

class CardList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Card.objects.all()
  serializer_class = CardSerializer

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Card.objects.all()
  serializer_class = CardSerializer
