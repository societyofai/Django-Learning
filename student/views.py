from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

def index(request):
    # data = Student.objects.all() # querying the data
    data = Student.objects.filter(studentClass='10') # querying the data
    details = {
        'data': data
    }
    return render(request, 'student/index.html', details)

def inputData(request):
    stdForm = StudentForm()
    stdForm = {
        'form': stdForm
    }
    if request.method == 'POST':
        details = StudentForm(request.POST)
        if details.is_valid():
            return HttpResponse("details saved")
        return HttpResponse("Error in process student details")
    if request.method == 'GET':
        return render(request, 'student/input_data.html', stdForm)
