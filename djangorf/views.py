from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'admin',
            'years_active': 10
        }
        return Response(data)