"""View module for handling requests for posts"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, User, Category, Tag, PostTag

class PostView(ViewSet):
  """Rare Post View"""
  
  def retrieve(self, request, pk):
    """Handle GET request for a single post
    
    Returns -> Response -- JSON serialized post with status of 200"""
    
    try:
      post = Post.objects.get(pk=pk)
      # tags = PostTag.objects.filter(post = post.pk)
      
      # tag_list = []
      # for e in tags:
      #   tag_list.append(e.tag_id)
      
      post.tags = Tag.objects.filter(pk__in = tag_list)
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
    category = Category.objects.get(pk=request.data['categoryId'])
    user = User.objects.get(uid=request.data['uid'])
    
    post = Post.objects.create(
      user = user,
      category = category,
      title = request.data['title'],
      publication_date = request.data['publicationDate'],
      image_url = request.data['imageUrl'],
      content = request.data['content'],
      approved = request.data['approved'],
    )
    
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT request for a post
    
    Returns -> -- JSON serialized post with 200 status"""
    
    post = Post.objects.get(pk=pk)
    category = Category.objects.get(pk=request.data['categoryId'])
    user = User.objects.get(uid=request.data['uid'])
    post.user = user
    post.category = category
    post.title = request.data['title']
    post.publication_date = request.data['publicationDate']
    post.content = request.data['content']
    post.approved = request.data['approved']
    
    post.save()
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    """Handles Delete requests for a post
    
    Returns -> Empty body with a 204 status"""
    
    post = Post.objects.get(pk=pk)
    post.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ("id", "label")      
      
class PostSerializer(serializers.ModelSerializer):
  """JSON serializer for posts"""
  
  # tags = TagSerializer(many=True)
  class Meta:
    model = Post
    fields = ('id', 'rare_user', 'category', 'title', 'publication_date', 'image_url', 'content', 'approved')
