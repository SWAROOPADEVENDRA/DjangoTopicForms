from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from app.models import *


def insert_topic(request):
    ETFO=Topicforms()
    d={'ETFO':ETFO}

    if request.method=='POST':
        ETTO=Topicforms(request.POST)

        if ETTO.is_valid():
            tn=ETTO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('Topic insert successfully')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WISE=Webpageforms()
    d={'WISE':WISE}

    if request.method=='POST':
        EWFO=Webpageforms(request.POST)

        if EWFO.is_valid():
            tn=EWFO.cleaned_data['topic_name']
            na=EWFO.cleaned_data['name']
            url=EWFO.cleaned_data['url']
            
            
            WO=Webpage.objects.get_or_create(topic_name=tn,name=na,url=url)[0]
            WO.save()
            return HttpResponse('Insert webpage create successfully')
        
        else:
            return HttpResponse('Invalid data')
    
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    ARIE=Accessrecordforms()
    d={'ARIE':ARIE}

    if request.method=='POST':
        ARIO=Accessrecordforms(request.POST)

        if ARIO.is_valid():
            na=ARIO.cleaned_data['name']
            da=ARIO.cleaned_data['date']
            au=ARIO.cleaned_data['author']
            
            
            AR=AccessRecord.objects.get_or_create(name=na,date=da,author=au)[0]
            AR.save()
            return HttpResponse('Insert AccessRecord create successfully')
        
        else:
            return HttpResponse('Invalid data')
    
    return render(request,'insert_access.html',d)