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
        return TrashCan.objects.order_by('-name')[:5]

# def index(request):
#     latest_trash_list = TrashCan.objects.order_by('-name')
#     template = loader.get_template('map/index.html')
#     context = {
#         'latest_trash_list' : latest_trash_list,
#     }
#     return HttpResponse(template.render(context, request))

# def detail(request, pk):
#     trashCan = get_object_or_404(TrashCan, pk=pk)
#     return render(request, 'map/detail.html', {'trashcan': trashCan})

class DetailView(generic.DetailView):
    template_name = 'map/detail.html'
    model = TrashCan
    