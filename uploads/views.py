from rest_framework import generics

from .models import Upload
from .serializers import UploadSerializer

class UploadList(generics.ListCreateAPIView):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
    
    
class UploadDetail(generics.RetrieveUpdateAPIView):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer