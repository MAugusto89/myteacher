from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HomeApiView(APIView):
    def get(self, request, format=None):
        return Response({"Nome":"Marcelo"}, status=200)
