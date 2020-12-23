from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from random import randint
from .objList.objectsList import getObjDict

# Create your views here.
def index(request):
    return render(request,'base.html')

def data(request):
    if request.method=='GET':
        print (request.GET.get('search'))
    if request.is_ajax():
        print(request.POST.get('text'))
        return JsonResponse(getObjDict(),status=200)

    return render(request,'ajax.html',{'objs':getObjDict().keys()}) # 