from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApplicationCreateView.as_view()),
    path('/<int:pk>', views.ApplicationDestroyView.as_view()),
]
