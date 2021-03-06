import re
from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from drfapp.serializers import StudentSerializer
from drfapp.models import Student

class TestView(APIView):
    permission_classes = (IsAuthenticated)

    def get(self, request, *args, **kwargs):
        # For all
        qs = Student.objects.all()
        serializer = StudentSerializer(qs, many = True)
        # For one object
        # student1 = qs.first()
        # serializer = StudentSerializer(student1)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)