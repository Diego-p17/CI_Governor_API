from .models         import TbLocation
from rest_framework  import viewsets, permissions
from .serializers    import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = TbLocation.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = LocationSerializer