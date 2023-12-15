
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Comment, rare_user

class CommentView(ViewSet):
  """Rare Comment View"""
  
  def retrieve(self, request, pk):
    """Handle GET request for a single comment
    
    Returns -> Response -- JSON serialized comment with status of 200"""
    
    try:
      comment = Comment.objects.get(pk=pk)
      serializer = CommentSerializer(comment)
      return Response(serializer.data)
    except comment.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    """Handle GET requests for all comments
    
    Returns -> Response -- JSON serialized list of comments with status 200"""
    
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handle comment operations for comments
    
    Returns -> JSON serialized comment instance with a status of 201"""
    author_id = rare_user.objects.get(pk=request.data['id'])
    post_id = Post.objects.get(pk=request.data['id'])
    
    comment = comment.objects.create(
      author_id = author_id,
      post_id = post_id,
      content = request.data['content'],
      created_on = request.data['created_on'],
    )
    
    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT request for a comment
    
    Returns -> -- JSON serialized comment with 200 status"""
    
    comment = comment.objects.get(pk=pk)
    author_id = rare_user.objects.get(pk=request.data['id'])
    comment.author_id = author_id
    post_id = Post.objects.get(pk=request.data['id'])
    comment.post_id = post_id
    comment.content = request.data['content']
    comment.created_on = request.data['created_on']
    
    comment.save()
    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    """Handles Delete requests for a comment
    
    Returns -> Empty body with a 204 status"""
    
    comment = comment.objects.get(pk=pk)
    comment.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
      
      
class CommentSerializer(serializers.ModelSerializer):
  """JSON serializer for comments"""
  class Meta:
    model = Comment
    fields = ('id', 'author_id', 'post_id', 'content', 'created_on')