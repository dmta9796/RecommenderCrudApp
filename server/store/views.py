from django.http import HttpResponse
# import pymysql
from . import models
from . import seedscript

def index(request):
    data = sendtodb()
    return HttpResponse(data)


def sendtodb():
    data = seedscript.data()
    return data
