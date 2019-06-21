from django.http import HttpResponse
# import pymysql
from . import models
from . import seedscript

def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def sendtodb():
    data = seedscript.data()
    print(data)
