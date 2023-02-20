from .models         import TbOrganization
from rest_framework  import viewsets, permissions
from .serializers    import OrganizationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = TbOrganization.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = OrganizationSerializer
    
    