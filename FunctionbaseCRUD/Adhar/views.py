from .models import Adharcard
from rest_framework import status
from Adhar.serializer import AdharSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
# Create your views here.
@csrf_exempt
def adharGetView(request):
    adhar = Adharcard.objects.all()
    serializer = AdharSerializer(adhar, many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

@csrf_exempt
def adharPostView(request):
    data = JSONParser().parse(request)
    serializer = AdharSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200, safe=False)
    return JsonResponse(serializer.errors, status=status.HTTP_201_CREATED)


@csrf_exempt
def AdharInfo(request, pk):
    try:
        adhar = Adharcard.objects.get(pk=pk)
    except Adharcard.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        serializer = AdharSerializer(adhar)
        return JsonResponse(serializer.data)
  
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AdharSerializer(adhar, data=data)
  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        adhar.delete()
        return HttpResponse(status=204)



