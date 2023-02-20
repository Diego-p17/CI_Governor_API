from rest_framework import serializers
from .models        import TbOrganization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbOrganization
        fields = ( '__all__' )
        