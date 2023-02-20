from rest_framework import serializers
from .models        import TbToken


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbToken
        fields = ( '__all__' )