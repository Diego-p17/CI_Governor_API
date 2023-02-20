from .models         import TbPeople
from rest_framework  import viewsets, permissions
from .serializers    import PeopleSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = TbPeople.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class   = PeopleSerializer