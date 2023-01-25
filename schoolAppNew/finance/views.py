from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def feeCollection(request):
    return HttpResponse("<h1>I will collect the fee from this view<h1>")

def feeDuesReport(request):
    return HttpResponse("<h1>I will get fee dues report from this views<h1>")

def feeCollectionReport(request):
    return HttpResponse("<h1>I will fee collect report from this view<h1>")
