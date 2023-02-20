from rest_framework import serializers
from .models        import TbKey


class KeysSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbKey
        fields = ( '__all__' )