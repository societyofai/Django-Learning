from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from rest_framework import viewsets, renderers
from .serializers import CourseSerializer, AddCourseSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
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

class AddCourseApiView(APIView):

    def post(self, request, format=None):
        courseDetails = AddCourseSerializer(data = request.data)
        # immutable dictionary 
        # courseDetails = AddCourseSerializer(request.data)
        if courseDetails.is_valid():
            # return Response(courseDetails.data, status=status.HTTP_200_OK)
            return Response({'message': 'Values saved successfully'}, status=status.HTTP_201_CREATED)
        return Response(courseDetails.errors, status=status.HTTP_400_BAD_REQUEST)  


