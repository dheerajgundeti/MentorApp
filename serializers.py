from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from onlineapp.models import *

class CollegeSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=College
        fields=('id','name','location','acronym','contact')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields = "__all__"

class MockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=MockTest1
        fields = "__all__"

