from django.dispatch import receiver
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from classproject import settings
from onlineapp.serializers import *
from onlineapp.models import *
from rest_framework import status
from django.db.models.signals import post_save
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication,TokenAuthentication))
@permission_classes((IsAuthenticated,))
def rest_college(request):
    if request.method == 'GET':
        college=College.objects.all()

        serial=CollegeSerialize(college,many=True)
        return Response(serial.data)
    if request.method == 'POST':
        serializer = CollegeSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def rest_college_i(request,clgid):
    if request.method == 'GET' :
        college = College.objects.filter(id=clgid)
        serial = CollegeSerialize(college, many=True)
        return Response(serial.data)

    if request.method == 'PUT':
        clg = College.objects.get(id=clgid)
        serializer = CollegeSerialize(clg,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        College.objects.get(id=clgid).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


