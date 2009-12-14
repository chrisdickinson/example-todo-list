from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from models import List, Item
from django.template import RequestContext
from django import forms

class CompletionForm(forms.Form):
    user = forms.IntegerField(widget=forms.widgets.HiddenInput)
    is_done = forms.ChoiceField(choices=(
        (False, 'Incomplete',),
        (True, 'Complete',),
    ))

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

    completion_form = None
    if request.user.is_authenticated():
        completion_form = CompletionForm({'user':request.user.pk, 'is_done':list_item.is_done})
        if request.method == 'POST':
            completion_form = CompletionForm(request.POST)
            if completion_form.is_valid():
                user = User.objects.get(pk=int(completion_form.cleaned_data['user']))
                if user == list_item.list.owner:
                    list_item.is_done = completion_form.cleaned_data['is_done']
                    list_item.save()
                    return HttpResponseRedirect(list_item.get_absolute_url()) 

    context = {
        'item':list_item,
        'completion_form':completion_form,
    }
    return render_to_response('todo/list-item-detail.html', context, context_instance=RequestContext(request))
