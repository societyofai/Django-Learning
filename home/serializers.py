from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'
        # fields = ('name', )

class AddCourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ('name', 'description')
        # fields = ('name', )
