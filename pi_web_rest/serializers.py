from datetime import datetime

from rest_framework import serializers


class PIValue(object):
    def __init__(self, tag, timestamp, value):
        self.tag = tag
        self.timestamp = timestamp
        self.value = value

class PIRecordedValues(object):
    def __init__(self, tag, begin, end, values=[]):
        self.tag = tag
        self.begin = begin
        self.end = end
        self.values = values

class PIValueSerializer(serializers.Serializer):
    tag =serializers.CharField(max_length=80)
    timestamp = serializers.DateTimeField()
    value = serializers.FloatField()

class PIRecordedValuesSerializer(serializers.Serializer):
    tag = serializers.CharField(max_length=80)
    begin = serializers.CharField(max_length=50)
    end = serializers.CharField(max_length=50)
    values = serializers.ListField(allow_empty=True)

