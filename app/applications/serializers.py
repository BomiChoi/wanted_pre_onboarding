from rest_framework import serializers
from .models import Application
from app.users.models import User
from app.posts.models import Post


class ApplicationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Application
        fields = (
            'id',
            'user',
            'post',
            'created_at'
        )