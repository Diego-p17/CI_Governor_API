from rest_framework import serializers
from .models        import TbPackageConfigKeys


class PackageConfigKeysSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbPackageConfigKeys
        fields = ( '__all__' )