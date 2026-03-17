from django.http import HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def emplist(request):
    records=Employee.objects.all()#queryset
    #serializer convert queryset to simplified data
    serializer=EmployeeSerializer(records,many=True)
    return Response(serializer.data)

def empdetail(request,pk):
    return HttpResponse("Employee Detail for Employee id: "+str(pk))
