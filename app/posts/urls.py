from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostListCreateView.as_view()),
    path('/<int:pk>', views.PostRetrieveUpdateDestroyView.as_view()),
]
