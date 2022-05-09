from . models import Book
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    bid = serializers.IntegerField()
    bname= serializers.CharField(max_length=100)
    bauthor= serializers.CharField(max_length=100)
    bqty = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.bid = validated_data.get('bid', instance.bid)
        instance.bname = validated_data.get('bname', instance.bname)
        instance.bauthor = validated_data.get('bauthor', instance.bauthor)
        instance.bqty = validated_data.get('bqty', instance.bqty)

        instance.save()
        return instance
        
