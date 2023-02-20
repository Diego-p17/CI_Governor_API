from rest_framework import serializers
from .models        import TbDevice


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbDevice
        fields = ( '__all__' )