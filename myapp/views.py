from django.shortcuts import render
from myapp.models import User,Post, Follows
from myapp.serializers import userserializer,postserializer, followsserializer
from rest_framework import viewsets

# Create your views here.

class userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializer
    
    
class postviewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = postserializer
    
class followsviewset(viewsets.ModelViewSet):
    queryset = Follows.objects.all()
    serializer_class = followsserializer
    
    
    