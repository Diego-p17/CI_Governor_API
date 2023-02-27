from .models         import TbSetting
from rest_framework  import viewsets, permissions
from .serializers    import SettingSerializer


class SettingViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = SettingSerializer
    
    def get_queryset(self):
        queryset = TbSetting.objects.all()

        device = self.request.query_params.get('device')

        if device is not None: queryset = queryset.filter(device = device)

        return queryset