from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import TrashCan

class IndexView(generic.ListView):
    template_name = 'map/index.html'
    context_object_name = 'latest_trash_list'

    def get_queryset(self):
        """ Return the last five published questions. """
        return TrashCan.objects.order_by('-name')[::-1]


class DetailView(generic.DetailView):
    template_name = 'map/detail.html'
    model = TrashCan

class MapView(generic.ListView):
    template_name = "map/map.js"
    context_object_name = "latest_trash_list"

    def get_queryset(self):
        """ Return the last five published questions. """
        return TrashCan.objects.order_by('-name')[::-1]
