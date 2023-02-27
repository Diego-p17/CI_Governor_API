from .models         import TbPermission
from rest_framework  import viewsets, permissions
from .serializers    import PermissionSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = TbPermission.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = PermissionSerializer