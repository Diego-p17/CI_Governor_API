from rest_framework import serializers
from .models        import TbPeopleModule


class PeopleModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbPeopleModule
        fields = ( '__all__' )