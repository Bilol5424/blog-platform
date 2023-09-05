from rest_framework import serializers
from ..models import Post
from user.serilizers import UserShortDetailSerializer
from categories.serializers import CategorySerializer



class PostSerializer(serializers.ModelSerializer):
    creator = UserShortDetailSerializer()
    category = CategorySerializer()
    likesCount = serializers.SerializerMethodField()
    dislikesCount = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'creator', 'publish_date', 'last_updated', 'category', 'views', 'image', 'video', 'gif', 'is_published','likesCount', 'dislikesCount']

class PostCreateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'image', 'video', 'gif')