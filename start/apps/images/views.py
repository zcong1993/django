from rest_framework import response, status, viewsets

from .models import Image
from .serializers import ImageSerializer


# Create your views here.
class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.filter(is_deleted=False)
    serializer_class = ImageSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.soft_delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
