from django.http import HttpResponse
from django.http import JsonResponse
# import pymysql
from . import models
from . import seedscript


def index(request):
    return HttpResponse('at the index')

def sendtodb():
    data = seedscript.data()
    return data

def data(request):
    data = sendtodb()
    #response = HttpResponse(data)
    response = HttpResponse(data, content_type='text/plain')
    #print(response)
    return response