from django.shortcuts import render
from django.http import HttpResponse
from sections.models import Section
from trainers.models import Trainer

# Create your views here.
def index(request):
    #return HttpResponse('<h1>Hello</h1>')
    sections = Section.objects.order_by('title').filter(is_published=True)
    trainers = Trainer.objects.order_by('first_name')
    context = {
        'sections': sections,
        'trainers': trainers,
    }
    return render(request, 'pages/index.html', context) #


def about(request):
    ## Get all realtors
    # realtors = Realtor.objects.order_by('-hire_date')
    #
    # # Get MVP
    # mpv_realtors = Realtor.objects.all().filter(is_mpv=True)
    # context = {
    #     'realtors': realtors,
    #     'mvp_realtors': mpv_realtors
    # }
    # return render(request, 'pages/about.html', context)
    pass