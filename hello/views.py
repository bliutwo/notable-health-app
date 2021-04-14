import requests
import os

from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import DataParser

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    # return render(request, "index.html")
    # r = requests.get('http://httpbin.org/status/418')
    # print(r.text)
    # return HttpResponse('<pre>' + r.text + '</pre>')
    # times = int(os.environ.get('TIMES',3))
    # return HttpResponse('Hello! ' * times)
    return render(request, "notable.html")

def results(request):
    dp = DataParser()
    context = {
        'patient_data': dp.patient_data,
        'physician_data': dp.physician_data,
        'physicians': dp.physicians,
    }
    return render(request, "results.html", context)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
