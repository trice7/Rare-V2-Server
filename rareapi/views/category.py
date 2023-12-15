"""View module for handling requests for Category"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Category

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for posts"""
    
    class Meta:
        model = Category
        fields = ('id', 'label')
