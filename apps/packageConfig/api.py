from .models         import TbPackageConfig
from rest_framework  import viewsets, permissions
from .serializers    import PackageConfigSerializer


class PackageConfigViewSet(viewsets.ModelViewSet):
    queryset = TbPackageConfig.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = PackageConfigSerializer