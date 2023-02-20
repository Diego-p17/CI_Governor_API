from .models                    import TbSite
from rest_framework             import viewsets, permissions
from .serializers               import SiteSerializer



class SiteViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]
    serializer_class   = SiteSerializer
    
    def get_queryset(self):
        queryset     = TbSite.objects.all()
        
        organization = self.request.query_params.get('org')
        isActive = self.request.query_params.get('active')
        
        if organization is not None:
            if isActive is not None:
                queryset = queryset.filter(organization=organization, isActive= isActive)
            else:
                queryset = queryset.filter(organization=organization)
        return queryset

    