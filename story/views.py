from django.shortcuts import render, get_object_or_404

from .models import Story

def index(request):
    stories = Story.objects.all()
    context = {'stories': stories}
    return render(request, 'index.html', context)

def detail(request, story_id):
    question = get_object_or_404(Story, pk=story_id)
    return render(request, 'story.html', {'story': question})
