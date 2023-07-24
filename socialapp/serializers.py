from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Relationship

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = ['follower', 'following']

    def validate(self, data):
        follower = data['follower']
        following = data['following']

        existing_relationship = Relationship.objects.filter(follower=follower, following=following).first()

        if existing_relationship:
            raise serializers.ValidationError('Relationship already exists.')

        return data