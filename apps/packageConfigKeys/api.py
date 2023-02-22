from .models         import TbPackageConfigKeys
from rest_framework  import viewsets, permissions
from .serializers    import PackageConfigKeysSerializer


class PackageConfigKeysViewSet(viewsets.ModelViewSet):
    queryset = TbPackageConfigKeys.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = PackageConfigKeysSerializer