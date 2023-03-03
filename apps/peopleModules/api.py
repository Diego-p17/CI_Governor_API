from .models         import TbPeopleModule
from rest_framework  import viewsets, permissions
from .serializers    import PeopleModuleSerializer


class PeopleModuleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class   = PeopleModuleSerializer

    def get_queryset(self):
        queryset = TbPeopleModule.objects.all()

        people = self.request.query_params.get('user')
        module = self.request.query_params.get('app')

        if people is not None:
            queryset = queryset.filter(people = people)
        if module is not None:
            queryset = queryset.filter(aplication = module)

        return queryset