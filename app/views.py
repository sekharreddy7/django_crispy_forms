from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *


def contact(request):
    form=contactforms()
    return render(request,'contact_form.html',context={'form':form})

def hai(request,name):
    return HttpResponse('hello how {}'.format(name))