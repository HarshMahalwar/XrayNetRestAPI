from rest_framework import serializers


class ResultSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    result = serializers.CharField(max_length=100)
    Name = serializers.CharField(max_length=100)
