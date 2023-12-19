from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import PostTag, Post, Tag

class PostTagView(ViewSet):
  def retrieve(self, request, pk):
    try:
      post_tag = PostTag.objects.get(pk=pk)
      serializer = PostTagSerializer(post_tag)
      return Response(serializer.data)
    except PostTag.DoesNotExist as ex:
      return Response({"message": ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
    post_tags = PostTag.objects.all()
    serializer = PostTagSerializer(post_tags, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    postId = Post.objects.get(pk=request.data['postId'])
    tagId = Tag.objects.get(pk=request.data['tagId'])
    post_tag = PostTag.objects.create(
      post=postId,
      tag=tagId
    )
    serializer = PostTagSerializer(post_tag)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    post_tag = PostTag.objects.get(pk=pk)
    postId = Post.objects.get(pk=request.data['postId'])
    tagId = Tag.objects.get(pk=request.data['tagId'])
    post_tag.post = postId
    post_tag.tag = tagId
    post_tag.save()
    serializer = PostTagSerializer(post_tag)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    post_tag = PostTag.objects.get(pk=pk)
    post_tag.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
class PostTagSerializer(serializers.ModelSerializer):
    
    class Meta:
      model = PostTag
      fields = ("id", "post", "tag")
