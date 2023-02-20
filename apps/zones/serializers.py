from rest_framework import serializers
from .models        import TbZone


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbZone
        fields = ( '__all__' )