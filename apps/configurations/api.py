from .models         import TbConfiguration
from rest_framework  import viewsets, permissions
from .serializers    import ConfigurationSerializer


class ConfigurationnViewSet(viewsets.ModelViewSet):
    queryset = TbConfiguration.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = ConfigurationSerializer