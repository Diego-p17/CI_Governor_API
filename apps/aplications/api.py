from rest_framework import viewsets, permissions
from .models        import TbAplication, TbSection
from . serializers  import AplicationSerializer, SectionSerializer

class AplicationViewSet(viewsets.ModelViewSet):
    permission_classes = [ permissions.AllowAny]
    serializer_class   = AplicationSerializer

    def get_queryset(self):
        queryset     = TbAplication.objects.all()

        isActive     = self.request.query_params.get('active')
        aplication   = self.request.query_params.get('app')

        if isActive is not None:
            queryset = queryset.filter(isActive= isActive)
        if aplication is not None:
            queryset = queryset.filter(nameAplication= aplication)

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
    
    