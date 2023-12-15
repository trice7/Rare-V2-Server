"""View module for handling requests for Category"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Category

class CategoryView(ViewSet):
    """Rare Category View"""

    def list(self, request):
        """Handle GET requests for all categories
        
        Returns -> Response -- JSON serialized list of songs with status 200"""

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for posts"""

    class Meta:
        model = Category
        fields = ('id', 'label')
