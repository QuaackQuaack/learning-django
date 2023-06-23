from django.shortcuts import render

from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView 

from .models import Post

# Create your views here.

class ListPageView(ListView):
    template_name = "task.html"
    model = Post
    context_object_name = 'all_task'


class CreatePageView(CreateView):
    fields = ["task"] 
    model = Post
    template_name = "new_task.html"

#class TaskPageView(View):
#    def get(self, request):
#        tasks = ["foo", "bar", "baz"]
#        context = {
#                "tasks": tasks}
#        return render(request, "../templates/task1.html", context)
#


