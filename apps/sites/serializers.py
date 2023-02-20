from rest_framework import serializers
from .models        import TbSite


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbSite
        fields = ( '__all__' )