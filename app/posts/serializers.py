from rest_framework import serializers

from app.companies.models import Company
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), write_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    company_country = serializers.CharField(source='company.country.name', read_only=True)
    company_region = serializers.CharField(source='company.region', read_only=True)
    position = serializers.CharField()
    reward = serializers.IntegerField()
    skill = serializers.CharField()

    class Meta:
        model = Post
        fields = (
            'id',
            'company',
            'company_name',
            'company_country',
            'company_region',
            'position',
            'reward',
            'skill',
        )


class PostDetailSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), write_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    company_country = serializers.CharField(source='company.country.name', read_only=True)
    company_region = serializers.CharField(source='company.region', read_only=True)
    position = serializers.CharField()
    reward = serializers.IntegerField()
    skill = serializers.CharField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    company_posts = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = Post
        fields = (
            'id',
            'company',
            'company_name',
            'company_country',
            'company_region',
            'position',
            'reward',
            'skill',
            'content',
            'created_at',
            'company_posts'
        )
