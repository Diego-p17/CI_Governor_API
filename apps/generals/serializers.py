from rest_framework import serializers
from .models        import *



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbCountry
        fields = ('Id_Country', 'nameCountry')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TbCity
        fields = ('Id_City', 'nameCity' , 'country')

class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbDeviceType
        fields = ('Id_DeviceType', 'nameDeviceType')

class HwPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbHwPlatform
        fields = ('Id_HwPlatform', 'nameHwPlatform')

class OsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbOs
        fields = ('Id_Os', 'nameOs')

class TokenTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbTokenType
        fields = ('Id_TokenType', 'nameTokenType')

class SettingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbSettingType
        fields = ('Id_SettingType', 'nameSettingType')
