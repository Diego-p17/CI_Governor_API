from .models         import TbDevice
from rest_framework  import viewsets, permissions
from .serializers    import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]
    serializer_class   = DeviceSerializer
    def get_queryset(self):
        queryset     = TbDevice.objects.all()

        isActive     = self.request.query_params.get('active')
        organization = self.request.query_params.get('organization')
        aplication   = self.request.query_params.get('app')

        if isActive is not None:
            queryset = queryset.filter(isActive= isActive)
        elif organization is not None:
            queryset = queryset.filter(organization= organization)
        elif aplication is not None:
            queryset = queryset.filter(aplication= aplication)
        elif organization is not None and isActive is not None:
            queryset = queryset.filter(organization= organization, isActive= isActive)
        elif organization is not None and isActive is not None and aplication is not None:
            queryset = queryset.filter(organization= organization, aplication= aplication, isActive= isActive)

        return queryset