from .models         import *
from .serializers    import *
from rest_framework  import viewsets,permissions


class CountryViewSet(viewsets.ModelViewSet):
    queryset = TbCountry.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = CountrySerializer
    
class CityViewSet(viewsets.ModelViewSet):
    queryset = TbCity.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = CitySerializer

class DeviceTypeViewSet(viewsets.ModelViewSet):
    queryset = TbDeviceType.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = DeviceTypeSerializer
    
class HwPlatformViewSet(viewsets.ModelViewSet):
    queryset = TbHwPlatform.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = HwPlatformSerializer

class OsViewSet(viewsets.ModelViewSet):
    queryset = TbOs.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = OsSerializer
    
class TokenTypeViewSet(viewsets.ModelViewSet):
    queryset = TbTokenType.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = TokenTypeSerializer

class SettingsTypeViewSet(viewsets.ModelViewSet):
    queryset = TbSettingType.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = SettingTypeSerializer
    
class LevelKeysViewSet(viewsets.ModelViewSet):
    queryset = TbLevelKeys.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = LevelKeysSerializer