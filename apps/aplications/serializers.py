from rest_framework import serializers
from .models        import TbAplication

class AplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbAplication
        fields = ('__all__')