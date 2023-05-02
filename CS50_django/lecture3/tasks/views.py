from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms #here we are using basic form not Modelform

# Create your views here.

class NewTask(forms.Form):
    task = forms.CharField(label = 'new task')
    priority = forms.IntegerField(label = 'Priority', min_value = 1, max_value = 10)
#line 10 is to add client side validation 
def index(request):
    if "tasks" not in request.session: #now each user will have their own session
        request.session["tasks"] = [] #to use session we need to use migrate

    return render(request, 'tasks/home.html', {
        "tasks": request.session["tasks"]
        })

def add(request):
    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task'] #basic form used, to we need to clean our data
            request.session["tasks"] += [task] #cleaned_data return dictionary value 
            return HttpResponseRedirect(reverse("tasks:index"))

        else :
            return render(request, 'tasks/add.html', { "form":form})

    return render(request, 'tasks/add.html',{
        "form":NewTask()

        })

