from rest_framework import serializers
from .models import Agent, Light, Graph

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['positionX', 'positionY', 'angle','speed','torque']

class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = ['positionX', 'positionY', 'brightness']

class GraphSerializer(serializers.ModelSerializer):
    agent = AgentSerializer()
    light = LightSerializer()
    class Meta:
        model = Graph
        fields = ['pk','agent','light','sensor']

class CreateGraphSerializer(serializers.Serializer):
    brightness = serializers.FloatField(required=False)
    torque = serializers.FloatField(required=False)
    speed = serializers.FloatField(required=False)

class PutGraphSerializer(serializers.Serializer):
    left = serializers.BooleanField()
    right = serializers.BooleanField()