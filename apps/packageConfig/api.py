from .models         import TbPackageConfig
from rest_framework  import viewsets, permissions
from .serializers    import PackageConfigSerializer


class PackageConfigViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = PackageConfigSerializer

    def get_queryset(self):
        queryset = TbPackageConfig.objects.all()

        organization = self.request.query_params.get('org')
        namePackage  = self.request.query_params.get('name')

        if organization is not None:
            queryset = queryset.filter(organization = organization)
        elif namePackage is not None:
            queryset = queryset.filter(namePackage = namePackage)

        return queryset