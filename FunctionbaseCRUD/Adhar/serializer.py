from .models import Adharcard
from rest_framework import serializers


class AdharSerializer(serializers.Serializer):
    aid = serializers.IntegerField()
    aname = serializers.CharField(max_length=100)
    anumber = serializers.IntegerField()
    aadd= serializers.CharField(max_length=200)


    def create(self, validated_data):
        return Adharcard.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.aid = validated_data.get('aid', instance.aid)
        instance.aname = validated_data.get('aname', instance.aname)
        instance.anumber = validated_data.get('anumber', instance.anumber)
        instance.aadd = validated_data.get('aadd', instance.aadd)

        instance.save()
        return instance
