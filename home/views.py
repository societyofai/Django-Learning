from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from rest_framework import viewsets, renderers
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers

def index(request):
    courses = Course.objects.all()
    # return HttpResponse("home page")
    return render(request, 'home/index.html')


class CourseApiView(APIView):

    def get(self, request, format=None):
        query = Course.objects.all()
        serializer = CourseSerializer(query, many=True)
        # return Response({'items': serializer.data})
        return Response(serializer.data)


