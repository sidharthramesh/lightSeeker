from django.test import TestCase
from .serializers import GraphSerializer
from .models import Graph, Agent, Light
from rest_framework.renderers import JSONRenderer
# Create your tests here.
class AgentTest(TestCase):
    
    def test_serializer(self):
        agent = Agent.objects.create()
        print(agent.positionX)
        light = Light.objects.create()
        graph = Graph.objects.create(agent=agent, light=light)
        print(graph.pk)
        print(JSONRenderer().render(GraphSerializer(graph).data))

    def test_create(self):
        data = """{"pk":1,"agent":{"positionX":37.499658650227964,"positionY":81.46646373717672,"angle":2.1835667330361925,"speed":0.5,"torque":0.05},"light":{"positionX":0.31190575877415583,"positionY":6.403703062221444,"brightness":0.069}}"""
        g = GraphSerializer(data=data)
        print(g.is_valid())
        print(g.errors)
