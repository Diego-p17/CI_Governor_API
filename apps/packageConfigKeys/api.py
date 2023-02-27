from .models         import TbPackageConfigKeys
from rest_framework  import viewsets, permissions
from .serializers    import PackageConfigKeysSerializer


class PackageConfigKeysViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = PackageConfigKeysSerializer

    def get_queryset(self):
        queryset = TbPackageConfigKeys.objects.all()

        package = self.request.query_params.get('package')
        organization = self.request.query_params.get('org')
        zone    = self.request.query_params.get('zone')
        site    = self.request.query_params.get('site')
        key     = self.request.query_params.get('key')
        deviceType = self.request.query_params.get('deviceType')

        if package is not None:
            queryset = queryset.filter(packageConfig = package)
        if organization is not None:
            queryset = queryset.filter(organization = organization)
        if zone is not None:
            queryset = queryset.filter(zone = zone)
        if site is not None:
            queryset = queryset.filter(site = site)
        if deviceType is not None:
            queryset = queryset.filter(deviceType = deviceType)
        if key is not None:
            queryset = queryset.filter(keys = key)

        return queryset