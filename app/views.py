from django.shortcuts import render
from django.http import HttpResponse

def generic(request):
    return HttpResponse('<h1><marquee><i><b>My generic urls</b></i></marquee></h1>')


