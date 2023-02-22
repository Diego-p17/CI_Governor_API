from rest_framework import serializers
from .models        import TbPackageConfig


class PackageConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbPackageConfig
        fields = ( '__all__' )