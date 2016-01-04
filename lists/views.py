from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#function that does not do anything, makes the resolver happy
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')
