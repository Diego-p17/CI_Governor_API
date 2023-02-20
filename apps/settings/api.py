from .models         import TbSetting
from rest_framework  import viewsets, permissions
from .serializers    import SettingSerializer


class SettingViewSet(viewsets.ModelViewSet):
    queryset = TbSetting.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = SettingSerializer