from django.urls import path, include

urlpatterns = [
    path('posts', include('app.posts.urls')),
    path('applications', include('app.applications.urls'))
]
