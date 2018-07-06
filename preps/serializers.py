from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

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


class StageCreateSerializer(serializers.ModelSerializer):
    action = PrimaryKeyRelatedField(queryset=Action.objects.all())
    sample = PrimaryKeyRelatedField(queryset=Sample.objects.all())

    class Meta:
        model = Stage
        fields = ['action', 'sample']


class SampleSerializer(serializers.HyperlinkedModelSerializer):
    stages = StageSerializer(many=True)

    class Meta:
        model = Sample
        fields = ('sid', 'stages')
