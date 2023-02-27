from .models         import TbKey
from rest_framework  import viewsets, permissions
from .serializers    import KeysSerializer


class KeysViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = KeysSerializer

    def get_queryset(self):
        queryset     = TbKey.objects.all()

        organization = self.request.query_params.get('org')
        deviceType   = self.request.query_params.get('type')

        if organization is not None:
            queryset = queryset.filter(organization = organization)
        elif deviceType is not None:
            queryset = queryset.filter(deviceType = deviceType)
        elif organization is not None and deviceType is not None:
            queryset = queryset.filter(organization = organization, deviceType = deviceType)

        return queryset