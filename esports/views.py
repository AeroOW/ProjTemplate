from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from esports.models import Esport
from esports.serializers import esportserializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "esports/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = esport.objects.all()
    return render(request, "esports/index.html", {'esports': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'esports/index.html'

    def get(self, request):
        queryset = esport.objects.all()
        return Response({'esports': queryset})


class list_all_esports(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'esports/esport_list.html'

    def get(self, request):
        queryset = esport.objects.all()
        return Response({'esports': queryset})


@api_view(['GET', 'POST', 'DELETE'])
def esport_list(request):
    if request.method == 'GET':
        esports = esport.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            esports = esports.filter(name__icontains=name)

        esports_serializer = esportserializer(esports, many=True)
        return JsonResponse(esports_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        esport_data = JSONParser().parse(request)
        esport_serializer = esportserializer(data=esport_data)
        if esport_serializer.is_valid():
            esport_serializer.save()
            return JsonResponse(esport_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(esport_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = esport.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} esports were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def esport_detail(request, pk):
    try:
        esport = esport.objects.get(pk=pk)
    except esport.DoesNotExist:
        return JsonResponse({'message': 'The esport does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        esport_serializer = esportserializer(esport)
        return JsonResponse(esport_serializer.data)

    elif request.method == 'PUT':
        esport_data = JSONParser().parse(request)
        esport_serializer = esportserializer(esport, data=esport_data)
        if esport_serializer.is_valid():
            esport_serializer.save()
            return JsonResponse(esport_serializer.data)
        return JsonResponse(esport_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        esport.delete()
        return JsonResponse({'message': 'esport was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def esport_list_pc(request):
    esports = esport.objects.filter(type="PC/Console")

    if request.method == 'GET':
        esports_serializer = esportserializer(esports, many=True)
        return JsonResponse(esports_serializer.data, safe=False)

@api_view(['GET'])
def esport_list_mobile(request):
    esports = esport.objects.filter(type="Mobile")

    if request.method == 'GET':
        esports_serializer = esportserializer(esports, many=True)
        return JsonResponse(esports_serializer.data, safe=False)
