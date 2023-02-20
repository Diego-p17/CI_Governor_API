from rest_framework import serializers
from .models        import TbSetting


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbSetting
        fields = ( '__all__' )