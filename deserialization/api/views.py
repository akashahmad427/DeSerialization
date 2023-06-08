from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import Serializerdata
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = Serializerdata(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'your data has been saved succussfully'}
            return JsonResponse(res)
        