from django.shortcuts import render,render_to_response
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.
def poll_list(req):
    polls = poll.objects.all()
    return render_to_response('poll_list.html',{"polls":polls})

class PollList(ListView):
    model = poll

class PollDetel(DetailView):
    model = poll

    def get_context_data(self, **kwargs):
        ctx = super ().get_context_data(**kwargs)
        ctx['option']=Option.object.filter(poll_idself.kwargs['pk'])
        return ctx