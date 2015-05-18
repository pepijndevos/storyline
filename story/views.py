from .models import Story

from django.views import generic

class IndexView(generic.ListView):
    template_name = 'index.html'
    model = Story

class DetailView(generic.DetailView):
    template_name = 'story.html'
    model = Story
