from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HTTPResponse('Welcome to the gallery App')
