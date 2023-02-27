
from rest_framework  import viewsets, permissions
from .serializers import LoginSerializers
from django.contrib.auth.models import User

class Loginviewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializers