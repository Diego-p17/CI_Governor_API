from .models         import TbZone
from rest_framework  import viewsets, permissions
from .serializers    import ZoneSerializer


class ZonenViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class   = ZoneSerializer
    
    def get_queryset(self):
        queryset     = TbZone.objects.all()
        
        site = self.request.query_params.get('site')
        
        if site is not None:
            queryset = queryset.filter(site=site)
        return queryset