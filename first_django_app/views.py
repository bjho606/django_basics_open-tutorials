from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    # return HttpResponse('Welcome!')
    result = '<h1>Random</h1>' + str(random.random())
    return HttpResponse(result)

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!' + id)