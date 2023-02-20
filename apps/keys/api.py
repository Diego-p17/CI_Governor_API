from .models         import TbKey
from rest_framework  import viewsets, permissions
from .serializers    import KeysSerializer


class KeysViewSet(viewsets.ModelViewSet):
    queryset = TbKey.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = KeysSerializer