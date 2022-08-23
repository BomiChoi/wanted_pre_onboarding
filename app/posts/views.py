from django.db.models import Q
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Post
from .serializers import PostSerializer


# Create your views here.
class PostListCreateView(ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        search = self.request.GET.get('search', '')

        queryset = Post.objects.all()
        if search:
            queryset = queryset.filter(
                Q(company__name__icontains=search) |
                Q(company__country__name__icontains=search) |
                Q(company__region__icontains=search) |
                Q(position__icontains=search) |
                Q(content__icontains=search) |
                Q(skill__icontains=search)
            )
        return queryset


class PostRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
