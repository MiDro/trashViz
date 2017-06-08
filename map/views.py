from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import TrashCan

def index(request):
    latest_trash_list = TrashCan.objects.order_by('-name')
    template = loader.get_template('map/index.html')
    context = {
        'latest_trash_list' : latest_trash_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, trashCan_id):
    trashCan = get_object_or_404(TrashCan, pk=trashCan_id)
    return render(request, 'map/detail.html', {'TrashCan': trashCan})
