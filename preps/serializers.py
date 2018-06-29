from rest_framework import serializers
from .models import Stage, Action, Sample


class ActionSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = ['name']


class StageSerializer(serializers.ModelSerializer):
    actions = ActionSerialiser(many=True)

    class Meta:
        model = Stage
        fields = ['name', 'actions', 'date', 'active']


class SampleSerializer(serializers.HyperlinkedModelSerializer):
    stages = StageSerializer(many=True)

    class Meta:
        model = Sample
        fields = ('sid', 'stages')
