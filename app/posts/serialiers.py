from rest_framework import serializers
from .models import Post
from app.companies.models import Company


class PostSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), write_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    company_country = serializers.CharField(source='company.country.name', read_only=True)
    company_region = serializers.CharField(source='company.region', read_only=True)
    position = serializers.CharField()
    reward = serializers.IntegerField()
    content = serializers.CharField()
    skill = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

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
            'content',
            'skill',
            'created_at'
        )
