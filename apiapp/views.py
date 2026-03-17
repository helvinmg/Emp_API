from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def emplist(request):
    return HttpResponse("Employee List")

def empdetail(request,pk):
    return HttpResponse("Employee Detail for Employee id: "+str(pk))
