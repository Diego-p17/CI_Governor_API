from rest_framework import serializers
from .models        import TbConfiguration


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbConfiguration
        fields = ( '__all__' )