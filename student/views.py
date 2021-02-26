from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def index(request):
    # data = Student.objects.all() # querying the data
    data = Student.objects.filter(studentClass='10') # querying the data
    details = {
        'data': data
    }
    return render(request, 'student/index.html', details)

