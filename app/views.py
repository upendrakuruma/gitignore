from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
# Create your views here.
@api_view(['GET'])
def api(request):
    student_obj= Student.objects.all()
    seriali = Studentserializers(student_obj,many=True)
    return Response(seriali.data)

@api_view(['POST'])
def apii(request):
    student_obj= Student.objects.all()
    seriali = Studentserializers(data=request.data)
    if seriali.is_valid():
        seriali.save()
    return Response(seriali.data)

@api_view(['POST'])
def update(request,id):
    stu_obj= Student.objects.get(id=id)
    seriali = Studentserializers(instance=stu_obj,data=request.data)
    if seriali.is_valid():
        seriali.save()
    return Response(seriali.data)


@api_view(['DELETE'])
def delete(request,id):
    stu_obj= Student.objects.get(id=id)
    stu_obj.delete()
    return Response('Student deleted')