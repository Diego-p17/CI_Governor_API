from .models         import TbLocation
from rest_framework  import viewsets, permissions
from .serializers    import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = TbLocation.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = LocationSerializer

    def get_queryset(self):
        queryset = TbLocation.objects.all()

        device   = self.request.query_params.get('device')
        site     = self.request.query_params.get('site')
        isActive = self.request.query_params.get('isActive')


        if device is not None:
            queryset = queryset.filter(device = device)
        elif site is not None:
            queryset = queryset.filter(site = site)
        elif device is not None and isActive is not None:
            queryset = queryset.filter(device = device, isActive = isActive)

        return  queryset