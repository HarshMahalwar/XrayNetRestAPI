from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response


class ResultApiView(APIView):
    serializer_class = ResultSerializer

    def get(self, request):
        context = results.objects.all().values()
        return Response({"list": context})

    def post(self, request):
        obj = ResultSerializer(data=request.data)
        if obj.is_valid():
            results.objects.create(id=obj.data.get("id"),result=obj.data.get("result"), Name=obj.data.get("Name"))
        context = results.objects.all().filter(id=request.data["id"]).values()
        return Response({'list': context})
