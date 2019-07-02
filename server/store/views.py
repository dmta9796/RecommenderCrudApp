from django.http import HttpResponse
from . import models
from . import seedscript


def index(request):
    return HttpResponse('at the index')

def sendtodb():
    data = seedscript.data()
    return data

def data(request):
    data = sendtodb()
    #print(data)
    response = HttpResponse(data)
    #print(response)
    return response