"""View module for handling requests for posts"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post

class PostView(ViewSet):
  """Rare Post View"""
  
  def retrieve(self, request, pk):
    """Handle GET request for a single post
    
    Returns -> Response -- JSON serialized post with status of 200"""
    
    try:
      post = Post.objects.get(pk=pk)
      serializer = PostSerializer(post)
      return Response(serializer.data)
    except Post.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handle GET requests for all posts
    
    Returns -> Response -- JSON serialized list of songs with status 200"""
    
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle POST operations for posts
    
    Returns -> JSON serialized post instance with a status of 201"""
    category = Category.objects.get(pk=request.data['category'])
    
    post = Post.objects.create(
      rare_user = request.data['uid'],
      category = category,
      title = request.data['title'],
      publication_date = request.data['publication_date'],
      image_url = request.data['image_url'],
      content = request.data['content'],
      approved = request.data['approved'],
    )
    
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT request for a post
    
    Returns -> -- JSON serialized post with 200 status"""
    
    post = Post.objects.get(pk=pk)
    category = Category.objects.get(pk=request.data['category'])
    post.rare_user = request.data['uid']
    post.category = category
    post.title = request.data['title']
    post.publication_date = request.data['publication_date']
    post.content = request.data['content']
    post.approved = request.data['approved']
    
    post.save()
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    """Handles Delete requests for a post
    
    Returns -> EMpy body with a 204 status"""
    
    post = Post.objects.get(pk=pk)
    post.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
      
      
class PostSerializer(serializers.ModelSerializer):
  """JSON serializer for posts"""
  class Meta:
    model = Post
    fields = ('id', 'rare_user', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved')
