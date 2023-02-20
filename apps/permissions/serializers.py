from rest_framework import serializers
from .models        import TbPermission


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbPermission
        fields = ( '__all__' )