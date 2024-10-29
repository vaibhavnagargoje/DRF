from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.


# Model objects -
def student_detail(request,key):
    stu = Student.objects.get(id =key)
    print(stu)
    serializer = StudentSerializers(stu)
    print(serializer)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    print(type(stu))
    print(json_data)

    return HttpResponse(json_data,content_type='application/json')


def student_list(request):
    stu = Student.objects.all()
    serializer =StudentSerializers(stu,many = True)
    json_data = JSONRenderer().render(serializer.data)

    
    return HttpResponse(json_data,content_type='application/json')