from .models         import TbDevice
from rest_framework  import viewsets, permissions
from .serializers    import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = TbDevice.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = DeviceSerializer