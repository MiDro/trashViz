from rest_framework import serializers
from django.contrib.auth.models import User
from processing.models import TrashCan


class TrashCanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashCan
        fields = ('url', 'lastEmptied', 'lastUpdated', 'sensor1', 'sensor2', 'sensor3', 'fillLevel', 'percent', 'full_status', 'latitude', 'longitude', 'location', 'info', 'maxFill', 'installDate', 'trashID', 'owner')
    lastEmptied = serializers.DateTimeField(required=False)
    lastUpdated = serializers.DateTimeField(required=True)
    sensor1 = serializers.IntegerField(min_value=0.0, required=True)
    sensor2 = serializers.IntegerField(min_value=0.0, required=True)
    sensor3 = serializers.IntegerField(min_value=0.0, required=True)
    fillLevel = serializers.DecimalField(max_digits=None, decimal_places=3, min_value=0.0, default=50.000)  # generated
    percent = serializers.DecimalField(max_digits=5, decimal_places=2, min_value=0.0, default=50.00)  # generated
    full_status = serializers.BooleanField(required=False)  # generated
    latitude = serializers.DecimalField(max_digits=None, decimal_places=6, min_value=None, required=False)
    longitude = serializers.DecimalField(max_digits=None, decimal_places=6, min_value=None, required=False)
    location = serializers.CharField(max_length=400, read_only=True, required=False)
    info = serializers.CharField(max_length=500, read_only=True)
    maxFill = serializers.DecimalField(max_digits=None, decimal_places=3, min_value=0.0, required=False)
    installDate = serializers.DateTimeField('installed', read_only=True)
    trashID = serializers.IntegerField(min_value=0, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')


    def create(self, validated_data):
        """
        Create and return a new `TrashCan` instance, given the validated data.
        """
        return TrashCan.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `TrashCan` instance, given the validated data.
        """
        instance.lastEmptied = validated_data.get(
                'lastEmptied', instance.lastEmptied)
        instance.lastUpdated = validated_data.get(
                'lastUpdated', instance.lastUpdated)
        instance.sensor1 = validated_data.get('sensor1', instance.sensor1)
        instance.sensor2 = validated_data.get('sensor2', instance.sensor2)
        instance.sensor3 = validated_data.get('sensor3', instance.sensor3)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    trashcans = serializers.HyperlinkedRelatedField(many=True, view_name='trashcan-detail', read_only=True)
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'trashcans')
