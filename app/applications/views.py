from rest_framework.generics import CreateAPIView, DestroyAPIView
from .models import Application
from .serializers import ApplicationSerializer


# Create your views here.
class ApplicationCreateView(CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationDestroyView(DestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
