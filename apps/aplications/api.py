from rest_framework import viewsets, permissions
from .models        import TbAplication, TbModule, TbSection
from . serializers  import AplicationSerializer, ModuleSerializer, SectionSerializer

class AplicationViewSet(viewsets.ModelViewSet):
    permission_classes = [ permissions.AllowAny]
    serializer_class   = AplicationSerializer

    def get_queryset(self):
        queryset     = TbAplication.objects.all()

        isActive     = self.request.query_params.get('active')

        if isActive is not None:
            queryset = queryset.filter(isActive= isActive)

        return queryset

class ModuleViewSet(viewsets.ModelViewSet):
    permission_classes = [ permissions.AllowAny]
    serializer_class   = ModuleSerializer

    def get_queryset(self):
        queryset = TbModule.objects.all()

        aplication = self.request.query_params.get('app')

        if aplication is not None:
            queryset = queryset.filter(aplication= aplication)

        return queryset

class SectionViewSet(viewsets.ModelViewSet):
    permission_classes = [ permissions.AllowAny]
    serializer_class   = SectionSerializer

    def get_queryset(self):
        queryset     = TbSection.objects.all()

        aplication = self.request.query_params.get('app')

        if aplication is not None:
            queryset = queryset.filter(aplication= aplication)

        return queryset