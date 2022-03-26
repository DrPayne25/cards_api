from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'user', 'name', 'description', 'created_at', 'updated_at')
    model = Card
