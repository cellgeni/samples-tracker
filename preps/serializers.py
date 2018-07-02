from rest_framework import serializers
from .models import Stage, Action, Sample


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = ['name']


class StageSerializer(serializers.ModelSerializer):
    action = ActionSerializer()

    class Meta:
        model = Stage
        fields = ['action', 'date', 'active']


class SampleSerializer(serializers.HyperlinkedModelSerializer):
    stages = StageSerializer(many=True)

    class Meta:
        model = Sample
        fields = ('sid', 'stages')
