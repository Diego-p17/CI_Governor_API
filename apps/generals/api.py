from .models         import *
from .serializers    import *
from rest_framework  import viewsets,permissions


class CountryViewSet(viewsets.ModelViewSet):
    queryset = TbCountry.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = CountrySerializer
    
class CityViewSet(viewsets.ModelViewSet):
    queryset = TbCity.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = CitySerializer

class DeviceTypeViewSet(viewsets.ModelViewSet):
    queryset = TbDeviceType.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = DeviceTypeSerializer
    
class HwPlatformViewSet(viewsets.ModelViewSet):
    queryset = TbHwPlatform.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = HwPlatformSerializer

class OsViewSet(viewsets.ModelViewSet):
    queryset = TbOs.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = OsSerializer
    
class TokenTypeViewSet(viewsets.ModelViewSet):
    queryset = TbTokenType.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = TokenTypeSerializer

class SettingsTypeViewSet(viewsets.ModelViewSet):
    queryset = TbSettingType.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = SettingTypeSerializer
    
