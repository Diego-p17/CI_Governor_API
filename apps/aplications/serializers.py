from rest_framework import serializers
from .models        import TbAplication, TbSection

class AplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbAplication
        fields = ('__all__')

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbSection
        fields = ('__all__')