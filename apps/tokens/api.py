from .models         import TbToken
from rest_framework  import viewsets, permissions
from .serializers    import TokenSerializer


class TokenViewSet(viewsets.ModelViewSet):
    queryset = TbToken.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = TokenSerializer