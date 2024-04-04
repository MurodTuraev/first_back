from django.shortcuts import render
from rest_framework.views import APIView
from new_app.seriliazers import NewsSerializer
from django.http import HttpResponse
from new_app.tasks import get_data_from_olx

# Create your views here.
class NewAppView(APIView):
    def post(self, request, format=None):
        serializers = NewsSerializer(data=request.data)

def index(request):
    get_data_from_olx.delay()
    return HttpResponse("Hello, world. You're at the")