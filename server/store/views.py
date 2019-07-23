from django.http import HttpResponse
from . import models
from . import seedscript


def index(request):
    return HttpResponse('at the index')

def readfromfile():
    data = seedscript.data()
    print(data)
    return data

def data(request):
    data = readfromfile()
    response = HttpResponse(data)
    return response