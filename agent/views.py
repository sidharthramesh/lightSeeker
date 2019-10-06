from rest_framework.views import APIView
from django.views.generic import TemplateView
from .models import Graph, Light, Agent
from .serializers import CreateGraphSerializer, PutGraphSerializer, GraphSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class AgentView(APIView):
    def get(self, request, pk):
        graph = Graph.objects.get(pk=pk)
        graph = GraphSerializer(graph)
        return Response(graph.data)
    def put(self, request, pk):
        action = PutGraphSerializer(data=request.data)
        if action.is_valid():
            graph = Graph.objects.get(pk=pk)
            graph.step(**action.validated_data)
            return Response(GraphSerializer(graph).data)
        else:
            return Response(action.errors)
    def delete(self, request, pk):
        graph = Graph.objects.get(pk=pk)
        graph.delete()
        return Response({"status":"deleted"})

@method_decorator(csrf_exempt, name='dispatch')
class AgentCreate(APIView):
    def post(self, request):
        params = CreateGraphSerializer(data=request.data)
        if params.is_valid():
            try:
                brightness = params.validated_data.pop("brightness")
                light = Light.objects.create(brightness=brightness)
            except KeyError:
                light = Light.objects.create()
            agent = Agent.objects.create(**params.validated_data)
            graph = Graph.objects.create(agent=agent, light=light)
            return Response(GraphSerializer(graph).data)
        else:
            return Response(params.errors)

class HomeView(TemplateView):
    template_name = "visualize.html"