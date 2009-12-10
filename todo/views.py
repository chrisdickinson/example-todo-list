from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from models import List, Item
from django.template import RequestContext

def todo_list_all(request):
    lists = List.objects.all()
    context = {
        'lists':lists,
    }
    return render_to_response('todo/list-list.html', context, context_instance=RequestContext(request))

def todo_list(request, slug):
    list = get_object_or_404(List, slug=slug)
    context = {
        'list':list,
    }
    return render_to_response('todo/list-detail.html', context, context_instance=RequestContext(request))

def todo_list_item(request, slug, pk):
    list_item = get_object_or_404(Item, list__slug=slug, pk=int(pk))
    context = {
        'item':list_item,
    }
    return render_to_response('todo/list-item-detail.html', context, context_instance=RequestContext(request))
