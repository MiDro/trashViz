from rest_framework import serializers
from django.contrib.auth.models import User
from processing.models import TrashCan
import requests
from processing.models import DEFAULT_STR, DEFAULT_DEC, DEFAULT_INT

def get_adr(lat, lng):
    # TODO: implement this
    return "101"
def get_name():
    # Number of trash cans
    num = len(TrashCan.objects.all()) + 1

    if num < 10:
        num = "0"+str(num)
    else:
        num = str(num)
    return "TrashCan" + num
def get_id():
    return len(TrashCan.objects.all()) + 1

class TrashCanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashCan
        fields =  ('header', 'payload')
    header  = serializers.JSONField(binary=False)
    payload = serializers.JSONField(binary=False)


    def create(self, validated_data):
        """
        Create and return a new `TrashCan` instance, given the validated data.
        """

        head = validated_data['header']
        load = validated_data['payload']

        lat = load.get('latitude',   DEFAULT_DEC)
        lng = load.get('longitude',  DEFAULT_DEC)

        final_data = {
            'messageID':   head.get('messageID',  DEFAULT_STR),
            'sensorID':    head.get('sensorID',   DEFAULT_STR),
            'macAddress':  head.get('macAddress', DEFAULT_STR),
            'name':        get_name(),
            'longitude':   lng,
            'latitude':    lat,
            'longitude':   get_adr(lat, lng),
            'trashID':     get_id(),
            'header':      head,
            "payload":     load,
            'bt':          validated_data['bt'],
            'ver':         validated_data['ver'],
            'bn':          validated_data['bn']
        }

        return TrashCan.objects.create(**final_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `TrashCan` instance, given the validated data.
        """

        print("BRUH")

        instance.header  = validated_data.get('header',   instance.header)
        instance.payload = validated_data.get('payload',  instance.payload)
        instance.bt      = validated_data.get('bt',       instance.bt)
        instance.v       = validated_data.get('ver',      instance.v)
        instance.bn      = validated_data.get('bn',       )

        instance.messageID = head['messageID']

        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    trashcans = serializers.HyperlinkedRelatedField(
        many=True, view_name='trashcan-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'trashcans')
