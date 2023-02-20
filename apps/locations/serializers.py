from rest_framework import serializers
from .models        import TbLocation


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbLocation
        fields = ( '__all__' )