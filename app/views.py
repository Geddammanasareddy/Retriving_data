from django.shortcuts import render

# Create your views here.
from django.db.models.functions import Length
from app.models import *
def display_topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}


    return render(request,'display_topic.html',context=d)

def display_webpage(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='cricket')
    #LOW=Webpage.objects.get(topic_name='football')
    LOW=Webpage.objects.exclude(topic_name='cricket')
    LOW=Webpage.objects.all()[1:3:]
    LOW=Webpage.objects.all().order_by('name')        
    LOW=Webpage.objects.all().order_by('-name')
    LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length('name').desc())
    d={'webpages':LOW}
    return render(request,'display_webpage.html',context=d)



def display_AccessRecords(request):
    LOA=AccessRecords.objects.all()
    LOA=AccessRecords.objects.filter(date__gt='2022-10-12')
    LOA=AccessRecords.objects.filter(date__lt='2022-10-12')
    LOA=AccessRecords.objects.filter(date__gte='2022-8-31')
    LOA=AccessRecords.objects.filter(date__lte='2022-11-8')



    d={'access':LOA}
    return render(request,'display_AccessRecords.html',context=d)

