from .models         import TbPeople
from rest_framework  import viewsets, permissions
from .serializers    import PeopleSerializer


class PeopleViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]
    serializer_class   = PeopleSerializer

    def get_queryset(self):
        queryset = TbPeople.objects.all()

        userName     = self.request.query_params.get('username')
        if userName is not None:
            queryset = queryset.filter(Id_Username= userName)


        return queryset