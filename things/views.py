from django.shortcuts import render
from django.db.models import F
from .models import *

# Create your views here.
def thing_list(request):
    things = Thing.objects.all() #instanse things
    return render(request,'things/thing_list.html',{'things':things})
  #  return HttpResponse(things)


def thing_detail(request,pk):         # provide pk thru url
    thing = Thing.objects.get(pk=pk)
    return render(request, 'things/thing_detail.html',{'thing':thing})

def step_detail(request,thing_pk, step_pk):
    print "inside stepdetail"
    step = Step.objects.get( thing_id = thing_pk, pk=step_pk)

    return render(request, 'things/step_detail.html',{'step':step})

def step_detail1(request,thing_pk, step_pk):
    print "inside stepdetail1"
    step = Step.objects.get( thing_id = thing_pk, pk=step_pk)
    step.number_increment = step.number_increment + 1
    step.save()
    print step.number_increment
    return render(request, 'things/step_detail.html',{'step':step})