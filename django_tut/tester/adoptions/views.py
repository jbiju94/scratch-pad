from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p> Woolaa!!!</p>')

def view_detail(request,id):
    return HttpResponse('<p> Woolaa!!! You put in {} as id</p>'.format(id))

