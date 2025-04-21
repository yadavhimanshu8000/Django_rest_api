from rest_framework import serializers
from myapp.models import User,Post,Follows

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
             
class postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        
class followsserializer(serializers.ModelSerializer):
    class Meta:
        model = Follows
        fields = '__all__'
        
        
        
        
        