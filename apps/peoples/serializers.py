from rest_framework import serializers
from .models        import TbPeople


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TbPeople
        fields = ( '__all__' )