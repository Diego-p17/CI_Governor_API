from rest_framework import viewsets, permissions
from .models        import TbAplication
from . serializers  import AplicationSerializer

class AplicationViewSet(viewsets.ModelViewSet):
    queryset = TbAplication.objects.all()
    permission_classes = [ permissions.AllowAny]
    serializer_class   = AplicationSerializer